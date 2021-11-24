from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

Builder.load_file('frontend.kv')



class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
    
    def capture(self):
        pass

    def stop(self):
        pass



class FileSharer():
    def __init__(self):
        self.apiKey = 'apikey'
        self.filepath = 'files/captured.jpg'


    def upload():
        pass
        return link



class RootWidget(ScreenManager):
    pass


class CamApp(App):
    def build(self):
        return RootWidget()


CamApp().run()