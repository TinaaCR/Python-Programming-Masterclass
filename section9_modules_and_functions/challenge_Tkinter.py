import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('340x340-8-200')
mainWindow['padx'] = 6

mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=1, sticky='sw')

# Buttons
c_Button = tkinter.Button(mainWindow, text='C')
ce_Button = tkinter.Button(mainWindow, text='CE')
c_Button.grid(row=0, column=2, sticky='es')
ce_Button.grid(row=0, column=3, sticky='sw')

# More buttons
for i in range(0,10):
    x_button = tkinter.Button(mainWindow, text='{}'.format(i))
    x_button.grid()

# even more buttons
pluss_Button = tkinter.Button(mainWindow, text='+')
minus_Button = tkinter.Button(mainWindow, text='-')
pluss_Button.grid(row=1, column=2, sticky='se')
minus_Button.grid(row=1, column=3, sticky='ws')
gange_Button = tkinter.Button(mainWindow, text='*')
deltpa_Button = tkinter.Button(mainWindow, text='/')
gange_Button.grid(row=2, column=2, sticky='se')
deltpa_Button.grid(row=2, column=3, sticky='ws')
erlik_Button = tkinter.Button(mainWindow, text='=')
erlik_Button.grid(row=3, column=2, sticky='se')


mainWindow.mainloop()