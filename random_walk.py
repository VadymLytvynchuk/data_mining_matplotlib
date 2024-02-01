from random import choice

class RandomWalk():
    def __init__(self, num_points=500):
        self.num_points = num_points
    # Все блуждания начинаются с точки (0, 0).
        self.x_values = [0]
        self.y_values = [0]  

    def fill_walk(self):
      """Вычисляет все точки блуждания."""
      # Шаги генерируются до достижения нужной длины.
      while len(self.x_values) < self.num_points:
        # Определение направления и длины перемещения. 
         x_step = self.get_step()
         y_step = self.get_step()
         # Отклонение нулевых перемещений.
         if x_step == 0 and y_step == 0:
            continue
         # Вычисление следующих значений x и y.
         x = self.x_values[-1] + x_step
         y = self.y_values[-1] + y_step
         self.x_values.append(x)
         self.y_values.append(y)
    
    def get_step(self):
     _direction = choice([1, -1]) # значение 1 для перемещения вправо или –1 для движения влево
     _distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
     _step = _direction * _distance
     return _step
