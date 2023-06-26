import tkinter 



button_frame = tkinter.Frame()
button_frame.pack()

reset_button = tkinter.Button(button_frame, text='Reset')
run_button = tkinter.Button(button_frame, text='Run')
x_button = tkinter.Button(button_frame, text='X')

##button_frame.columnconfigure(0, weight=1)
##button_frame.columnconfigure(1, weight=1)
##button_frame.columnconfigure(1, weight=1)

reset_button.grid(row=0, column=0)
run_button.grid(row=0, column=1)
x_button.grid(row=0, column=3)
