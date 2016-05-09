#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import csv
from time import sleep

data = []

with open('russianwords.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = '@',quotechar='|')
    for row in spamreader:
        global data
        data.append(row)

def str_to_num(argument):
    switcher = {
        "RA": 0,
        "EN": 1,
        "RS": 2,
    }
    return switcher.get(argument, "nothing")

response0 = raw_input("Russian Alphabet (RA), English (EN), Russian Sentence (RS): ")
#response1 = raw_input("Enter input: ")
wordtype = str_to_num(response0)

root = Tk()

fram = Frame(root)
Label(fram,text='Text to find:').pack(side=LEFT)
edit = Entry(fram)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(fram, text='Find')
butt.pack(side=RIGHT)
fram.pack(side=TOP)

text = Text(root)
text.insert('1.0','''Search text 
                   Here
                  ''')
text.pack(side=BOTTOM)

# scrollb = tki.Scrollbar(fram, command=fram.text.yview)
# scrollb.grid(row=0, column=1, sticky='nsew')
# fram.text['yscrollcommand'] = scrollb.set



def find():
    global wordtype
    global response0
    text.delete('1.0', END)
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    if s:
        idx = '1.0'
        wordcontainer = []
        global data
        for word in data:
            if s in word[wordtype]:
                wordcontainer.append(word)
        for word in wordcontainer:
            print word[wordtype][:-1]
            print word[wordtype][1:-1]
            print word[wordtype][1:]
            lastidx = '%s+%dc' % (idx, len(s))
            text.insert(idx, word[wordtype][:-1]+'\n')
        text.tag_config('found', foreground='red')
    edit.focus_set()
butt.config(command=find)
root.mainloop()