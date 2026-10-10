"""Example test. Replace with real checks as you build Stage 0.

Run locally with:  python3 -m pytest
"""
import numpy as np


def mse_grad(w, x, y):
    """Gradient of mean squared error for y_hat = x @ w."""
    return 2 * x.T @ (x @ w - y) / len(y)


def test_mse_gradient_matches_finite_differences():
    rng = np.random.default_rng(0)
    x, y, w = rng.normal(size=(20, 3)), rng.normal(size=20), rng.normal(size=3)
    loss = lambda w: np.mean((x @ w - y) ** 2)
    eps = 1e-6
    numeric = np.array([(loss(w + eps * e) - loss(w - eps * e)) / (2 * eps) for e in np.eye(3)])
    assert np.allclose(mse_grad(w, x, y), numeric, atol=1e-5)
