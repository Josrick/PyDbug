import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivymd.app import MDApp
import sqlite3
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
import time


class CreateAccountWindow(Screen):
    nickname = ObjectProperty(None)
    schid = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.nickname.text != "" and self.password.text != "" and self.schid.text.count(""):
            if self.password != "":
                db.add_user(self.schid.text, self.password.text, self.nickname.text)

                self.reset()

                sm.current = "login"
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.schid.text = ""
        self.password.text = ""
        self.nickname.text = ""


class LoginWindow(Screen):
    schid = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.schid.text, self.password.text):
            MainWindow.current = self.schid.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.schid.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"
    def Start(self):
        sm.current = "menu"
    def Leaderboard(self):
        sm.current = "menu"



    def on_enter(self, *args):
        markup: True
        password, nickname, created = db.get_user(self.current)
        self.n.text = "[color=#F19A0A][b]Account Name:[/b][/color] " + nickname
        self.schid.text = "[color=#F19A0A][b]School Id:[/b][/color] " + self.current
        self.created.text = " [color=#F19A0A][b]Created On:[/b][/color] " + created

class MenuWindow(Screen):


    def game1(self):
        sm.current = "gs1"
    def game2(self):
        sm.current = "main"

class Gamestart1Window(Screen):

    def startbtn1(self):
        sm.current = "qsa"


class QuestionsaWindow(Screen):

    number = NumericProperty()

    def __init__(self, **kwargs):
        super(QuestionsaWindow, self).__init__(**kwargs)
        Clock.schedule_interval(self.increment_time, .1)

        self.increment_time(0)

    def increment_time(self, interval):
        self.number += .1



    def init(self, kwargs):
        super(QuestionsaWindow, self).init(kwargs)
        self.label_value = 0

    def do_action(self):
        self.my_label.text = 'Write a Python program that accepts a word from the user and reverse it.'


    def leftd(self):
        sm.current = "qsd"

    def rightb(self):
        sm.current = "qsb"

    def selectb(self):
        sm.current = "qsb"



class QuestionsbWindow(Screen):
    number = NumericProperty()

    def __init__(self, **kwargs):
        super(QuestionsbWindow, self).__init__(**kwargs)
        Clock.schedule_interval(self.increment_time, .1)

        self.increment_time(0)

    def increment_time(self, interval):
        self.number += .1

    def startb(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)

    def init(self, kwargs):
        super(QuestionsbWindow, self).init(kwargs)
        self.label_value = 0

    def do_action(self):
        self.my_label.text = 'Write a Python program that accepts a word from the user and reverse it.'

    def lefta(self):
        sm.current = "qsa"

    def rightc(self):
        sm.current = "qsc"

    def selectb(self):
        sm.current = "qsc"

class QuestionscWindow(Screen):
    number = NumericProperty()

    def __init__(self, **kwargs):
        super(QuestionscWindow, self).__init__(**kwargs)
        Clock.schedule_interval(self.increment_time, .1)

        self.increment_time(0)

    def increment_time(self, interval):
        self.number += .1

    def startc(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)

    def init(self, kwargs):
        super(QuestionscWindow, self).init(kwargs)
        self.label_value = 0

    def do_action(self):
        self.my_label.text = 'Write a Python program that accepts a word from the user and reverse it.'

    def leftb(self):
        sm.current = "qsb"

    def rightd(self):  
        sm.current = "qsd"

    def selectc(self):
        sm.current = "qsd"

class QuestionsdWindow(Screen):
    number = NumericProperty()

    def __init__(self, **kwargs):
        super(QuestionsdWindow, self).__init__(**kwargs)
        Clock.schedule_interval(self.increment_time, .1)

        self.increment_time(0)

    def increment_time(self, interval):
        self.number += .1

    def startd(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)

    def init(self, kwargs):
        super(QuestionsdWindow, self).init(kwargs)
        self.label_value = 0

    def do_action(self):
        self.my_label.text = 'Write a Python program that accepts a\n word from the user and reverse it.'

    def leftc(self):
        sm.current = "qsc"

    def righta(self):
        sm.current = "qsa"

    def selectd(self):
        sm.current = "qsa"

class FinishWindow(Screen):

    def Leaderboard(self):
        sm.current = "login"

    def QuitGame(self):
        sm.current = "login"




class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid School ID or Password.'),
                  size_hint=(None, None), size=(350, 350))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()



kv = Builder.load_file("PyDbug.kv")

sm = WindowManager()
db = DataBase("User.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),MenuWindow(name="menu"),
           Gamestart1Window(name="gs1"),QuestionsaWindow(name="qsa"),QuestionsbWindow(name="qsb"),QuestionscWindow(name="qsc"),
           QuestionsdWindow(name="qsd"), FinishWindow(name="fdw")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class PyDBugApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 0)
        return sm


if __name__ == "__main__":
    PyDBugApp().run()