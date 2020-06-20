import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class FirstWindow(Screen):
	pass

class SecondWindow(Screen):
	pass

class Manager(ScreenManager):
	pass

class MyApp(App):
	def build(self):
		return Builder.load_file("8.screen_navigation.kv")

if __name__ == '__main__':
	MyApp().run()

