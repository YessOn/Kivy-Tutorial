import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


class Touch(Widget):
	btn = ObjectProperty(None)
	def on_touch_down(self, touch):
		print("Down", touch)
		self.btn.opacity = 0.5

	def on_touch_move(self, touch):
		print("Move", touch)

	def on_touch_up(self, touch):
		print("Up", touch)
		self.btn.opacity = 1

class MyApp(App):
	def build(self):
		return Touch()

if __name__ == '__main__':
	MyApp().run()
