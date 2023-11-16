import random, copy, sys
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

    def __setup(self):
        position = (input("Enter number of positions (between 1 and 10) : "))
        num_color = (input("Enter number of colors (between 1 and 8) : "))
        if not position.isdigit() or not num_color.isdigit():
            print("please input NUMBERS.")
            self.__setup()
        elif 1 < int(position) < 10 and 1 < int(num_color) < 8:
            self.__column = int(position)
            self.__color = int(num_color)
            print("positions and colors setted\n")
        else:
            print("please try again with the valid numbers.")
            self.__setup()
        self.menu()

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

    def __play(self):
        temp_lst = [count for count in range(1, self.__color +1)]
        self.__answer = random.choices(temp_lst, k = self.__column)
        print(f"Playing Mastermind with {self.__color} colors and {self.__column} positions")
        guess = input("What is your guess?: ")
        if not guess.isdigit():
            print("please input NUMBERS.")
            self.__play()
        elif len(guess) == self.__column:
            ans_lst = [int(i) for i in guess]
            self.__last_guess = guess
            self.__gen_hint(ans_lst)
            while ans_lst != self.answer:
                guess = input("What is your guess?: ")
                self.__last_guess = guess
                self.__round += 1
                ans_lst = [int(i) for i in guess]
                self.__gen_hint(ans_lst)
            print(f"You solve it after {self.__round} rounds\nReturning to menu\n")
            self.menu()
            
        else:
            print("please enter guess with the correct amount of positions")
            self.__play()

    def menu(self):
        print("\nWelcome to Mastermind! Please pick one of the choices below.\n")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("| Play -- Play Mastermind                                             |")
        print("| Setup -- config the numbers of colors and position (default is 4x4) |")
        print("| Quit -- Quit the game                                               |")
        print("|_____________________________________________________________________|\n")
        choice = input()
        if choice.lower() == "play":
            self.__play()
        elif choice.lower() == "setup":
            self.__setup()
        elif choice.lower() == "quit":
            sys.exit()
        else:
            self.menu()

if __name__ == __name__:
    game = Mastermind()
    game.menu()