from tkinter import *
from tkinter.ttk import *

root = Tk()

progress = Progressbar(root, orient = HORIZONTAL,
			length = 100, mode = 'determinate')
