

# kivy library which will provide the GUI
# kivy has 4 parts - App,ScreenManager,Screen,Widgets

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from wikipedia import wikipedia as WP
import requests as RQ

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
   
    def getImageLink(self):

        query = self.manager.current_screen.ids.search_input.text 
        wikiQuery = WP.page(query,auto_suggest=False)
    # wikiQuery = WP.page(query)
        return wikiQuery.images[0]

    def downloadImage(self):


        request_image = RQ.get(self.getImageLink())
        print('works')
        file_string = 'background.jpg'

        with open(file_string,'wb') as file:
            file.write(request_image.content)
        return file_string 

    def setImage(self):   
        
        self.manager.current_screen.ids.img.source = self.downloadImage() 



        # background_image = open('background.jpg','wb')
        # request_image = RQ.get(wikiImages)
        # background_image.write(request_image.content)



      
        # wikipedia = WP.page('Compu')
        # wikiImages = wikipedia.images
        # rqImage = RQ.get(wikiImages[5])
        # image = open('background.jpg','wb')
        # image.write(rqImage.content)
        # print('hello dear')       
        

class RootWidget(ScreenManager):
    pass



class MyApp(App):
    def build(self):
        return RootWidget()

MyApp().run()        
