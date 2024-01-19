#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Jan 20, 2024 01:30:21 AM JST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import test_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x443+359+180")
        top.minsize(120, 1)
        top.maxsize(1444, 941)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.55, rely=0.361, height=26, width=47)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=test_support.put_bottun1)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Button''')

        self.Spinbox1 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.283, rely=0.361, relheight=0.043
                , relwidth=0.225)
        self.Spinbox1.configure(activebackground="#d9d9d9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(command=test_support.put_spin1)
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(foreground="#000000")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="#000000")
        self.Spinbox1.configure(insertbackground="#000000")
        self.Spinbox1.configure(selectbackground="#d9d9d9")
        self.Spinbox1.configure(selectforeground="black")
        self.value_list = ['aaa','bbb','ccc','ddd',]
        self.Spinbox1.configure(values=self.value_list)

def start_up():
    test_support.main()

if __name__ == '__main__':
    test_support.main()



