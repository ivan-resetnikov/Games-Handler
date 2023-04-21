import tkinter as tk
import tkinter.ttk as ttk

from tkinter.constants import *



class VerticalScrolledFrame(ttk.Frame):
	''' 
		FROM: https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame#answer-16198198

		Use the 'interior' attribute to place widgets inside the scrollable frame.
		Supports pack, grid and place methods.
	'''
	def __init__(self, parent, *args, **kw):
		ttk.Frame.__init__(self, parent, *args, **kw)

		vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
		vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
		canvas = tk.Canvas(self,
			bd=0, highlightthickness=0,
			yscrollcommand=vscrollbar.set)

		canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
		vscrollbar.config(command=canvas.yview)

		canvas.xview_moveto(0)
		canvas.yview_moveto(0)

		self.interior = interior = ttk.Frame(canvas)
		interior_id = canvas.create_window(
			0, 0, window=interior, anchor=NW)


	def _configure_interior(event):
		size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
		canvas.config(scrollregion="0 0 %s %s" % size)

		if interior.winfo_reqwidth() != canvas.winfo_width():
			canvas.config(width=interior.winfo_reqwidth())

		interior.bind('<Configure>', _configure_interior)


	def _configure_canvas(event):
		if interior.winfo_reqwidth() != canvas.winfo_width():
			canvas.itemconfigure(interior_id, width=canvas.winfo_width())

		canvas.bind('<Configure>', _configure_canvas)