import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.textinput import TextInput

class RegScreen(App):
  def build(self):
    layout=BoxLayout(orientation='vertical')
    layout.add_widget(Label(text='Team Lead ID',size_hint=(1,0.1)))
    layout.add_widget(TextInput(multiline='False',size_hint=(1,0.1)))
    layout.add_widget(Label(text='Team memebers ID',size_hint=(1,0.1)))
    layout.add_widget(TextInput(multiline='True',size_hint=(1,0.6)))
    layout.add_widget(Button(text='Register', size_hint=(1,0.1)))
    return layout
if __name__=="__main__":
  app=RegScreen()
  app.run()

    
    
  
