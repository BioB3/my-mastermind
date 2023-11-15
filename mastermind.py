import random
class Mastermind:
    def __init__(self):
        self.__column = 4
        self.__color = 4
        self.__answer = []
    
    @property
    def column(self):
        return self.__column
    
    @property
    def color(self):
        return self.__color
    
    @property
    def answer(self):
        return self.__answer

    def setup(self):
        position = int(input("Enter number of positions (between 1 and 10) : "))
        num_color = int(input("Enter number of colors (between 1 and 8) : "))
        if 1 < position < 10 and 1 < num_color < 8:
            self.__column = position
            self.__color = num_color
            print("positions and colors setted")
        else:
            print("please try again with the valid numbers.")
            self.setup()
        temp_lst = [count for count in range(1, self.__color +1)]
        self.__answer = random.choices(temp_lst, k = self.__column)
        print(self.__answer)

    def gen_hint(self, ans_lst):
        temp_lst = []
        for ans in ans_lst:
            if ans in self.__answer and ans == self.__answer[ans_lst.index(ans)]:
                temp_lst.append("*")
            elif ans in self.__answer:
                temp_lst.append("o")
            temp_lst.sort()
        print(temp_lst)
        


game = Mastermind()
game.setup()