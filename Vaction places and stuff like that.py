#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 19:50:24 2022

@author: priyankadas
"""

from tkinter import *
import random

root = Tk()

root.title("Your Next Vacation Places")
root.geometry("500x500")

get_friend = Entry(root)
get_friend1 = Entry(root)
label1 = Label(root)
label2 = Label(root)
label3 = Label(root)
label4 = Label(root)

list1 = []
list2 = []

def add_friend():
    new_friend = get_friend.get()
    new_friend1 = get_friend1.get()
    list1.append(new_friend)
    list2.append(new_friend1)
    label1["text"] = "Country Name = " + str(list1)
    label4["text"] = "City Name = " + str(list2)
    
def random_friend():
    length = len(list1)
    n = random.randint(0, length-1)
    length1 = len(list2)
    r = random.randint(0, length1-1)
    label3["text"] = "Random Country : " + list1[n]
    label2["text"] = "Random City : " + list2[n]
    
btn = Button(root, text = "Display City and Country Name", command = add_friend)
btn1 = Button(root, text = "Grab random city and country", command = random_friend)
label1.place(relx = 0.5, rely = 0.2, anchor = CENTER)
label2.place(relx = 0.5, rely = 0.8, anchor = CENTER)
label3.place(relx = 0.5, rely = 0.7, anchor = CENTER)
label4.place(relx = 0.5, rely = 0.3, anchor = CENTER)
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)
btn1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
get_friend.pack()
get_friend1.pack()

root.mainloop()


#first label with tell which country to go first, then the second label will tell you which country to go next.