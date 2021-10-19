from tkinter import * from tkinter.ttk import *
root = Tk()
  
# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
            length = 100, mode = 'indeterminate')
  
# Function
def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 100
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(0.5)
    progress['value'] = 0
    
    
