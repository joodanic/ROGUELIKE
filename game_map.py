import numpy as np
import tile_types

from tcod.console import Console

class GameMap:
    
    def __init__(self,width: int,height: int):
        self.width = width
        self.height = height
        self.tiles = np.full((width,height), fill_value=tile_types.wall, order="F")
    
    def in_bounds(self,x: int,y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height
    
    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width,0:self.height] = self.tiles["dark"]
        
