import tkinter as tk
from itertools import count
from threading import Thread

from playsound import playsound

from PIL import Image, ImageTk

stop = False


class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


def play():
    playsound("hb.mp3")


def Potok():
    global stop
    if not stop:
        Thread(target=play).start()
        stop = True


root = tk.Tk()
root.title("С днем рождения, Настя!")
lbl = ImageLabel(root)
lbl.pack()
lbl.load('b.gif')
play_button = tk.Button(root, text="Нажми :D", font=("Helvetica", 32),
                        relief=tk.GROOVE, command=Potok)
play_button.pack()
root.mainloop()
