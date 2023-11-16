import random, copy
class Mastermind:
    def __init__(self):
        self.__column = 4
        self.__color = 4
        self.__answer = []
        self.__last_guess = ""
        self.__round = 1
    
    @property
    def column(self):
        return self.__column
    
    @property
    def color(self):
        return self.__color
    
    @property
    def answer(self):
        return self.__answer

    @property
    def last_guess(self):
        return self.__last_guess

    def setup(self):
        position = int(input("Enter number of positions (between 1 and 10) : "))
        num_color = int(input("Enter number of colors (between 1 and 8) : "))
        if 1 < position < 10 and 1 < num_color < 8:
            self.__column = position
            self.__color = num_color
            print("positions and colors setted")
            temp_lst = [count for count in range(1, self.__color +1)]
            self.__answer = random.choices(temp_lst, k = self.__column)
        else:
            print("please try again with the valid numbers.")
            self.setup()

    def __gen_hint(self, ans_lst):
        hint_lst = []
        _lst = copy.deepcopy(self.__answer)
        _lst2 = copy.deepcopy(ans_lst)
        for n in range(len(ans_lst)):
            if ans_lst[n] == self.__answer[n]:
                hint_lst.append("*")
                _lst.remove(self.__answer[n])
                _lst2.remove(self.__answer[n])
        for m in _lst2:
            if m in _lst:
                hint_lst.append("o")
        hint_lst.sort()
        print(f"Your guess is {self.__last_guess}")
        print("".join(hint_lst))
        print()

    def play(self):
        guess = input("What is your guess?: ")
        if len(guess) == self.__column:
            ans_lst = [int(i) for i in guess]
            self.__last_guess = guess
            self.__gen_hint(ans_lst)
            while ans_lst != self.answer:
                guess = input("What is your guess?: ")
                self.__last_guess = guess
                self.__round += 1
                ans_lst = [int(i) for i in guess]
                self.__gen_hint(ans_lst)
            print(f"You solve it after {self.__round} rounds")
        else:
            print("please enter guess with the correct amount of positions")
            self.play()


game = Mastermind()
game.setup()
game.play()