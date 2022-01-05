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
        self.visited_floor = False  # Флажок для посещенного этажа

    def theLift(self):
        while self.callsInLiftToFloor:
            if self.liftUpOrDown == "Up":
                print(" ", colored('____' + self.liftUpOrDown + '____', 'cyan', attrs=['reverse', 'blink']))
                self.liftGoesUp()
            elif self.liftUpOrDown == "Down":
                print(" ", colored('____' + self.liftUpOrDown + '____', 'cyan', attrs=['reverse', 'blink']))
                self.liftGoesDown()
        ''' Возвращаем список посещенных этажей '''
        b = copy.deepcopy(self.listOfVisitedFloors)
        count = 0
        for i in range(len(self.listOfVisitedFloors) - 1):
            if self.listOfVisitedFloors[i] == self.listOfVisitedFloors[i + 1]:
                del b[i - count]
                count += 1
        self.listOfVisitedFloors = b
        try:
            if self.listOfVisitedFloors[0] != 0:
                self.listOfVisitedFloors.insert(0, 0)
        except:
            if not self.listOfVisitedFloors:
                return [0]
        return self.listOfVisitedFloors

    def liftGoesUp(self):
        for floor in range(self.floorLift, len(self.queues)):
            self.visited_floor = False
            if self.people_in_lift == 0 and max(self.callsInLiftToFloor) < floor:
                """ Лифт поедит вниз """
                self.liftUpOrDown = "Down"  # Флаг
                self.floorLift = floor - 1  # Этаж на котором остановился лифт
                break
            cprint("--- " + str(floor) + " Этаж ---", 'red')

            ''' Люди выходят '''
            self.outputPeople(floor)

            ''' Проверка на вызовы '''
            if not self.callsInLiftToFloor and self.people_in_lift == 0:
                self.CheckingForCalls(floor)
                break

            ''' Люди заходят '''
            self.inputPeople(floor)

            ''' Указываем этаж лифта '''
            self.floorLift = floor

            '''  '''
            if self.visited_floor:
                cprint("Visited", 'yellow')
                self.listOfVisitedFloors.append(self.floorLift)
        self.liftUpOrDown = "Down"

    def liftGoesDown(self):
        for floor in range(self.floorLift, -1, -1):
            self.visited_floor = False
            if self.people_in_lift == 0 and min(self.callsInLiftToFloor) > floor:
                """ Лифт поедит вверх """
                self.liftUpOrDown = "Up"  # Флаг
                self.floorLift = floor + 1  # Этаж на котором остановился лифт
                break
            cprint("--- " + str(floor) + " Этаж ---", 'red')

            ''' Люди выходят '''
            self.outputPeople(floor)

            ''' Проверка на вызовы '''
            if not self.callsInLiftToFloor and self.people_in_lift == 0:
                self.CheckingForCalls(floor)
                break

            ''' Люди заходят '''
            self.inputPeople(floor)

            ''' Указываем этаж лифта '''
            self.floorLift = floor

            '''  '''
            if self.visited_floor:
                cprint("Visited", 'yellow')
                self.listOfVisitedFloors.append(self.floorLift)
        self.liftUpOrDown = "Up"

    # Люди выходят
    def outputPeople(self, floor):
        if floor in self.lift:
            cprint("Выходят : ", 'blue')
            print(self.lift, end=" -> ")
            while floor in self.lift:
                self.lift.remove(floor)
                self.people_in_lift -= 1
            print(self.lift)
            self.visited_floor = True

    # Люди заходят
    def inputPeople(self, floor):
        if floor in self.callsInLiftToFloor:
            if self.people_in_lift != self.capacity:
                cprint("Заходят : ", 'green')
                print("Люди на этаже", self.callsInLiftToFloor.get(floor), end=" -> ")
                for people_in_floor in copy.deepcopy(self.callsInLiftToFloor.get(floor)):
                    if self.people_in_lift == self.capacity:
                        break
                    if (people_in_floor > floor and self.liftUpOrDown == "Up") or (
                            people_in_floor < floor and self.liftUpOrDown == "Down"):
                        self.lift.append(people_in_floor)
                        self.callsInLiftToFloor[floor].remove(people_in_floor)
                        self.people_in_lift += 1
                        self.visited_floor = True
                print(self.callsInLiftToFloor.get(floor))
                if not self.callsInLiftToFloor.get(floor):
                    del self.callsInLiftToFloor[floor]
                print("Лифт - " + str(self.lift))

    # Проверка на вызовы
    def CheckingForCalls(self, floor):
        self.floorLift = floor
        if self.visited_floor:
            cprint("Visited", 'yellow')
            self.listOfVisitedFloors.append(self.floorLift)
        cprint(" ----------- ----------- ----------- ----------- -----------", 'grey')
        for i in range(self.floorLift - 1, -1, -1):  # -1 - это нету счетчика в цикле до этого условия и -1 -
            # это на этаж ниже потому что мы уже на нем были
            cprint("--- " + str(i) + " Этаж ---", 'red')
            self.floorLift = i
        self.listOfVisitedFloors.append(0)
        print(self.listOfVisitedFloors)

    # список вызовов этажей
    def callsFloor(self):
        return [i for i in range(len(self.queues)) if self.queues[i]]

    # список посещение этажей
    def visitingFloors(self):
        set_ = set()
        for i in [i for i in range(len(self.queues)) if self.queues[i]]:
            set_.add(i)
            for j in self.queues[i]:
                set_.add(j)
        return set_

    # Словарь с
    # ключ - вызов лифта
    # значение - Этаж куда человек хочет поехать
    def callsInLiftToFloors(self):
        return {i: list(reversed(self.queues[i])) for i in range(len(self.queues)) if self.queues[i]}


class Dayn():
    pass


# lifts = Dinglemouse(((), (), (5, 5, 5), (), (), (), ()), 5)
# lift = Dinglemouse(((), (), (1, 1), (), (), (), ()), 5)
lift = Dinglemouse(((1, 2, 3, 4, 5,), (3, 5, 6,), (0, 8, 7, 6,), (7, 8,), (0,), (7, 8, 3, 2), (2, 2, 2, 2),
                    (5, 8), (9, 9, 9, 9, 2, 0), (2,)), 4)
# lift = Dinglemouse(((), (6, 5, 2), (4,), (), (0, 0, 0), (), (), (3, 6, 4, 5, 6), (), (1, 10, 2), (1, 4, 3, 2)), 5)
# print("список вызовов этажей", lift.callsFloor())
# print("список посещение этажей", lift.visitingFloors())
print(lift.callsInLiftToFloors())
# print(lift.liftGoesUp())
print(lift.theLift())
print(lift.callsInLiftToFloor)
