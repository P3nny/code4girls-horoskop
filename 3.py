from flask import Flask
from random import choice
app = Flask(__name__)

@app.route('/')
def hello_world():
    A = ['Es könnte sein, dass ',
    'Sei nicht überrascht, wenn ',
    'Es ist gut möglich, dass ',
    'Die Sterne sagen, dass ']
    B = ['im nächsten Monat ',
    'diese Woche ',
    'am Mittwoch ',
    'im Zoo ',
    'auf dem Heimweg ',
    'durch eine übernatürliche Erscheinung ',
    'heute ']
    C = ['etwas Wunderbares passiert.',
    'ein interessanter Mensch in dein Leben tritt.',
    'eine gute Gelegenheit auf dich wartet.',
    'Kekse auf dich herab regnen.',
    'ein Pappnasenclown dein Herz erobert.',
    'ein Papagei dich Eierkopf nennt.']

    horoskop = choice(A) + choice(B) + choice(C)
    #return('Dein Horoskop')
    return(horoskop)
    print(horoskop)    

if __name__ == '__main__':
    app.run()
