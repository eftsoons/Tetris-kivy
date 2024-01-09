from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Line
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
import random
import math

#print(asd[0])
#print(Window.size[1])
#squaresize1 = (asd[0] + asd[1]) * 0.025
#print(asd[0] + asd[1])
#squaresize2 = (asd[0] + asd[1]) * 0.015

squaresize = Window.width * 0.023
squaresize2 =  Window.width * 0.023

speed = 0.25

'''
I-фигура (длинная фигура): (0, 0.6784, 0.9373, 1) - голубой или светло-синий.
J-фигура (фигура в форме буквы "J"): (0, 0, 1, 1) - темно-синий.
L-фигура (фигура в форме буквы "L"): (1, 0.6471, 0, 1) - оранжевый.
O-фигура (квадратная фигура): (1, 1, 0, 1) - желтый.
S-фигура (фигура в форме буквы "S"): (0, 0.5019, 0, 1) - зеленый.
T-фигура (фигура в форме буквы "T"): (0.5019, 0, 0.5019, 1) - фиолетовый.
Z-фигура (фигура в форме буквы "Z"): (1, 0, 0, 1) - красный.
chatgpt is good
'''

'''
0 - палка
1 - квадрат
2 - L
3 - J
4 - S
5 - Z
6 - T

7 - палка в горизантале

8 - L 2 типа (скрин в избранном)
9 - L 3 типа (скрин в избранном)
10 - L 4 типа (скрин в избранном)

11 - J 2 типа (скрин в избранном)
12 - J 3 типа (скрин в избранном) -- ОДНУ ИЗ НИХ ПОПУТАЛ
13 - J 4 типа (скрин в избранном)

14 - S 2 типа

15 - Z 2 типа

16 - T 2 типа
17 - T 3 типа
18 - T 4 типа

ДОДЕЛАТЬ!

'''

obj = {
	"objcoord" : [
		[[0, 10, 20, 30], [7]],
		[[0, 1, 10, 11], [1]],
		[[0, 10, 20, 19], [8]],
		[[0, 10, 20, 21], [11]],
		[[0, -1, 10, 11], [14]],
		[[0, 1, 10, 9], [15]],
		[[0, -1, 1, 10], [16]],


		[[21, 20, 19, 18], [0]], # хз с какой

		[[0, 10, -1, -2], [9]],
		[[8, 18, -1, -2], [10]],
		[[8, 18, 19, 20], [2]],

		[[12, 22, 21, 20], [12]],
		[[1, 2, 12, 22], [13]],
		[[0, 10, 1, 2], [3]],

		[[0, 10, 9, 19], [4]],

		[[10, 9, 20, -1], [5]],

		[[0, 10, -10, 1], [17]],
		[[0, -10, 1, -1], [18]],
		[[0, 10, -10, -1], [6]],
	],
	"objcolor": [
		[0, 0.6784, 0.9373],
		[1, 1, 0],
		[1, 0.6471, 0,],
		[0, 0, 1],
		[0, 0.5019, 0],
		[1, 0, 0],
		[0.5019, 0, 0.5019]
	],
}

main_menu = BoxLayout(orientation='vertical') #horizontal

#label = Label(text="Score: 0", size_hint = [.5, 0.25], font_size = 30)
#label = Label(text="Score: 0", size_hint = [.5, 0.25], size=(100, 150), font_size = 30)

crosses_0_squares = GridLayout(cols=6, size_hint = [1, 0.35])

