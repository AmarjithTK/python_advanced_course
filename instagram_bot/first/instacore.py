from selenium import webdriver
from random import uniform


def IsAlreadyfollowed(insta_addict):
    css_color = self.driver.getElementByXpath(insta_addict).properties.color
    return true if css_color == True else False



class InstaCore:

    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.url = 'instagram.com'
        self.driver = webdriver.Firefox()

    def seleniumPageLoad(self,url):
        self.driver.get(url)
        # selenium.wait(default=FUll)   

    def getLandingPage(self):

        self.Loadpage(self.url)
        # selenium.wait(default = full_page)
        username_input = self.driver.getElementByXpath('')
        password_input = self.driver.getElementByXpath('')
        username_input.value = self.username
        password_input.value = self.password
        self.driver.sendkeys('return')
        # selenium.wait(default = full_page)


    def like_FeedPosts(self):

       feedposts = self.driver.elementbyxpath('')
       for feedpost in feedposts:
           feedpost.like.sendkeys('return')
           sleep(uniform(10,100)) # make this huge according to instagram guidelines

    def follow_Friends(self):

        # profile_button = self.driver.getElementByXpath('')
        # profile_button.sendkeys('return')
        # # selenium.wait(default = full_page)
        # followers_button = self.driver.getElementByXpath('')
        # followers_button.sendkeys('return')
        feedposts = self.driver.getElementByXpath()
        feedposts[uniform(0, feedposts.__len__())].likers
        # likers_list = self.driver.getElementByXpath('')
        # likers_list(Map(isAlreadyfollowed() => false remove fromlist))
        likers_list[uniform(0, followers_list.__len__())].sendkeys('return')

    def push_Favorites():
        pass
        # export new_favorites.upload.github/gdrive/filestack
        # most likely gitub or filestack

    def add_Comments(addict_post):

        emojiurl = 'emojisite.site'
        self.Loadpage('instagram/?logged_in=yes?feed')
        comments = requests.get(emojiurl).content
        comment_box = self.driver.getElementByXpath('comment box')
        comment_box.sendkeys(comments[random.uniform(0,comments.__len__())])
