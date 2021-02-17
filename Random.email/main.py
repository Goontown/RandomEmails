import random
from random import randint
import csv


def forname():
    with open("firstnames.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        name = (random.choice(words))
        return name



def lastname():
    with open("lastnames.csv", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        name = (random.choice(words))
        return name



def numbers():
        value = (random.randint(10,999))
        return value

def generator(forname,lastname,numbers):
    adress = (f"{forname}{lastname}{numbers}@gmail.com\n")
    print(adress)
    file = open('randomemails', 'a')
    file.write(adress)
    file.close()


def main ():
 for i in range (30):
  fn = forname()
  ln = lastname()
  nu = numbers()
  generator(fn, ln, nu)
if __name__ == "__main__":
    main()




