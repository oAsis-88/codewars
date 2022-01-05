import copy
import sys
from termcolor import colored, cprint


class Dinglemouse(object):
    def __init__(self, queues, capacity):
        self.queues = queues  # очередь на этажах вызова
        self.capacity = capacity  # max кол-во людей в лифте
        self.callsInLiftToFloor = self.callsInLiftToFloors()  # тоже самое что и queues но в виде словаря
        self.floorLift = 0  # на каком этаже лифт
        self.people_in_lift = 0  # Кол-во людей в лифте
        self.lift = []  # Кол-во людей в лифте
        self.liftUpOrDown = "Up"  # Куда едит лифт
        self.listOfVisitedFloors = []

    def theLift(self):
        while self.callsInLiftToFloor:
            if self.liftUpOrDown == "Up":
                self.liftGoesUp()
            elif self.liftUpOrDown == "Down":
                self.liftGoesDown()
        ''' Возвращаем список посещенных этажей '''
        b = copy.deepcopy(self.listOfVisitedFloors)
        count = 0
        for i in range(len(self.listOfVisitedFloors) - 1):
            if self.listOfVisitedFloors[i] == self.listOfVisitedFloors[i + 1]:
                del b[i-count]
                count += 1
        self.listOfVisitedFloors = b
        if self.listOfVisitedFloors[0] != 0:
            self.listOfVisitedFloors.insert(0, 0)
        return self.listOfVisitedFloors

    def liftGoesUp(self):
        for floor in range(self.floorLift, len(self.queues)):
            visited_floor = False
            if self.people_in_lift == 0 and max(self.callsInLiftToFloor) < floor:
                """ Лифт поедит вниз """
                self.liftUpOrDown = "Down"  # Флаг
                self.floorLift = floor - 1  # Этаж на котором остановился лифт
                break

            ''' Люди выходят '''
            if floor in self.lift:
                while floor in self.lift:
                    self.lift.remove(floor)
                    self.people_in_lift -= 1
                visited_floor = True

            ''' Проверка на вызовы '''
            if not self.callsInLiftToFloor and self.people_in_lift == 0:
                self.floorLift = floor
                if visited_floor:
                    self.listOfVisitedFloors.append(self.floorLift)
                for i in range(self.floorLift - 2, -1, -1):  # -1 - это нету счетчика в цикле до этого условия и -1 -
                    # это на этаж ниже потому что мы уже на нем были
                    self.floorLift = i
                self.listOfVisitedFloors.append(0)
                break

            ''' Люди заходят '''
            if floor in self.callsInLiftToFloor:
                if self.people_in_lift != self.capacity:
                    a = copy.deepcopy(self.callsInLiftToFloor.get(floor))
                    for people_in_floor in a:
                        if self.people_in_lift == self.capacity:
                            break
                        if people_in_floor > floor:
                            self.lift.append(people_in_floor)
                            self.callsInLiftToFloor[floor].remove(people_in_floor)
                            self.people_in_lift += 1
                            visited_floor = True
                    if not self.callsInLiftToFloor.get(floor):
                        del self.callsInLiftToFloor[floor]

            ''' Указываем этаж лифта '''
            self.floorLift = floor

            '''  '''
            if visited_floor:
                self.listOfVisitedFloors.append(self.floorLift)
        self.liftUpOrDown = "Down"

    def liftGoesDown(self):
        for floor in range(self.floorLift, -1, -1):
            visited_floor = False
            if self.people_in_lift == 0 and min(self.callsInLiftToFloor) > floor:
                """ Лифт поедит вверх """
                self.liftUpOrDown = "Up"  # Флаг
                self.floorLift = floor + 1  # Этаж на котором остановился лифт
                break

            ''' Люди выходят '''
            if floor in self.lift:
                while floor in self.lift:
                    self.lift.remove(floor)
                    self.people_in_lift -= 1
                visited_floor = True

            ''' Проверка на вызовы '''
            if not self.callsInLiftToFloor and self.people_in_lift == 0:
                self.floorLift = floor
                if visited_floor:
                    self.listOfVisitedFloors.append(self.floorLift)
                for i in range(self.floorLift - 1, -1, -1):  # -1 - это нету счетчика в цикле до этого условия и -1 -
                    # это на этаж ниже потому что мы уже на нем были
                    self.floorLift = i
                self.listOfVisitedFloors.append(0)
                break

            ''' Люди заходят '''
            if floor in self.callsInLiftToFloor:
                if self.people_in_lift != self.capacity:
                    a = copy.deepcopy(self.callsInLiftToFloor.get(floor))
                    for people_in_floor in a:
                        if self.people_in_lift == self.capacity:
                            break
                        if people_in_floor < floor:
                            self.lift.append(people_in_floor)
                            self.callsInLiftToFloor[floor].remove(people_in_floor)
                            self.people_in_lift += 1
                    if not self.callsInLiftToFloor.get(floor):
                        del self.callsInLiftToFloor[floor]
                visited_floor = True
            ''' Указываем этаж лифта '''
            self.floorLift = floor

            '''  '''
            if visited_floor:
                self.listOfVisitedFloors.append(self.floorLift)
        self.liftUpOrDown = "Up"

    # Словарь с
    # ключ - вызов лифта
    # значение - Этаж куда человек хочет поехать
    def callsInLiftToFloors(self):
        return {i: list(self.queues[i]) for i in range(len(self.queues)) if self.queues[i]}


# lifts = Dinglemouse(((), (), (5, 5, 5), (), (), (), ()), 5)
# lift = Dinglemouse(((), (), (1, 1), (), (), (), ()), 5)
lift = Dinglemouse(((), (6, 5, 2), (4,), (), (0, 0, 0), (), (), (3, 6, 4, 5, 6), (), (1, 10, 2), (1, 4, 3, 2)), 5)
# print("список вызовов этажей", lift.callsFloor())
# print("список посещение этажей", lift.visitingFloors())
# print(lift.callsInLiftToFloors())
print(lift.theLift())
# print(lift.callsInLiftToFloor)
