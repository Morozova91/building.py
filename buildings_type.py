# Перегрузка операторов
# 1) Создайте новый класс Building
# 2) Создайте инициализатор для класса Building, который будет задавать
# целочисленный атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
# 3) Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашнему заданию

class Building:  # Создайте новый класс Building
    def __init__(self, number_of_floors: int, building_type: str):  #инициализатор для класса Building
        self.number_of_floors = number_of_floors
        self.building_type = building_type

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and self.building_type == other.building_type


wed = Building(5, '4')
print(wed)
