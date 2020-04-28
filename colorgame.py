import tkinter, random

colours = ["Red","Yellow","Blue","Green","Grey","Orange", "Purple","Cyan", "Brown","Black","Magenta","White"]

score = 0

timeleft = 60

def startgame(event):
	if timeleft == 60:
		countdown()
	nextColour()

def nextColour():
	global score
	global timeleft

	if timeleft > 0:
		e.focus_set()
		if e.get().lower() == colours[1].lower():
			score += 1

		e.delete(0, tkinter.END)
		random.shuffle(colours)

		label.config(fg = str(colours[1]), text = str(colours[0]))
		scoreLabel.config(text = "Score: " + str(score))

def countdown():
	global timeleft

	if timeleft > 0:
		timeleft -= 1
		timeLabel.config(text = "Time Left: "+ str(timeleft))

		timeLabel.after(1000, countdown)

root = tkinter.Tk()
root.title("Color Game")
root.geometry("350x350")

instructions = tkinter.Label(root, text="Type the colour name not the string name.", font=("Helvetica", 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start game", font=("Helvetica", 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time Left: " + str(timeleft), font = ("Helvetica", 40))

timeLabel.pack()

label = tkinter.Label(root, font=("Helvetica", 60))

label.pack()

e = tkinter.Entry(root)

root.bind("<Return>", startgame)

e.pack()

e.focus_set()

root.mainloop()