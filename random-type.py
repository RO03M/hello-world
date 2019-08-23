import datetime
import difflib
import string
from random import randint, choice
from time import sleep


alphabet_list = string.ascii_letters


def phrase(total):
    what_to_type = []
    for c in range(0, total):
        if choice([True]):
            what_to_type.append(alphabet_list[randint(0, len(alphabet_list) - 1)])
        else:
            what_to_type.append("{}".format(randint(0, 9)))
    what_to_type = "".join(what_to_type)
    return what_to_type


letters = int(input("Type the amount of letters that you want to type: "))
phrase = phrase(letters)
print("Preparing your phrase")
sleep(2)
print("Get ready!")
for time in range(3, 0, -1):
    sleep(1)
    print(time)
print("READY")
lastTime = datetime.datetime.now().timestamp()
print(phrase)
user_phrase = str(input("Type it: "))
now = datetime.datetime.now().timestamp()
total_time = now - lastTime
precision = round(difflib.SequenceMatcher(None, user_phrase, phrase).ratio(), 2)
print("Precision: {}%\nTime to type: {:.2f} seconds".format(precision * 100, total_time))
