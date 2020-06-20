import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line


class Touch(Widget):
	def __init__(self, **kwargs):
		super(Touch, self).__init__(**kwargs)

		with self.canvas:
			Color(1, 0, 1, .6, mode="rgba")
			self.rect = Rectangle(pos=(400, 280), size=(10, 10))
			Color(.5, 0, 1, .6, mode="rgba")
			self.line = Line(points=self.rect.pos, width=10)
	def on_touch_down(self, touch):
		self.rect.pos = touch.pos
		self.line.points += touch.pos

	def on_touch_move(self, touch):
		self.rect.pos = touch.pos
		self.line.points += touch.pos

	def on_touch_up(self, touch):
		pass

class MyApp(App):
	def build(self):
		return Touch()

if __name__ == '__main__':
	MyApp().run()

