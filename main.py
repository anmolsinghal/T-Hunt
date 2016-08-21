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

rom kivy.clock import Clock

from plyer import compass
from plyer import accelerometer



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
	def distancefromclue(**kwargs):
		lb.text={lat},{lon}.format(**kwargs)
	gps.configure(on_location=distancefromclue)
	gps.start()



class CompassTest(BoxLayout):
    def __init__(self):
        super(CompassTest, self).__init__()
        self.sensorEnabled = False
    def solved(self):
    	sm.add_widget(Clue2(name='AccelerometerTest'))
			self.Goto('AccelerometerTest',"left")    
    def do_toggle(self):
        try:
            if not self.sensorEnabled:
                compass.enable()
                Clock.schedule_interval(self.get_readings, 1 / 20.)

                self.sensorEnabled = True
                self.ids.toggle_button.text = "Stop compass"
            else:
                compass.disable()
                Clock.unschedule(self.get_readings)

                self.sensorEnabled = False
                self.ids.toggle_button.text = "Start compass"
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            status = "Compass is not implemented for your platform"
            self.ids.status.text = status

    def get_readings(self, dt):
        val = compass.orientation

        self.ids.x_label.text = "X: " + str(val[0])
        self.ids.y_label.text = "Y: " + str(val[1])
        self.ids.z_label.text = "Z: " + str(val[2])

class AccelerometerTest(BoxLayout):
    def __init__(self):
        super(AccelerometerTest, self).__init__()
        self.sensorEnabled = False
    def solved(self):
    	sm.add_widget(Clue2(name='clue2'))
			self.Goto('clue2',"left")     

    def do_toggle(self):
        try:
            if not self.sensorEnabled:
                accelerometer.enable()
                Clock.schedule_interval(self.get_acceleration, 1 / 20.)

                self.sensorEnabled = True
                self.ids.toggle_button.text = "Stop Accelerometer"
            else:
                accelerometer.disable()
                Clock.unschedule(self.get_acceleration)

                self.sensorEnabled = False
                self.ids.toggle_button.text = "Start Accelerometer"
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            status = "Accelerometer is not implemented for your platform"
            self.ids.accel_status.text = status

    def get_acceleration(self, dt):
        val = accelerometer.acceleration[:3]

        if not val == (None, None, None):
            self.ids.x_label.text = "X: " + str(val[0])
            self.ids.y_label.text = "Y: " + str(val[1])
            self.ids.z_label.text = "Z: " + str(val[2])			
		

screennames=[('Clue'.format(i)) for i in range(1,4)]
print screennames
class Clue1(Clue):


	def Solved(self):
		if self.IsSolved is False:
			self.IsSolved=True
			Dashboard.SolvedCount+=1
			print Dashboard.SolvedCount
			sm.add_widget(Clue2(name='CompassTest'))
			self.Goto('CompassTest',"left")
	
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

