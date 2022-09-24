'''Number to words ::
 Create a python function that takes an integer number and
 print the number in words
'''
# Using num2words Libarary
from colorama import Fore
import requests
import shutil
from num2words import num2words
import pyautogui
import datetime
from collections import Counter
from PIL import Image
import time
from pynput.keyboard import Key, Listener
from datetime import date


def NumberToWord():
    userInput = input('Choose Any number : ')
    if userInput.isdigit():
        result = num2words(userInput, to='ordinal')
        return result
    else:
        result = print('Please type number not word')
        return result


''' Google Image Downloader :
create a python function that takes a url of an
image from google and save location , then download the image in the save
location
'''

# using import requests & import shutil to download image by url


def ImageDownloader():
    url = input('Paste the link of your image to download it : ')
    file_name = input('Save image as : ')
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ', file_name)
    else:
        print('Image Couldn\'t be retrieved')


'''Print colored text :
 create a python function that takes a text from the user and
print the text in colors
'''
# using colorama


def coloredText():
    userInput = input('type a sentience to Change the color to red :')
    print(Fore.RED + userInput)


'''  BMI calculator :
 create a python function that takes the user height , weight and
print the user BMI and if the user underweight , overweight or healthy
'''


def BmiCalc():

    height = float(input('Enter your height : '))
    weight = float(input('Enter your weight : '))
    bmi = (weight / height / height)*10000
    bmiList = [(16, 'severely underweight'),
               (18.5, 'underweight'),
               (25, 'normal'), (30, 'overweight'),
               (35, 'moderately obese'),
               (float('inf'), 'severely obese')]
    for number, text in bmiList:
        if bmi <= number:
            print('Your BMI is', round(bmi, 1), 'and the person is :', text)
            break


''' Screenshot taker :
 Create a python script that take a desktop screenshot every
minute , and save them in a new folder on the desktop
'''


def ScreenshotTaker():
    userInput = input(
        'press enter if you want take screenshot ok or no to exit : ')
    if userInput == 'ok':
        image = pyautogui.screenshot()
        image.save('ScreenShot.jpg')
        print('Screenshot Done Succesfully')
    else:
        print('no Screenshot back re-launch if you want to take screenshot ')


'''
Birthday Calculator :
create a python function that takes a user birthdate and
print how many days left to the birthday
'''


def birthdaycalc():

    userBirthYear = int(input('Enter your Birth Year : '))
    userBirthMonth = int(input('Enter your Birth Month : '))
    userBirthDay = int(input('Enter your Birth Day : '))
    today = datetime.date.today()
    user_birthday = datetime.date(today.year, userBirthMonth, userBirthDay)
    if user_birthday == today:
        print('Happy Birthday')
    else:
        if user_birthday < today:
            user_birthday = user_birthday.replace(year=today.year+1)
            daysUntilBirthday = user_birthday - today
            print(daysUntilBirthday)
        else:
            daysUntilBirthday = user_birthday-today
            print(daysUntilBirthday)


def AgeCalc():
    userBirthYear = int(input('Enter your Birth Year : '))
    userBirthMonth = int(input('Enter your Birth Month : '))
    userBirthDay = int(input('Enter your Birth Day : '))
    today = datetime.date.today()
    age = today.year - userBirthYear - \
        ((today.month - today.day) < (userBirthMonth - userBirthDay))
    print(age)


'''
Count the frequency of each unique element in a string :
create a python
function that takes a string and prints how many time each unique word exists in
the sentence
'''


def stringCounter():
    userInput = input('type a sentence To fix it and count words in it  : ')
    counts = dict()
    words = userInput.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print(counts)


'''Image resizer : create a python function that takes an image path , the the
needed image size then resize the image to this size and save it in the same folder
'''


def ImageResizer():
    myimage = Image.open(
        r'C:\\Users\\Gaming\Desktop\\Python Tasks\\ScreenShot.jpg')

    resizeImage = myimage.resize((400, 400))
    resizeImage.save('ImageAfterResize.jpg')
    print('Image before Edit Size : ', myimage.size)
    print('Image After Edit Size : ', resizeImage.size)
    resizeImage.show()


'''Days Calculator :
 create a python function that takes 2 dates and prints how
many days between the 2 dates'''


def DaysCalc():
    '''
    StartDate = (input('Please type the Start day YYYY/MM/DD : ')
    EndDate = date(input('Please Type The End day YYYY/MM/DD : ')
'''
    print('Insert The Start Date : ')
    yearStart = int(input('Year : '))
    monthStart = int(input('Month : '))
    dayStart = int(input('Day : '))
    print('Insert The End Date ')
    yearEnd = int(input('Year : '))
    monthEnd = int(input('Month : '))
    dayEnd = int(input('Day : '))
    StartDate = date(yearStart, monthStart, dayStart)
    EndDate = date(yearEnd, monthEnd, dayEnd)
    result = EndDate - StartDate
    print(result.days, ' Days')



