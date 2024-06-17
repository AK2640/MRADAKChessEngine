import win32gui # type: ignore
import win32con # type: ignore
import os
import time


from tkinter import *
root = Tk()
w = Label(root, text='MRADAK Engine')
w.pack()
root.mainloop()

def set_window_title(window_title_string, wait_for_change=False):
    os.system("title " + window_title_string)
    if (wait_for_change):
        matched_window = 0
        while (matched_window == 0):
            matched_window = win32gui.FindWindow(None, window_title_string)
            time.sleep(0.025) # To not flood it too much...
    
    return window_title_string

def set_window_icon(window_title, image_path):
    hwnd = win32gui.FindWindow(None, window_title)
    icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
    hicon = win32gui.LoadImage(None, image_path, win32con.IMAGE_ICON, 0, 0, icon_flags)
    
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_SMALL, hicon)
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_BIG, hicon)

def set_title_and_icon(window_title, icon_path):
    """Set the window title, wait for it to apply, then adjust the icon."""
    window_title = set_window_title(window_title, wait_for_change=True)
    set_window_icon(window_title, icon_path)
    return window_title

set_title_and_icon("MRADAK Engine", "C:\Users\mriegert1234\Downloads\ChessAssets\Icon.ico")
