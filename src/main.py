import core

import tkinter.ttk as ttk
import tkinter as tk



class GamesManager:
	''' 
		GamesManager class that handles window
		and interacts with core, acts as middleman
		between user and application
	''' 
	def __init__(self):
		self.window = tk.Tk()

		self.window.geometry('700x500')
		self.window.title('Games manager / v1.0')


	def initWigets(self) -> None:
		self.games = ttk.LabelFrame(text=' games ')
		self.games.grid(row=0, column=0, padx=10, pady=10)

		self.gamesFrame = core.VerticalScrolledFrame(self.games)
		self.gamesFrame.grid(row=0, column=0)

		ttk.Label(self.gamesFrame.interior, text='They are falling from above!').grid(row=0, column=0, padx=10, pady=10)


	def start(self) -> None:
		self.initWigets()

		self.window.mainloop()



if __name__ == '__main__':
	GamesManager().start()