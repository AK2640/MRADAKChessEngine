import tkinter as tk
def SubmitCom():
    global eloText
    elo = eloText.get("1.0", "end-1c")
    for widget in root.winfo_children():
        widget.destroy()

root = tk.Tk()
w = tk.Label(root, text='MRADAK Engine')
w.pack(pady=20)

eloHelp = tk.Label(root, text='Enter Elo:')
eloHelp.pack()

eloText = tk.Text(root, height=1, width=8)
eloText.pack(pady=10)

colourHelp = tk.Label(root, text='Select colour:')
colourHelp.pack()

OPTIONSBW = ["White", "Black"]
selectedOptionBW = tk.StringVar(root)
selectedOptionBW.set(OPTIONSBW[0])
dropdownMenuBW = tk.OptionMenu(root, selectedOptionBW, *OPTIONSBW)
dropdownMenuBW.pack(pady=10)

diffHelp = tk.Label(root, text='Select difficulty')
diffHelp.pack()

OPTIONSDIFF = ["Easy", "Medium", "Hard", "Nightmare"]
selectedOptionDIFF = tk.StringVar(root)
selectedOptionDIFF.set(OPTIONSDIFF[0])
dropdownMenuDIFF = tk.OptionMenu(root, selectedOptionDIFF, *OPTIONSDIFF)
dropdownMenuDIFF.pack(pady=10)

submitButton = tk.Button(root, text='Submit', command=SubmitCom)
submitButton.pack()

root.mainloop()

