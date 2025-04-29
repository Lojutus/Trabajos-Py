from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
class Formulario(GridLayout):
    def __init__(self, **kwargs):
        super(Formulario, self).__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text='Nombre:'))
        self.nombre = TextInput()
        self.add_widget(self.nombre)
        
        self.add_widget(Label(text='Edad:'))
        self.edad = TextInput()
        self.add_widget(self.edad)
        
        self.add_widget(Label(text='Correo electrónico:'))
        self.email = TextInput()
        self.add_widget(self.email)
        
    def guardar_formulario(self):
        with open("formulario.txt", "w") as archivo:
            archivo.write(f"Nombre: {self.nombre}\n")
            archivo.write(f"Edad: {self.edad}\n")
            archivo.write(f"Correo electrónico: {self.email}\n")
            
class MyApp(App):
    def build(self):
        return Formulario()

if __name__ == '__main__':
    MyApp().run()
