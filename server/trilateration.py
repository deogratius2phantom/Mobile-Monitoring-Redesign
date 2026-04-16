from __future__ import annotations

from typing import Dict, Iterable, Tuple

import numpy as np
from scipy.optimize import least_squares


def rssi_to_distance(rssi: float, tx_power_dbm: float = -40.0, path_loss_exponent: float = 2.0) -> float:
    """Convert RSSI to approximate distance in meters using a log-distance path loss model."""
    if path_loss_exponent <= 0:
        raise ValueError("path_loss_exponent must be > 0")
    return 10 ** ((tx_power_dbm - rssi) / (10 * path_loss_exponent))


def _residuals(point: np.ndarray, anchors: np.ndarray, distances: np.ndarray) -> np.ndarray:
    return np.linalg.norm(anchors - point, axis=1) - distances


def solve_position(
    node_positions: Dict[str, Tuple[float, float, float]],
    node_rssi: Dict[str, float],
    tx_power_dbm: float,
    path_loss_exponent: float,
) -> Tuple[float, float, float] | None:
    """Solve a 3D point from node RSSI values via non-linear least squares trilateration."""
    available = [(nid, rssi) for nid, rssi in node_rssi.items() if nid in node_positions]
    if len(available) < 3:
        return None

    anchors = np.array([node_positions[nid] for nid, _ in available], dtype=float)
    distances = np.array(
        [rssi_to_distance(rssi, tx_power_dbm=tx_power_dbm, path_loss_exponent=path_loss_exponent) for _, rssi in available],
        dtype=float,
    )

    # Start at anchor centroid for stability.
    x0 = anchors.mean(axis=0)
    result = least_squares(_residuals, x0=x0, args=(anchors, distances), method="trf")

    if not result.success:
        return None

    return tuple(result.x.tolist())
