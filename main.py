class dog:
    def __init__(self,name):
        self.name=name
        self.gladness=100
        self.progress=0
        self.alive=True

    def to_walking(self):
        print("time to walking")
        self.progress+=5
        self.progress+=15
    def to_sleep(self):
        print("time to sleep")
        self.progress+=0.5
        self.gladness-=0.5
    def to_chill(self):
        print("time to playing with host")
        self.progress+=1
        self.gladness+=20
    def to_training(self):
        print("time to training with host")
        self.progress+=20
        self.gladness+=10
    def is_alive(self):
        if self.progress<=5:
            print("You were kicked out of the house because you are a weak dog")
            self.alive=False
        elif self.gladness>=0:
            print("The host does not need you")
            self.alive=False
        elif self.progress>10:
            print("It is necessary to try harder")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")

    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")