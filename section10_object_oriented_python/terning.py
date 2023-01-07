
# terningspill:
# velge hvor mange sider terningen skal ha
# velge hvor mange terninger du vil rulle

#try:
#    import tkinter
#except ImportError: # python 2
#    import Tkinter as tkinter

#from tkinter import *

#import tkinter as tk

import random

#root = tk.Tk()
#root.geometry("400x400")
#root.title("Role the Dice")




spørsmål1 = input("hvor mange sider skal terningen ha? ")
spørsmål2 = input("Hvor mange terninger vil du rulle? ")

rolled = []
count = [rolled.count(int(spørsmål1))]


#label = tk.Label(root, spørsmål2, spørsmål2, font=("Helvetica", 260))

def terning():
    for terninger in range(0, int(spørsmål2)):
        print(random.randint(1, int(spørsmål1)))

        #label.configure(text=f'')
        #label.pack()
terning()


def probability():
    #for i in range(0, ((int(spørsmål1))+1)):
    percentage = "{:.2f}".format(terning() / (int(spørsmål1) * int(spørsmål2)) * 100)
    percent = str(percentage) + '%'
    print(percent)
        #print(' ', i + 1, ':', percent)




#print("sansynlgiheten er: {}".format(count[int(spørsmål2)]))

probability()


#terning()


#root.mainloop()

#mainWindow.mainloop()



