# Определим класс для хранения координат тчек на плоскости

# class Point:
#     "Описание класса. Определение координат на плоскости"
#     color = "red" # Переменные внутри класса
#     circle = 2    # это атрибуты класса (или его свойства)

# Чтобы создать экземпляр класса надо поставить () после его имени
# Напрмер a = Point()

# Экземпляры класса изначально наследуют атрибуты родительского класса,
# а при переопределении хранят свои

# Классы содержат
# Свойства (данные) color, size, x, y
# методы (действия) set_param, set_value, start, stop



# Объявим в нашем клссе Point метод, который будет называться set_coords

class Point:
    "Описание класса. Определение координат на плоскости"
    color = "red"
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление экземпляра " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print("Вызов метода set_coords " + str(self))

    def get_coords(self):
        return self.x, self.y

pt = Point(1,2)
print(pt.__dict__)
