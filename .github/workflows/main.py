from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.lang import builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from kivy.properties import StringProperty,ListProperty,NumericProperty
from firebase import firebase

firebase=firebase.FirebaseApplication("https://counter-application-3e972-default-rtdb.firebaseio.com/",None)

class ThirdScreen(MDScreen):
    def goSecond(self,instance):
        self.screenManagement.transition.direction = 'right'
        self.screenManagement.current="second"

class SecondScreen(MDScreen):
    
    def goHome(self,instance):
        self.screenManagement.transition.direction = 'right'
        self.screenManagement.current="home"
    
    def goThird(self,instance,text):
        
        app=MDApp.get_running_app()
        app.s_bus=text
        app=MDApp.get_running_app()
        app.route=firebase.get(app.bus+"/"+app.s_bus+"/route","")
        app.mnp=firebase.get(app.bus+"/"+app.s_bus+"/mnp","")
        app.pib=firebase.get(app.bus+"/"+app.s_bus+"/pib","")
        app.sie=firebase.get(app.bus+"/"+app.s_bus+"/sie","")
        app.tseats=firebase.get(app.bus+"/"+app.s_bus+"/tseats","")
        self.screenManagement.transition.direction = 'left'
        self.screenManagement.current="third"
        
        
    
        
class HomeScreen(MDScreen):
    
    def setVehicle(self,instance,text,i_text):
        self.screenManagement.transition.direction = 'left'
        self.screenManagement.current="second"
        app=MDApp.get_running_app()
        app.bus=text
        app.icon=i_text
        

class ScreenManagement(ScreenManager):
    pass


class MainApp(MDApp):
    bus=StringProperty("")
    icon=StringProperty("")
    s_bus=StringProperty("")
    route=StringProperty("")
    mnp=NumericProperty()
    pib=NumericProperty()
    sie=NumericProperty()
    tseats=NumericProperty()
    def build(self):
        return ScreenManagement()
        

if __name__=='__main__':
    MainApp().run()