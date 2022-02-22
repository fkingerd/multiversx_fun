import tkinter as tk
import datetime


master = tk.Tk()
today = str(datetime.datetime.now().strftime("%d%m%Y"))[:11]


def palindrome_day():
    if today == today[::-1]:
        tk.Label(master, text="Today 22nd of February 2022 is a palindrome day!").grid(row=2, column=1)
    else:
        tk.Label(master, text="Today is not a good day for science!").grid(row=2, column=1)


btn = tk.Button(master, text='Get message', command=palindrome_day)
btn.grid(row=3, column=1, sticky=tk.W, pady=4)

master.mainloop()