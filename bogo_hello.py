from bs4 import BeautifulSoup
import random

def bogo_hello(ls):
    random.shuffle(ls)
    return


string = list("leHlo! owrld")
while string != list("Hello world!"):
    bogo_hello(string)
    print(''.join(string))
