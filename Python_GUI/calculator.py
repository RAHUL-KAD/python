from tkinter import *

root = Tk()
root.title("Calculator")

entry = Entry(root, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=30,pady=20)

def myCal(number):
	first = entry.get()
	entry.delete(0, END)
	entry.insert(0, str(first) + str(number))

def clear_button():
	entry.delete(0, END)

def add_button():
	first_number = entry.get()
	global f_number
	global math
	math = "addition"
	f_number = int(first_number)
	entry.delete(0,END)

def subtract_button():
	first_number = entry.get()
	global f_number
	global math
	math = "substraction"
	f_number = int(first_number)
	entry.delete(0,END)

def multiply_button():
	first_number = entry.get()
	global f_number
	global math
	math = "multiplication"
	f_number = int(first_number)
	entry.delete(0,END)

def divide_button():
	first_number = entry.get()
	global f_number
	global math
	math = "division"
	f_number = int(first_number)
	entry.delete(0,END)	

def equal_button():
	second_number = entry.get()
	entry.delete(0, END)

	if math == "addition":
		entry.insert(0, f_number + int(second_number))

	if math == "substraction":
		entry.insert(0, f_number - int(second_number))
		
	if math == "multiplication":
		entry.insert(0, f_number * int(second_number))

	if math == "division":
		entry.insert(0, f_number / int(second_number))	


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda:myCal(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:myCal(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:myCal(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:myCal(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:myCal(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:myCal(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:myCal(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:myCal(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:myCal(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:myCal(0))
button_add = Button(root, text="+", padx=39, pady=20, command=add_button)
button_equal = Button(root, text="=", padx=100, pady=20, bg="orange",command=equal_button)
button_clear= Button(root, text="AC", padx=97, pady=20, fg="orange" ,command=clear_button)

button_subtract = Button(root, text="-", padx=40, pady=20, command=subtract_button)
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply_button)
button_divide = Button(root, text="/", padx=40, pady=20, command=divide_button)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4,column=0)
button_multiply.grid(row=4 ,column=1)
button_divide.grid(row=4 ,column=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6 ,column=0)
button_clear.grid(row=6, column=1,columnspan=2)


root.mainloop()	