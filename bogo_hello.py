mysterious_numbers=[2535,853,288,2535,154,3767,154,2725,495,2535,855,2568]

from bs4 import BeautifulSoup
from urllib import request
url = "http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html"
sauce = request.urlopen(url).read().decode('utf8')

soup = BeautifulSoup(sauce, 'html.parser')
tasty_gloop = soup.body.text
start_pi = 24
end_pi = 101307
raw_pie = tasty_gloop[start_pi:end_pi]
cooked_pie= "".join(tasty for tasty in raw_pie if tasty not in '\n')

slices_of_pie=[]
for wow in mysterious_numbers:
    slices_of_pie.append(int(cooked_pie[wow:wow+3]))

message=list(map(chr, slices_of_pie))

import random
def bogo_hello(ls):
    random.shuffle(ls)
    return

while message != list("Hello world!"):
   bogo_hello(message)
   print(''.join(message))
