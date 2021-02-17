try:
    a = int(input())
except ValueError:
    print("Вы ввели не число")
else:
    print(f"Вы ввели {a}")
finally:
    print("Выход из программы")