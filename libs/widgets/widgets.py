from kivy.uix.accordion import ObjectProperty
from kivy.uix.accordion import StringProperty 
from kivy.animation import Animation
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivy.animation import Animation
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.label import Label
from kivy.properties import *
class Post(MDCard):
    image = StringProperty()
class Float_notice(MDCard):
    text = StringProperty()
    screen = ObjectProperty()
class Float_notice_icon(MDCard):
    text = StringProperty()
    screen = ObjectProperty()

class AppDrop(MDCard):
    valu = False

    def check(self):
        if self.valu:
            self.on_close()
            self.valu = False
        else:
            self.on_open()
            self.valu = True
    def on_open(self):
        Animation(
            duration = .7, 
            # size_hint_x = 0.9,
            pos_hint= {'center_y': 0.85 }
        ).start(self)
        

    def on_close(self):
        
        Animation(
            duration = .7,
            # size_hint_x = 0.9,
            pos_hint= {'center_y': 1.5}
        ).start(self)
class MyScroll(MDScrollView):
    def on_scroll_start(self, touch, check_children=True):
        # print(self.scroll_y)
        if self.scroll_y > 1:
            print('update!')
        elif self.scroll_y < 0:
            print('more!')
        return super().on_scroll_start(touch, check_children)
class MDARLabel(Label):
    """الخط العربي"""
