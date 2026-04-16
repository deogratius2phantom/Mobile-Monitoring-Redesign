from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from time import monotonic
from typing import Deque, Dict, List, Tuple

from trilateration import solve_position


@dataclass
class Reading:
    node_id: str
    mac: str
    rssi: int
    ts: float


class SlidingWindowProcessor:
    """Groups RSSI readings per target MAC in a sliding time window and estimates position."""

    def __init__(
        self,
        node_positions: Dict[str, Tuple[float, float, float]],
        window_ms: int,
        min_nodes_per_fix: int,
        tx_power_dbm: float,
        path_loss_exponent: float,
    ) -> None:
        self.node_positions = node_positions
        self.window_s = window_ms / 1000.0
        self.min_nodes_per_fix = min_nodes_per_fix
        self.tx_power_dbm = tx_power_dbm
        self.path_loss_exponent = path_loss_exponent
        self.readings_by_mac: Dict[str, Deque[Reading]] = defaultdict(deque)

    def add_reading(self, node_id: str, mac: str, rssi: int) -> None:
        now = monotonic()
        queue = self.readings_by_mac[mac]
        queue.append(Reading(node_id=node_id, mac=mac, rssi=rssi, ts=now))
        self._trim_queue(queue, now)

    def _trim_queue(self, queue: Deque[Reading], now: float) -> None:
        while queue and (now - queue[0].ts) > self.window_s:
            queue.popleft()

    def process(self) -> List[Tuple[str, Tuple[float, float, float]]]:
        now = monotonic()
        fixes: List[Tuple[str, Tuple[float, float, float]]] = []

        for mac, queue in list(self.readings_by_mac.items()):
            self._trim_queue(queue, now)
            if not queue:
                self.readings_by_mac.pop(mac, None)
                continue

            # Latest reading per node within the window.
            latest_per_node: Dict[str, int] = {}
            for r in queue:
                latest_per_node[r.node_id] = r.rssi

            if len(latest_per_node) < self.min_nodes_per_fix:
                continue

            point = solve_position(
                node_positions=self.node_positions,
                node_rssi=latest_per_node,
                tx_power_dbm=self.tx_power_dbm,
                path_loss_exponent=self.path_loss_exponent,
            )
            if point is not None:
                fixes.append((mac, point))

        return fixes
