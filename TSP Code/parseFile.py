from Tkinter import Tk
import os
from tkFileDialog import askopenfilename



class ParseFile:


    def read(self):

        print "\n\nPlease choose 'input1copy.txt'[1] \nOR\nChoose 'input2copy.txt'[2]"
        num = input()

        if num == 1:
            filename = 'input1copy.txt'
        else:
            filename = 'input2copy.txt'


        if not os.path.exists(filename):
            print("File not found. Please choose file: ")
            Tk().withdraw()
            filename = askopenfilename()
            print(filename)



        f = open(filename, "r")
        numTasks = int(f.readline())
        points = []

        for i in range(1, numTasks + 1):
            value = []
            value = f.readline().split()
            results = map(int, value)
            points.append(results)

        f.close()

        return points

