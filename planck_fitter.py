import tkinter
import os
import numpy as np
import matplotlib.pyplot as plt

# Copyright 2018 Błażej Twardy

def planck(box):
    try:
        t = int(box.get())
        if t > 0:
            nazwa = str(t)
            wav = np.arange(1000, 10000, 5)
            h = 6.626e-34
            c = 3.0e+8
            k = 1.38e-23
            a = 2.0 * h * c ** 2
            v = 2.8977685e-3  # stała Wiena
            wave1 = (v / t) * 10 ** 10
            b1 = h * c / (wave1 * (10 ** -10) * k * t)
            y1 = a / (((wave1 * 10 ** -10) ** 5) * (np.exp(b1) - 1.0))
            b = h * c / (wav * (10 ** -10) * k * t)
            y = (a / (((wav * 10 ** -10) ** 5) * (np.exp(b) - 1.0))) / y1
            plt.figure(1)
            plt.xlabel('$\lambda$' + '[$\AA$]')
            plt.ylabel('$I_\lambda$ / $I_m$ ')
            plt.plot(wav, y, label='Planck function for temp. ' + nazwa + 'K')
            plt.legend()
            return plt.show()
        else:
            tkinter.messagebox.showerror('Error', 'Value Error')
    except ValueError:
        tkinter.messagebox.showerror('Error', 'Value Error')

    

def click(box):
    try:
        entry_box = box.get()
        data = np.genfromtxt(entry_box)
        data_wave = np.genfromtxt('temp')
        y2 = data
        x = data_wave
        y3 = max(y2)
        y4 = y2 / y3
        plt.figure(1)
        plt.plot(x, y4, label=entry_box)
        plt.title(entry_box)
        plt.legend()
        return plt.show()
    except OSError:
        tkinter.messagebox.showerror('Error', 'File Error')

def refresh():
    plt.clf()
    plt.draw()


def opener(box, b='dat'):
    path = os.getcwd()
    a = tkinter.filedialog.askopenfilename(initialdir=path, title="Select file",
                                   filetypes=((str(b) + " files", "*." + str(b)), ("all files", "*.*")))
    box.delete(0, tkinter.END)
    box.insert(0, str(a))
    return a


def ten_buton(a):
    if a == 1:
        tkinter.messagebox.showinfo('Author', ' Author: Błażej Twardy \n')
    else:
        tkinter.messagebox.showerror('Error', 'Not Working')


def plus_dych(box, a=0):
    ent = int(box.get())
    ent = ent + a
    box.delete(0, tkinter.END)
    box.insert(0, str(ent))


def trigger_1_2(box, b=0):
    plus_dych(box, a=b)
    planck(box)

def mark_H():
    v = var.get()
    if v == 1:
        plt.text(6563, -0.02,"H_alpha", bbox=dict(fc='none'))
        plt.text(4891, -0.02, "H_beta", bbox=dict(fc='none'))
        plt.text(4340, -0.02, "H_gamma", bbox=dict(fc='none'))
        plt.text(3900, -0.02, "H_delta", bbox=dict(fc='none'))
        plt.arrow(6563, 0.01, 0, 0.5, head_width=80, head_length=0.1, length_includes_head=True)
        plt.arrow(4861, 0.01, 0, 0.68, head_width=80, head_length=0.1, length_includes_head=True)
        plt.arrow(4300, 0.01, 0, 0.59, head_width=80, head_length=0.1, length_includes_head=True)
        plt.arrow(4102, 0.01, 0, 0.77, head_width=80, head_length=0.1, length_includes_head=True)
        plt.draw()

def close_window():
    plt.close()
    window.destroy()
    exit()


window = tkinter.Tk()
window.title('Planck Fitter 3000')
window.geometry('510x300')

var = tkinter.IntVar()

B = tkinter.Button(window, text="About", command=lambda: ten_buton(1))
B.grid()

l1 = tkinter.Label(window, text="File name: ")
l1.grid(row=1, column=0)

textentry = tkinter.Entry(window, width=20)
textentry.grid(row=1, column=1)

open_button = tkinter.Button(window, text='Search', command=lambda: opener(textentry, b='txt'))
open_button.grid(row=1, column=2)

B1 = tkinter.Button(window, text='Apply', command=lambda: click(textentry))
B1.grid(row=2, column=1)

l2 = tkinter.Label(window, text="Enter temperature [K]: ")
l2.grid(row=3, column=0)

textentry2 = tkinter.Entry(window, width=20)
textentry2.grid(row=3, column=1)

B2 = tkinter.Button(window, text='Apply', command=lambda: planck(textentry2))
B2.grid(row=4, column=1)

T2 = tkinter.Button(window, text='-100', command=lambda: trigger_1_2(textentry2, b=-100))
T2.grid(row=3, column=2)

T3 = tkinter.Button(window, text='+100', command=lambda: trigger_1_2(textentry2, b=100))
T3.grid(row=3, column=3)

l2 = tkinter.Label(window, text="Click to exit:")
l2.grid(row=5, column=0)

B3 = tkinter.Button(window, text='EXIT', bg='red', command=lambda: close_window())
B3.grid(row=6, column=0)

B4 = tkinter.Button(window, text='Remove plots', bg='lime', command=lambda: refresh())
B4.grid(row=6, column=3)

C = tkinter.Checkbutton(window, text='Markers for H (works in star6)', variable=var, onvalue=1, offvalue=0 , command=lambda: mark_H())
C.grid(row=6, column=1)


window.mainloop()
