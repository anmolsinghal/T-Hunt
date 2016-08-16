from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, WipeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from plyer import gps





sm=ScreenManager()

class RegScreen(Screen):
	
	def next(self):
		sm.add_widget(RegScreen2(name='RegScreen2'))
		sm.transition = SlideTransition(direction="left")
		sm.current='RegScreen2'
		#Starting Game Here
		

class RegScreen2(Screen):
	def register(self):
		sm.add_widget(Dashboard(name='Dashboard'))
		sm.transition = SlideTransition(direction="left")
		sm.current='Dashboard'
		#Starting Game Here
		sm.add_widget(Clue1(name='clue1'))
		Dashboard.SolvedCount=0

class Dashboard(Screen):
	SolvedCount=NumericProperty()
	popup = Popup(title='Oops',
    		content=Label(text='Locked'),
    		size_hint=(None, None), size=(400, 400))
	#def UnlockClue(self,clue,cluename):
		#sm.add_widget(clue(name=cluename))
	def GotoClue(self,cluename):
		
		try:
			sm.current=cluename
			sm.transition = SlideTransition(direction="left")
		except:
			self.popup.open()
			
	



	



class Clue(Screen):
	IsSolved=BooleanProperty(False)
	popup = Popup(title='Oops',
    		content=Label(text='Locked'),
    		size_hint=(None, None), size=(400, 400))
	def Goto(self,name,direction):
		
		try:
			sm.current=name
			sm.transition = SlideTransition(direction=direction)
		except:
			self.popup.open()
	#pb=ProgressBar(max=2000)
	#pb.value=distancefromclue()
	lb=Label()
	#def distancefromclue(**kwargs):
	#	lb.text={lat},{lon}.format(**kwargs)
	#gps.configure(on_location=distancefromclue)
	#gps.start()

			
		

screennames=[('Clue'.format(i)) for i in range(1,4)]
print screennames
class Clue1(Clue):


	def Solved(self):
		if self.IsSolved is False:
			self.IsSolved=True
			Dashboard.SolvedCount+=1
			print Dashboard.SolvedCount
			sm.add_widget(Clue2(name='clue2'))
			self.Goto('clue2',"left")
	
class Clue2(Clue):
	def Solved(self):
		if self.IsSolved is False:
			self.IsSolved=True
			Dashboard.SolvedCount+=1
			print Dashboard.SolvedCount
			sm.add_widget(Finish(name='fin'))
			self.Goto('fin',"left")

class Finish(Screen):

	def Goto(self,name,direction):
		sm.transition = SlideTransition(direction=direction)
		try:
			sm.current=name
		except:
			print "Locked"


	
			
		
	
		

	



class ThuntApp(App):
	def build(self):
		sm.add_widget(RegScreen(name='Reg'))
		#sm.add_widget(Dashboard(name='Dboard'))
		return sm

if __name__ == '__main__':
    ThuntApp().run()


