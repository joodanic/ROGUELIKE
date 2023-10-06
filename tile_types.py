import numpy as np

from typing import Tuple

graphic_dt = np.dtype(
    [
        ("ch",np.int32),
        ("fg","3B"),
        ("bg","3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable",bool),
        ("transparent", bool),
        ("dark",graphic_dt),
    ]
)

def new_tile(
    *,
    walkable: int,
    tranparent: int,
    dark: Tuple[int,Tuple[int,int,int],Tuple[int,int,int]],
) -> np.ndarray:
    return np.array((walkable,tranparent,dark),dtype=tile_dt)

floor = new_tile(
    walkable=True, tranparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150))
    )

wall = new_tile(
    walkable=False, tranparent=False,dark=(ord("#"), (255, 255, 255), (0, 0, 100))
)