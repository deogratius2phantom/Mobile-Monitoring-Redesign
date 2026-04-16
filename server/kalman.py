from __future__ import annotations

import numpy as np


class KalmanFilter3D:
    """Basic 3D position Kalman filter for coordinate smoothing."""

    def __init__(self, process_var: float = 1e-2, measurement_var: float = 5e-1) -> None:
        self.x = np.zeros((3, 1), dtype=float)
        self.P = np.eye(3, dtype=float)
        self.Q = np.eye(3, dtype=float) * process_var
        self.R = np.eye(3, dtype=float) * measurement_var
        self.H = np.eye(3, dtype=float)
        self.initialized = False

    def update(self, measurement: tuple[float, float, float]) -> tuple[float, float, float]:
        z = np.array(measurement, dtype=float).reshape((3, 1))

        if not self.initialized:
            self.x = z
            self.initialized = True
            return tuple(self.x.flatten())

        # Predict
        self.P = self.P + self.Q

        # Update
        y = z - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        self.P = (np.eye(3) - K @ self.H) @ self.P

        return tuple(self.x.flatten())
