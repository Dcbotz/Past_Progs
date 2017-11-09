"""
Program: Calculator.py
Author: Duncan Sullivan and Daniel Botz
Using GUI design, this simple calculator can add, subtract, multiply and divide.
"""
from Tkinter import *

class Calculator(Frame):
	
	def __init__(self):
		
		Frame.__init__(self)
		self.master.title("Calculator")
		self.grid()
		
		self._dataPane = Frame(self)
		self._dataPane.grid(row = 0, column = 0)
		self._entry = Entry(self._dataPane)
		self._entry.grid(row = 0, column = 0, sticky = E)
		
		# 1st row of buttons
		self._buttonPane = Frame(self)
		self._buttonPane.grid(row = 1, column = 0)
		
		self._buttonAC = Button(self._buttonPane, text = "AC")
		self._buttonAorS = Button(self._buttonPane, text = "+/-")
		self._buttonDiv = Button(self._buttonPane, text = "/")
		self._buttonX = Button(self._buttonPane, text = "X")
		self._buttonAC.grid(row = 0, column = 0)
		self._buttonAorS.grid(row = 0, column = 1)
		self._buttonDiv.grid(row = 0, column = 2)
		self._buttonX.grid(row = 0, column = 3)
		
		# 2nd row of buttons
		self._button1 = Button(self._buttonPane, text = "1")
		self._button2 = Button(self._buttonPane, text = "2")
		self._button3 = Button(self._buttonPane, text = "3")
		self._buttonSub = Button(self._buttonPane, text = "-")
		self._button1.grid(row = 1, column = 0)
		self._button2.grid(row = 1, column = 1)
		self._button3.grid(row = 1, column = 2)
		self._buttonSub.grid(row = 1, column = 3)
		
		# 3rd row of buttons
		self._button4 = Button(self._buttonPane, text = "4")
		self._button5 = Button(self._buttonPane, text = "5")
		self._button6 = Button(self._buttonPane, text = "6")
		self._buttonAdd = Button(self._buttonPane, text = "+")
		self._button4.grid(row = 2, column = 0)
		self._button5.grid(row = 2, column = 1)
		self._button6.grid(row = 2, column = 2)
		self._buttonAdd.grid(row = 2, column = 3)
		
		# 4th row of buttons
		self._button7 = Button(self._buttonPane, text = "7")
		self._button8 = Button(self._buttonPane, text = "8")
		self._button9 = Button(self._buttonPane, text = "9")
		self._button7.grid(row = 3, column = 0)
		self._button8.grid(row = 3, column = 1)
		self._button9.grid(row = 3, column = 2, sticky = W)
		
		# 5th row of buttons
		self._button0 = Button(self._buttonPane, text = "0")
		self._buttonDeci = Button(self._buttonPane, text = ".")
		self._buttonEq = Button(self._buttonPane, text = "=")
		self._button0.grid(row = 4, column = 0)
		self._buttonDeci.grid(row = 4, column = 1)
		self._buttonEq.grid(row = 4, column = 2, columnspan = 2, sticky = W+E)
		
def main():
	Calculator().mainloop()
	
main()
		
