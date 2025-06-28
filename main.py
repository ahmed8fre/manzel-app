import kivy 

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager ,FadeTransition
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.utils import platform
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
import webbrowser

import threading
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
from libs.widgets.widgets import Post ,Float_notice ,Float_notice_icon
class WindowManager(ScreenManager):
    '''الشاشه الام للبرنامج '''

class Start(MDScreen):
    '''شاشه التحميل(بدء التشغيل)'''
class Home(MDScreen):
    '''الواجه الرئيسيه للبرنامج'''
    
class Connect(MDScreen):
    '''للتواصل'''
class Main(MDApp):
    def build(self):
        
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cards = [.5,.5,.5,.5 ]
        self.theme_cls.accent_palette = 'Teal'
        self.theme_cls.accent_hue = '400'
        self.title = "MANZEL"
        self.load_all_kv_file()
        self.wm = WindowManager(transition=FadeTransition())
        screens = [
            Home(name = 'home-sc'),Connect(name = 'connect-sc')
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        
        return self.wm
    def change_screen(self ,screen):
        '''الداله المسؤوله عن تغغير الشاشه الحاليه'''
        self.wm.current = screen
        
    def load_all_kv_file(self):
        '''تحميل الصفحات والتصاميم'''
        Builder.load_file('libs/widgets/widgets.kv')
        Builder.load_file('libs/pages/home.kv')
        Builder.load_file('libs/pages/start.kv')
        Builder.load_file('libs/pages/connect.kv')
    def PopupfloatNotice(self ,screen ,notice ,icon):
        '''لإظهار الإشعارات في اعلى الشاشه'''
        if icon:
            notic = Float_notice_icon()
            notic.text = notice
            screen.add_widget(notic)
            Clock.schedule_once(lambda dt: self.remove_widgets(screen,notic), 3)
        else:
            notic = Float_notice()
            notic.text = notice
            screen.add_widget(notic)
            Clock.schedule_once(lambda dt: self.remove_widgets(screen,notic), 3)
    def remove_widgets(self ,screen ,widget):
        screen.remove_widget(widget)
    def open_whatsapp_link(self, url):
        """فتح المتصفح"""
        if platform == 'android':
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
            PythonActivity.mActivity.startActivity(intent)
        else:
            # للتشغيل على سطح المكتب (Windows/Linux/macOS)
            
            webbrowser.open(url)
    
if __name__ == '__main__':
    thread_mainapp = threading.Thread(target=Main().run())
    