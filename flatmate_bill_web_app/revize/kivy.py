from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('app_design.kv') # kivy file for app loading


class RootWidget(ScreenManager):
    pass
   

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass


class MyApplication(App):
    def build(self):
        return RootWidget()

MyApplication().run()