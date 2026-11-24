import numpy as np

def vector_norm_3d(v: list) -> float | np.ndarray:
    """
    Returns a float or a NumPy array.
    """
    # Write code here
    v= np.asarray (v, dtype= np.float64)
    norm = np.linalg.norm(v, axis=-1)
    return float(norm) if v.ndim == 1 else norm
   