from dataclasses import dataclass


@dataclass
class Placeholder():
    x: float
    y: float
    width: float
    height: float

    def get_json(self):
        return f'{{"x": {self.x}, "y": {self.y}, "height": {self.height}, "width": {self.width}}}'
    def toJSON(self):
        return {"x": {self.x}, "y": {self.y}, "height": {self.height}, "width": {self.width}}

    @staticmethod
    def get_init_param_names():
        return ['x', 'y', 'width', 'height']

# p = Placeholder(1,2,3,4)
# print(p.get_json())