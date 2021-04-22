import tkinter as tk

def set_message():
    text = text_input.get()
    title_label.configure(text=text)
window = tk.Tk()
window.title('Mhee')
window.minsize(height=400, width=400)

title_label = tk.Label(master=window, text='wtf')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

submit_button = tk.Button(master=window, text='submit', command=set_message)
submit_button.pack()

window.mainloop()