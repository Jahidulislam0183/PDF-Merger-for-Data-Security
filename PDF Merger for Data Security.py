# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 01:23:37 2023

@author: Harun
"""
import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog
import PyPDF2
import os

class FileListGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("PDF Merger")
        self.grid(sticky=tk.W+tk.E+tk.N+tk.S)
        A= Font(family="Bahnschrift Light SemiCondensed",size=12,weight="bold")

        # label for file list
        self.label1 = tk.Label(self, text=" PDF File List",font=A,  width=25, height=2)
        self.label1.grid(row=0, column=1, sticky=tk.N)

        # listbox for files
        self.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE,font=A,  width=50, height=10)
        self.listbox.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

        # Button for adding files
        self.button1 = tk.Button(self, text='Add Files',cursor="plus",font=A, activeforeground='#58D68D',activebackground='#5D6D7E', command=self.add_files)
        self.button1.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        # Button for moving file up
        self.button2 = tk.Button(self, text='Move Up',cursor="plus",font=A, activeforeground='#58D68D',activebackground='#5D6D7E', command=self.move_up)
        self.button2.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

        # Button for moving file down
        self.button3 = tk.Button(self, text='Move Down',cursor="plus",font=A, activeforeground='#58D68D',activebackground='#5D6D7E', command=self.move_down)
        self.button3.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S)

        # Button for merging files
        self.button4 = tk.Button(self, text='Merge Files',cursor="plus",font=A, activeforeground='#58D68D',activebackground='#5D6D7E', command=self.merge_files)
        self.button4.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S)


        # Button for closing the application
        self.button6 = tk.Button(self, text='Close', cursor="plus",font=A, activeforeground='#58D68D',activebackground='#5D6D7E',command=self.master.destroy)
        self.button6.grid(row=5, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        # Initialize variables
        self.files = []

    def add_files(self):
        files = filedialog.askopenfilenames()
        for file in files:
            self.listbox.insert(tk.END, file)
            self.files.append(file)

    def move_up(self):
        current_selection = self.listbox.curselection()
        if current_selection:
            index = current_selection[0]
            if index > 0:
                text = self.listbox.get(index)
                self.listbox.delete(index)
                self.listbox.insert(index-1, text)
                self.listbox.selection_clear(0, tk.END)
                self.listbox.selection_set(index-1)
                self.files[index], self.files[index-1] = self.files[index-1], self.files[index]

    def move_down(self):
        current_selection = self.listbox.curselection()
        if current_selection:
            index = current_selection[0]
            if index < self.listbox.size()-1:
                text = self.listbox.get(index)
                self.listbox.delete(index)
                self.listbox.insert(index+1, text)
                self.listbox.selection_clear(0, tk.END)
                self.listbox.selection_set(index+1)
                self.files[index], self.files[index+1] = self.files[index+1], self.files[index]

    def merge_files(self):
        merger = PyPDF2.PdfFileMerger()
        for file in self.files:
            merger.append(file)
        self.merged_file = filedialog.asksaveasfilename(defaultextension=".pdf")
        merger.write(self.merged_file)
        merger.close()
        os.startfile(self.merged_file)

root = tk.Tk()
app = FileListGUI(root)
app.mainloop()

