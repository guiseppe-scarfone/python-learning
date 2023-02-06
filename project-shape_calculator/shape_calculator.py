class Rectangle:

  def __init__(self, width: int, height: int) -> None:
    self.width = width
    self.height = height

  def set_width(self, width: int) -> None:
    self.width = width

  def set_height(self, height: int) -> None:
    self.height = height

  def get_area(self) -> int:
    return self.width * self.height

  def get_perimeter(self) -> int:
    return (self.width * 2) + (self.height * 2)

  def get_diagonal(self) -> float:
    return ((self.width**2) + (self.height**2))**0.5

  def get_picture(self) -> str:
    pic = ''
    if self.height > 50 or self.width > 50:
      return 'Too big for picture.'
    else:
      for i in range(self.height):
        pic += '*' * self.width + '\n'
    return pic

  def get_amount_inside(self, shape: object) -> int:
    return int(self.get_area() / shape.get_area())

  def __str__(self) -> str:
    return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

  def __init__(self, side):
    self.height = side
    self.width = side

  def set_side(self, side) -> None:
    self.height = side
    self.width = side

  def set_height(self, side) -> None:
    self.height = side
    self.width = side

  def set_width(self, side) -> None:
    self.height = side
    self.width = side

  def __str__(self) -> str:
    return f'Square(side={self.height})'
