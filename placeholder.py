from dataclasses import dataclass



@dataclass
class Placeholder:
    x: int
    y: int
    width: int
    height: int

    def get_json(self):
        return f'{"x": {self.x}, "y": {self.y}, "height": {self.height}, "width": {self.width}}'