class TetrisApp(App):

	def _on_keyboard_up(self, windowsinfo, key1, key2):
		if key1 == 115 and hasattr(self, 'schedule'):
			self.speedboostkey(1)

	def _on_keyboard_down(self, windowsinfo, key1, key2, keytext, clamping):
		if keytext == "w":
			self.transform("")
		elif keytext == "a" and hasattr(self, 'schedule'):
			self.tetrisleft("")
		elif keytext == "d" and hasattr(self, 'schedule'):
			self.tetrisright("")
		elif keytext == "s" and hasattr(self, 'schedule'):
			self.speedboostkey(0)
		elif keytext == "f":
			self.start("")

	def build(self):

		Window.bind(on_key_down=self._on_keyboard_down, on_key_up=self._on_keyboard_up)

		self.score = 0

		self.square = []

		self.stopplay = True

		self.label = Label(text="Score: 0", size_hint = [.5, 0.25], font_size = 30)

		wid = Widget()

		#wid = ResizableRectangle(self.square)

		with wid.canvas:
			for x in range(200):
				self.square.append([Color(0.5, 0.5, 0.5, 1, mode = "rgba"), Rectangle(pos=[((x % 10) * squaresize) * 1.1 + Window.width / 2.25, (math.floor(x / 10) * squaresize2) * 1.1  + Window.width / 4.5], size=(squaresize, squaresize2))])
				#Color(0, 0, 0, 1)
				#Line(rectangle=(self.square[x][1].pos[0], self.square[x][1].pos[1], self.square[x][1].size[0], self.square[x][1].size[1]), width=1)


		#with wid.canvas:
			#for x in range(9):
			#	Color(r(), 1, 1, mode='hsv')
				#Rectangle(pos=[r() * wid.width + wid.x,
                              # r() * wid.height + wid.y], size=(20, 20))

		main_menu.add_widget(wid)

		#print(dir(Button(text="321", on_press=self.tetrisleft)))
		crosses_0_squares.add_widget(self.label)
		crosses_0_squares.add_widget(Button(text="<", size_hint = [.25, .5], on_press=self.tetrisleft))
		crosses_0_squares.add_widget(Button(text=">", size_hint = [.25, .5], on_press=self.tetrisright))
		crosses_0_squares.add_widget(Button(text="Transform", size_hint =  [.25, .5], on_press=self.transform))
		crosses_0_squares.add_widget(Button(text=">>>", size_hint =  [.25, .5], on_press=self.speedboost, on_release=self.speedboost2))
		crosses_0_squares.add_widget(Button(text="Start", size_hint =  [.25, .5], on_press=self.start))

		main_menu.add_widget(crosses_0_squares)
		
		return main_menu

	def transform(self, instance):
		if not self.stopplay:
			if self.checktransform():
				for x in self.objecttetris[0][0]:
					self.square[self.objecttetris[0][1] - x][0].rgba = [0.5, 0.5, 0.5, 1]
				self.objecttetris[0][0] = obj["objcoord"][self.objecttetris[0][3][0]][0]
				self.objecttetris[0][3] = obj["objcoord"][self.objecttetris[0][3][0]][1]
				for x in self.objecttetris[0][0]:
					self.square[self.objecttetris[0][1] - x][0].rgba = [self.objecttetris[0][2][0], self.objecttetris[0][2][1], self.objecttetris[0][2][2], 1]
			#else:
				#print(123)

	def checktransform(self):
		result = True 
		change = 0 # доделать!
		for x in obj["objcoord"][self.objecttetris[0][3][0]][0]: # жоско на гавнокодил
			if (self.objecttetris[0][1] - x) % 10 == 9 and self.objecttetris[0][1] % 10 < 5:
				#result = False
				#print((self.objecttetris[0][1] - x) % 10)
				if self.objecttetris[0][3][0] == 13:
					self.shifttetris(-1)
				else:
					self.shifttetris(1)
			if not (self.objecttetris[0][1] - x) % 10 and self.objecttetris[0][1] % 10 > 5:
				#result = False
				#print((self.objecttetris[0][1] - x) % 10)
				if self.objecttetris[0][3][0] == 10:
					self.shifttetris(1)
				else:
					self.shifttetris(-1)
			for x2 in self.xyeta: #genuis хуйня

				if self.objecttetris[0][1] - x == x2[0] + 1 or self.objecttetris[0][1] - x == x2[0] - 1 or self.objecttetris[0][1] - x < x2[0] - 10:
					result = False
			if self.objecttetris[0][1] - x < 0:
				result = False

		return result

	def speedboost2(self, instance):
		if not self.stopplay:
			self.schedule.timeout = speed
		
	def speedboost(self, instance):
		if not self.stopplay:
			self.schedule.timeout = 0.075

	def speedboostkey(self, mode):
		#print(self.schedule.timeout)
		if not self.stopplay:
			if mode == 0:
				self.schedule.timeout = 0.075
			else:
				self.schedule.timeout = speed

	def start(self, instance):
		for x in self.square:
			x[0].rgba = [0.5, 0.5, 0.5, 1]
		
		self.score = 0
		self.label.text = "Score: " + str(self.score)
		self.xyeta = []
		self.objecttetris = []
		if hasattr(self, 'schedule'):
			self.schedule.cancel()
		self.schedule = Clock.schedule_interval(self.update, speed)
		self.spawnobject()
		self.stopplay = False

	def checkblockleft(self):
		result = True
		for x in self.objecttetris[0][0]: #not (self.objecttetris[0][1] - x) % 10
			if not (self.objecttetris[0][1] - x) % 10: # база
				result = False
			for x2 in self.xyeta: #genuis хуйня
				if self.objecttetris[0][1] - x == x2[0] + 1:
					result = False
		return result

	def checkblockright(self):
		result = True
		for x in self.objecttetris[0][0]:
			if (self.objecttetris[0][1] - x) % 10 == 9: # база
				result = False
			for x2 in self.xyeta: #genuis хуйня
				if self.objecttetris[0][1] - x == x2[0] - 1:
					result = False
		return result

	def tetrisleft(self, instance):
		if not self.stopplay and not len(self.objecttetris) == 0:
			if self.checkblockleft():
				#square[objecttetris[0][1]][0].rgba = [0.5, 0.5, 0.5, 1]
				self.shifttetris(-1)

	def tetrisright(self, instanse):
		if not self.stopplay and not len(self.objecttetris) == 0:
			if self.checkblockright():
				self.shifttetris(1)

	def shifttetris(self, number):
		if not self.stopplay:
			for x in self.objecttetris[0][0]:
				self.square[self.objecttetris[0][1] - x][0].rgba = [0.5, 0.5, 0.5, 1]
			self.objecttetris[0][1] = self.objecttetris[0][1] + number
			for x in self.objecttetris[0][0]:
				self.square[self.objecttetris[0][1] - x][0].rgba = [self.objecttetris[0][2][0], self.objecttetris[0][2][1], self.objecttetris[0][2][2], 1]

	def update(self, dt):
		if not self.stopplay:
			self.checkover()
			self.down()
			self.checkanddell()
		#elif len(self.objecttetris) == 0:
			#self.spawnobject()
		else:
			#self.stopplay = False
			#for x in square:
				#x[0].rgba = [0.5, 0.5, 0.5, 1]
			#objecttetris = []
			self.schedule.cancel()

	def checkasdasd(self, test):
		result = True
		for x in self.xyeta:
			if x[0] + 10 == test:
				result = False
		return result

	def checkdsadsa(self, test):
		result = True
		for x in self.xyeta:
			#print(x)
			if x[0] + 1 == test[0] - 10 and x[1] == test[1] and x[2] == test[2] and x[3] == test[3]:
				#x[0] = x[0] + 10
				if self.checkasddsaasddsa(x[0]):
					#x[0] = x[0] + 10
					result = False

		#for x in self.xyeta:
			#print(x)
			if x[0] - 1 == test[0] and x[1] == test[1] and x[2] == test[2] and x[3] == test[3]:
				if self.checkasddsaasddsa(x[0]):
					result = False

		return result

	def checkasddsaasddsa(self, test):
		#print(test)
		result = 1
		dsa = False
		for x in self.xyeta:
			#print(obj)
			for x2 in obj["objcoord"][2][0]:
				#print(x3)
				#print(x2)
				if test - 10 + x2 == x[0]:
					result = result + 1

		if result == 4:
			dsa = True
		result = 0
		return dsa


	def checkanddell(self):
		count = {}
		for index, x in enumerate(self.xyeta): # меня можно убить за гавнокод
	#math.floor((x[1] - x2) / 10
			if count.get(str(math.floor(x[0] / 10))) is not None:
				count[str(math.floor(x[0] / 10))] = int(count[str(math.floor(x[0] / 10))]) + 1
			else:
				count[str(math.floor(x[0] / 10))] = 0
		
		for key, value in count.items():
			key = int(key)
			if value == 9:
				for numberdell in range(key * 10, key * 10 + 10): # genuis хуйня
					for x in self.xyeta:
						if x[0] == numberdell:
							self.square[numberdell][0].rgba = [0.5, 0.5, 0.5, 1]
							self.xyeta.pop(self.xyeta.index(x))

				for _ in range(10):
					for x in self.xyeta:	 # self.checkdsadsa(x) - переделать
						if self.checkasdasd(x[0]) and x[0] - 10 >= 0:
							self.square[x[0]][0].rgba = [0.5, 0.5, 0.5, 1]
							x[0] = x[0] - 10

					for x in self.xyeta:
						self.square[x[0]][0].rgba = [x[1], x[2], x[3], 1]

				self.score += 100
				self.label.text = "Score: " + str(self.score)
				count[str(key)] = None

				#for x in self.xyeta:
					#print(key * 10 + 10)
					#if x[0] >= key * 10 and x[0] <= key * 10 + 10:
						#self.square[x[0] - 10][0].rgba = [1, 1, 1, 1]
						#x[0] = x[0] - 10
							#x[0] = x[0] - 10
							#self.xyeta.pop(self.xyeta.index(x))
							#for x2 in self.xyeta:
								#if x2[0] - 10 == x[0]:
								#	self.xyeta.pop(self.xyeta.index(x2[0] + 10))
									#self.square[x2[0] + 10][0].rgba = [0.5, 0.5, 0.5, 1]
									#self.square[x2[0] - 10][0].rgba = [1, 1, 1, 1]
									#self.xyeta.append([x2[0] - 10, 1, 1, 1])
							#self.xyeta.append([x[0] - 10, 1, 1, 1])
						#x[0] = x[0] - 10
							#for _ in range(0, 5):
								#for x2 in self.xyeta:
									#if x2[0] != numberdell - 10 and x[0] == x2[0] - 10:
										#if x2[0] - 10 >= 0:
											#self.square[x2[0]][0].rgba = [0.5, 0.5, 0.5, 1]
											#self.square[x2[0] - 10][0].rgba = [1, 1, 1, 1]
											#x2[0] = x2[0] - 10
											#self.xyeta.pop(self.xyeta.index(x2))
											#self.xyeta.append([x2[0] - 10, x2[1], x2[2], x2[3]])
									#x2[0] = x2[0] - 10]
										#self.square[x2[0] - 10][0].rgba = [1, 1, 1, 1]
										#for x3 in self.xyeta:
										#	if x3[0] == x2[0] + 10:
												#self.xyeta.pop(self.xyeta.index(x3))
												#self.square[x3[0]][0].rgba = [0.5, 0.5, 0.5, 1]
												#self.square[x3[0] - 10][0].rgba = [1, 1, 1, 1]
											#	self.xyeta.append([x3[0] - 10, x3[1], x3[2], x3[3]])
										#self.xyeta.append([x2[0] - 10, x2[1], x2[2], x2[3]])
									#self.square[x[0]][0].rgba = [x[1], x[2], x[3], 1]
							#for x2 in self.xyeta:
								#if x[0] - 10 != x2[0] and x2[0] == numberdell:
									#print(123)




	def checkover(self):
		for x in self.xyeta:
			if x[0] > 179:
				self.stopplay = True

	def down(self):
		#for x in self.xyeta:
			#self.square[x[1] - x2][0].rgba = [x[2][0], x[2][1], x[2][2], 1]
			#self.square[x[0]][0].rgba = [x[1], x[2], x[3], 1]

		if self.checkblockdown():
			self.shifttetris(-10)
		else:
			#self.xyeta.append([self.objecttetris[0][0], self.objecttetris[0][1], [self.objecttetris[0][2][0], self.objecttetris[0][2][1], self.objecttetris[0][2][2]]])
			for x in self.objecttetris[0][0]:
				self.xyeta.append([self.objecttetris[0][1] - x, self.objecttetris[0][2][0], self.objecttetris[0][2][1], self.objecttetris[0][2][2]])
			self.objecttetris.pop(0)
			self.spawnobject()

	def checkblockdown(self):
		result = True
		for x3 in self.objecttetris[0][0]: #genuis хуйня
			if self.objecttetris[0][1] - x3 <= 9:
				result = False
			
			for x in self.xyeta:
				if self.objecttetris[0][1] - x3 == x[0] + 10 and self.objecttetris[0][1] - x3:
					result = False
		return result


	def spawnobject(self):
		#square[random.randint(190, 199)][0].rgba = [0, 0, 0, 1]
		index = random.randint(183, 187)
		idfigure = random.randint(0, len(obj["objcoord"]) - 1 - 12)
		#idfigure = 3
		intersects = False
		if self.xyeta:
			for x3 in obj["objcoord"][idfigure][0]:
				for x in self.xyeta:
					if index - x3 == x:
						intersects = True
		if not intersects:
			self.objecttetris.append([obj["objcoord"][idfigure][0], index, obj["objcolor"][idfigure], obj["objcoord"][idfigure][1]])


if __name__ == '__main__':
	TetrisApp().run()
