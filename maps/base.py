from os import system

system("cls")

file = open("0-0.txt", "r")
for line in file.readlines():
    print(line, end='')

system("PAUSE")
