import tkinter as tk
import random


xLoc = 00
yLoc = 00
i = 0
j = 0
b = 0

class Text1:
    def __init__(self, canvas, xLoc, yLoc, word):
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.canvas = canvas
        self.word = word
        self.id = canvas.create_text(xLoc, yLoc, text=word)

    def move_text(self):
        deltax = 10
        deltay = 10
        self.canvas.move(self.id, deltax, deltay)
        self.canvas.after(100, self.move_text)

    def del_text(self):
        global b
        b += 1
        self.canvas.delete(b)


root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

with open("easy_words.txt") as f:
    easy_words = list(map(lambda s: s.strip('\n'), f.readlines()))
    random.shuffle(easy_words)
for k, w in enumerate(easy_words):
    text1 = Text1(canvas, xLoc, yLoc, w)
    xLoc = xLoc-300
    yLoc = yLoc-300
    text1.move_text()


class KeyValidationDemo():
 def __init__(self):
    vcmd = (root.register(self.validate_data), '%S')
    invcmd = (root.register(self.invalid_name), '%S')
    self.entry = tk.Entry(root, validate="key", validatecommand=vcmd, invalidcommand=invcmd)
    self.entry.pack(pady=5, padx=5)
    self.entry.focus_set()
    self.errmsg = tk.Label(root, text= '', fg='red')
    self.errmsg.pack()

 def validate_data(self, S):
     global i, j
     print(S)
     self.errmsg.config(text='')
     if easy_words[i][j] == S and len(easy_words[i]) > j:
         j += 1
         if len(easy_words[i]) == j:
             j = 0
             i += 1
             self.delete()
             self.delete_entry()
             return True
         return True
     else:
         return False

 def invalid_name(self, S):
    self.errmsg.config(text='Invalid characters \n name can only have alphabets')

 def delete(self):
    text1.del_text()

 def delete_entry(self):
     self.entry.delete(0, tk.END)


app = KeyValidationDemo()
root.mainloop()