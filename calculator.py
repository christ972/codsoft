import tkinter as tk


class calculator:
    #fen=tk.Tk()
    def __init__(self):
        fen=tk.Tk()
        fen.geometry("800x700")
        fen.resizable(True,True)
        self.create_button(fen)
        fen.mainloop()


    def create_button(self,fen):

        op_plus=tk.Button(fen,text='+')
        op_moins=tk.Button(fen,text='-')
        op_fois=tk.Button(fen,text='x')
        op_div=tk.Button(fen,text='/')
        one=tk.Button(fen,text='1')
        two=tk.Button(fen,text='2')
        three=tk.Button(fen,text='3')
        four=tk.Button(fen,text='4')
        five=tk.Button(fen,text='5')
        six=tk.Button(fen,text='6')
        seven=tk.Button(fen,text='7')
        eight=tk.Button(fen,text='8')
        nine=tk.Button(fen,text='9')
        zero=tk.Button(fen,text='0')
        clear=tk.Button(fen,text='C')
        equal=tk.Button(fen,text='=')
        decimal=tk.Button(fen,text='.')
        history=tk.Button(fen,text='history')
        
        one.grid(row=0,column=0)
        two.grid(row=0,column=1)
        three.grid(row=0,column=2)
        four.grid(row=0,column=3)
        five.grid(row=1,column=0)
        six.grid(row=1,column=1)
        seven.grid(row=1,column=2)
        eight.grid(row=1,column=3)
        nine.grid(row=2,column=0)
        zero.grid(row=2,column=1)
        decimal.grid(row=2,column=2)
        equal.grid(row=2,column=3)
        clear.grid(row=0,column=5)
        history.grid(row=0,column=6)
        op_plus.grid(row=1,column=5)
        op_div.grid(row=2,column=5)
        op_fois.grid(row=3,column=5)
        op_moins.grid(row=4,column=5)

    def display(self,fen):
        fen
calc=calculator()