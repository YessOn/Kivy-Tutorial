import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1

		self.inside = GridLayout()
		self.inside.cols = 2
		self.inside.add_widget(Label(text="My First Name"))
		self.f_name = TextInput(multiline=False)
		self.inside.add_widget(self.f_name)

		self.inside.add_widget(Label(text="My Last Name"))
		self.l_name = TextInput(multiline=False)
		self.inside.add_widget(self.l_name)

		self.inside.add_widget(Label(text="My Email"))
		self.email = TextInput(multiline=False)
		self.inside.add_widget(self.email)

		self.add_widget(self.inside)

		self.submit = Button(text="Submit", font_size=32)
		self.submit.bind(on_press=self.pressed)
		self.add_widget(self.submit)

	def pressed(self, instance):
		fname = self.f_name.text
		lname = self.l_name.text
		email = self.email.text
		print(f"First Name: {fname}. Last Name: {lname}, Email: {email}")
		self.f_name.text = ""
		self.l_name.text = ""
		self.email.text = ""


class MyApp(App):
	def build(self):
		return MyGrid()


if __name__ == '__main__':
	MyApp().run()

