import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

class Widgets(Widget):
	def btn_clicked(self):
		show_popup()

class ThePopup(FloatLayout):
	pass

def show_popup():
	show = ThePopup()
	my_popup = Popup(title="Alert!", content=show, size_hint=(None, None), size=(400, 400))
	my_popup.open()

class MyApp(App):
	def build(self):
		return Widgets()

if __name__ == '__main__':
	MyApp().run()

