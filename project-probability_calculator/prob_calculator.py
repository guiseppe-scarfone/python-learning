import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs) -> None:
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
 
  def draw(self, number: int) -> list:
    draw_list = []
    for i in range(number):
      if len(self.contents) > 0:
        item = random.choice(self.contents)
        draw_list.append(item)
        self.contents.remove(item)
    return draw_list

def experiment(hat: object, expected_balls: object, num_balls_drawn: int, num_experiments: int) -> float:
  success_count = 0
  for i in range(num_experiments):
    exp = copy.deepcopy(hat)
    result = exp.draw(num_balls_drawn)
    result_dict = {}
    for j in range(len(result)):
      result_dict[result[j]] = result_dict.get(result[j], 0) + 1
      #print(f'{result_dict} vs {expected_balls}')
    success = True
    for k, v in expected_balls.items():
      if result_dict.get(k, 0) < v:
        success = False
    success_count += 1 if success else 0
  
  return float(success_count / num_experiments)