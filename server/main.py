from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Any

import yaml

from kalman import KalmanFilter3D
from processing import SlidingWindowProcessor
from udp_listener import Packet, UDPServerProtocol


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


async def run_server() -> None:
    config = load_config(Path(__file__).with_name("config.yaml"))

    queue: asyncio.Queue[Packet] = asyncio.Queue()
    loop = asyncio.get_running_loop()

    transport, _ = await loop.create_datagram_endpoint(
        lambda: UDPServerProtocol(queue),
        local_addr=(config["udp"]["host"], int(config["udp"]["port"])),
    )

    processor = SlidingWindowProcessor(
        node_positions={k: tuple(v) for k, v in config["nodes"].items()},
        window_ms=int(config["processing"]["window_ms"]),
        min_nodes_per_fix=int(config["processing"]["min_nodes_per_fix"]),
        tx_power_dbm=float(config["radio"]["tx_power_dbm"]),
        path_loss_exponent=float(config["radio"]["path_loss_exponent"]),
    )
    kalman_by_mac: dict[str, KalmanFilter3D] = {}

    print(f"UDP listener active on {config['udp']['host']}:{config['udp']['port']}")

    try:
        while True:
            # Drain queue quickly.
            while not queue.empty():
                pkt = queue.get_nowait()
                processor.add_reading(pkt.node_id, pkt.mac, pkt.rssi)

            fixes = processor.process()
            for mac, raw_point in fixes:
                kf = kalman_by_mac.setdefault(mac, KalmanFilter3D())
                smoothed = kf.update(raw_point)
                print(
                    f"MAC={mac} raw=({raw_point[0]:.2f}, {raw_point[1]:.2f}, {raw_point[2]:.2f}) "
                    f"smooth=({smoothed[0]:.2f}, {smoothed[1]:.2f}, {smoothed[2]:.2f})"
                )

            await asyncio.sleep(0.05)
    finally:
        transport.close()


if __name__ == "__main__":
    asyncio.run(run_server())
