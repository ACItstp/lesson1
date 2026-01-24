import colorama
from colorama import Fore, Back, Style

# Ініціалізація colorama (обовʼязково для Windows)
colorama.init()

# Інтроспекція бібліотеки
print("Атрибути модуля colorama:")
print(dir(colorama))

print("\nАтрибути Fore:")
print(dir(Fore))

print("\nАтрибути Back:")
print(dir(Back))

print("\nАтрибути Style:")
print(dir(Style))

# Демонстрація роботи основних атрибутів
print(Fore.RED + "Червоний текст")
print(Fore.GREEN + "Зелений текст")
print(Back.YELLOW + "Жовтий фон")
print(Style.BRIGHT + "Яскравий текст")

# Скидання стилів
print(Style.RESET_ALL + "Звичайний текст")
