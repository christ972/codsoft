from string import ascii_letters,digits,punctuation
import tkinter as tk
import random
a=''
def generator(screen):
    a=random.choices(digits + ascii_letters +punctuation,k=10)
    screen.delete(0,tk.END)  
    screen.insert(0,a)
    

def display(fen):
    screen=tk.Entry(fen,border=2)
    screen.grid(row=0,column=0,columnspan=6)
    screen.pack(expand=True)
    return screen

def interface(fen,screen):
     fen.geometry("600x400") 
     button=tk.Button(fen,text="Generator",command=lambda:generator(screen))
     button.pack(expand=True)

if __name__=="__main__":
   fen = tk.Tk()
   fen.resizable(False,False)
   interface(fen,display(fen))
   fen.mainloop()