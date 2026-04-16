from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass
from typing import Any


@dataclass
class Packet:
    node_id: str
    mac: str
    rssi: int


class UDPServerProtocol(asyncio.DatagramProtocol):
    """Async UDP server that places parsed packets onto a queue."""

    def __init__(self, queue: asyncio.Queue[Packet]) -> None:
        self.queue = queue

    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None:
        try:
            payload: dict[str, Any] = json.loads(data.decode("utf-8"))
            packet = Packet(
                node_id=str(payload["node_id"]),
                mac=str(payload["mac"]).upper(),
                rssi=int(payload["rssi"]),
            )
            self.queue.put_nowait(packet)
        except (KeyError, ValueError, json.JSONDecodeError):
            return
