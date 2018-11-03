import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class calc(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Calculator")
		self.set_size_request(250, 230)
		self.set_border_width(30)
		self.set_position(Gtk.WindowPosition.CENTER)
		vbox = Gtk.VBox(False, 2)
		def createeButton(name):
			return Gtk.Button(name)
		
		def createButton(name):
			return Gtk.Button(name)
		
		table = Gtk.Table(5, 4, True)
		self.text = Gtk.Entry()
		vbox.pack_start(self.text, False, False, 0)
		vbox.pack_end(table, True, True, 0)
	
	
		#Creating Buttons
		b1  =   createButton("Cls")
		b2  =   createButton("Bck")
		b3  = createButton("Close")
		b4  =     createButton("7")
		b5  =     createButton("8")
		b6  =     createButton("9")
		b7  =     createButton("/")
		b8  =     createButton("4")
		b9  =     createButton("5")
		b10 =     createButton("6")
		b11 =     createButton("*")
		b12 =     createButton("1")
		b13 =     createButton("2")
		b14 =     createButton("3")
		b15 =     createButton("-")
		b16 =     createButton("0")
		b17 =     createButton(".")
		b18 =     createButton("=")
		b19 =     createButton("+")
		
		#Assigning values to buttons.
		
		b19._value  = "+"
		b7._value   = "/"
		b11._value  = "*"
		b17._value  = "."
		b15._value  = "-"
		
		buttons = [b16, b12, b13, b14, b8, b9, b10, b4, b5, b6]
		
		for i in range(len(buttons)):
			buttons[i]._value = str(i)
		
		#Defining click for buttons.

		buttons = [b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b19]
		for button in buttons:
			button.connect("clicked", self.onClick)
		b18.connect("clicked", self.equalClick)
		b1.connect("clicked", self.clear)
		b2.connect("clicked", self.back)
		b3.connect("clicked", Gtk.main_quit)
		
		#Attaching Buttons to table.
		
		table.attach(b1, 0, 1, 0, 1)
		table.attach(b2, 1, 2, 0, 1)
		table.attach(b3, 3, 4, 0, 1)
		table.attach(b4, 0, 1, 1, 2)
		table.attach(b5, 1, 2, 1, 2)
		table.attach(b6, 2, 3, 1, 2)
		table.attach(b7, 3, 4, 1, 2)
		table.attach(b8, 0, 1, 2, 3)
		table.attach(b9, 1, 2, 2, 3)
		table.attach(b10, 2, 3, 2, 3)
		table.attach(b11, 3, 4, 2, 3)
		table.attach(b12, 0, 1, 3, 4)
		table.attach(b13, 1, 2, 3, 4)
		table.attach(b14, 2, 3, 3, 4)
		table.attach(b15, 3, 4, 3, 4)
		table.attach(b16, 0, 1, 4, 5)
		table.attach(b19, 3, 4, 4, 5)
		table.attach(b18, 2, 3, 4, 5)
		table.attach(b17, 1, 2, 4, 5)
		table.attach(Gtk.Label(), 2, 3, 0, 1)
		self.add(vbox)
		self.connect("destroy", Gtk.main_quit)
		self.show_all()
		
	expr = ""
	res = False
	operator = ['+', '-' , '/', '*']
	def onClick(self, widget):
		if self.res and  widget._value not in self.operator:
			eqn = widget._value
			self.text.set_text(eqn)
		else:
			eqn = self.text.get_text()
			eqn +=  widget._value
			self.text.set_text(eqn)
		if self.res == True:
			self.res = False

	def back(self, widget):
		temp = list(self.text.get_text())
		if temp:
			temp.pop()
		val = ""
		for i in temp:
			val += i
		self.text.set_text(val)	

	def equalClick(self, widget):
		res = eval(self.text.get_text())
		self.res = True
		self.text.set_text(str(float(res)))
	def clear(self, widget):
		self.text.set_text("")

calc()
Gtk.main()
		
