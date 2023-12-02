while True:
    guess = (input(("Введите число: ")))
    if (isinstance(guess, str)):
        print(f"{guess} is str")
    else:
        print(f"{guess} is not str")
    if (isinstance(guess, int)):
        print(f"{guess} is int")
    else:
        print(f"{guess} is not int")
    if guess.isdigit():
        guess = int(guess)
        print(type(guess))
        print(guess)
        print("Ok")
        break
    else:
        print("Вы ввели не цифры")
