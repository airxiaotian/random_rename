import os
import random


def get_random_name():
    randomFileName = ''
    for i in range(16):
        if i == 0:
            randomFileName = randomFileName + str(random.randint(1, 9))
        randomFileName = randomFileName + str(random.randint(0, 9))
    return randomFileName


files = os.listdir(os.getcwd() + '/files')

for file in files:
    randomFileName = get_random_name()
    if os.path.exists(randomFileName) == False:
        os.rename(os.getcwd() + '/files/'+file, os.getcwd() +
                  '/files/'+randomFileName + '.mp3')
