import colorama
from colorama import Fore, Back, Style

colorama.init()

help(colorama)
help(Fore)
help(Back)
help(Style)

print(Fore.RED + "Червоний текст")
print(Fore.GREEN + "Зелений текст")
print(Back.BLUE + "Синій фон")
print(Style.BRIGHT + "Яскравий текст")

print(Style.RESET_ALL + "Звичайний текст")
    