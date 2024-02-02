import random

class Student:
    def __init__(self, name):
        self.name = name
        self.cleverness = 0
        self.gladness = 50
        self.money = 100
        self.hunger = 10
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.cleverness += 5
        self.gladness -= 10
        self.hunger -= 10

    def to_chill(self):
        print("Time to chill!")
        self.gladness += 50
        self.cleverness -= 1
        self.money -= 15
        self.hunger += 30

    def to_sleep(self):
        print("Time to sleep!")
        self.cleverness += 50
        self.hunger -=10

    def to_work(self):
        print("Time to sleep!")
        self.gladness -= 10
        self.money += 50
        self.hunger -= 10
    def to_lunch(self):
        print("Time to sleep!")
        self.gladness -= 20
        self.money -= 200
        self.hunger += 100

    def is_alive(self):
        if self.cleverness < -1:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.cleverness > 5:
            print("Passed externally...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness: {self.gladness}")
        print(f"Cleverness: {self.cleverness}")
        print(f"Money: {self.money}")
        print(f"Hunger: {self.hunger}")
    def live(self, day):
        d = f"Day {day} of {self.name}'s life"
        print(f"{d:=^50}")
        live_cube = random.randint(1,5)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        elif live_cube == 4:
            self.to_lunch()
        self.end_of_day()
        self.is_alive()

nick = Student("Nick")
for day in range(1, 366):
    nick.live(day)