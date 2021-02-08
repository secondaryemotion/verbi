#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import random
import pandas as pd
from tkinter import *


# In[5]:


window = tk.Tk()
greeting = tk.Label(
    text="Ciao, principessa",
    height = 2)
greeting.pack()

file = pd.read_csv('verbs.csv',header=None)

i = random.randrange(0, 184,1)
verb = file[0][i]
right_answer=file[0].take([1,2,3,4,5,6],axis=1).tolist()
pronouns = [
    'Io',
    'Tu',
    'Lei/Lui',
    'Noi',
    'Voi',
    'Loro'
]


entries = [] 
results = []
i = random.randrange(0, 184,1)
verb = file.iloc[i].tolist()[0]
frame1 = tk.Frame(master = window)
frame1.pack()
verb_name = tk.Label(master = frame1, text = verb)
verb_name.pack()
verbs_form = tk.Frame(relief = tk.SUNKEN, borderwidth = 2)
verbs_form.pack()
for index, name in enumerate(pronouns):
    label = tk.Label(master = verbs_form, text = name)
    entry = tk.Entry(master = verbs_form, width = 15)
    result = tk.Label(master = verbs_form)
    label.grid(row = index, column = 0, sticky = 'e')
    entry.grid(row = index, column = 1)
    result.grid(row = index, column = 2)
    entries.append(entry)
    results.append(result)

def new_verb(event): 
    for entry in entries:
        entry.delete(0, 'end')
    for result in results:
        result['text']= ''
    i = random.randrange(0,184,1)
    verb = file.iloc[i].tolist()[0]
    verb_name['text']=verb
    return verb

def handle_click(event):
    answer = []
    verb = verb_name['text']
    j = file[file[0]==verb].index[0]
    right_answer = file.iloc[j].tolist()[1:7]
    for entry in entries:
        answer.append(entry.get())
    for i in range(len(pronouns)):
        if answer[i] == right_answer[i]:
            results[i]['text']= 'Sì'
        else:
            results[i]['text']= 'No'
       

btn_submit = tk.Button(master = window, text = 'Invia')
btn_submit.pack()
btn_submit.bind("<Button-1>", handle_click)
    
btn_new = tk.Button(master = window, text = 'Nuovo')
btn_new.pack()
btn_new.bind("<Button-1>", new_verb)



window.mainloop()






