anynum = int(input("Введите число: "))
bordnum = int(input("Введите пограничное число: "))
if anynum < bordnum:
    print("Введенное число меньше пограничного")
if anynum > bordnum:
    print("Введенное число больше пограничного")
if anynum > bordnum * 3:
    print("Введенное число более, чем в три раза больше пограничного")
