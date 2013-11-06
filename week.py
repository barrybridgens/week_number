# Display the ISO week number

from Tkinter import *
import tkFont
import datetime

def iso_week():
	return(str(datetime.date.isocalendar(datetime.date.today())[1]))

class Application(Frame):

    def createWidgets(self):

        self.isoweek = Label(self)
        s = "cw" + iso_week()
        self.isoweek["text"] = s,
        self.isoweek["font"] = tkFont.Font(family='Helvetica', size=36, weight='bold')

        self.isoweek.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()