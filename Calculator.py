import kivy

kivy.require('1.11.1')
from platform import system as sysv
from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 800)
Config.set('graphics', 'top', 100)

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.properties import ObjectProperty
from sources.database import DataBase
from sources.forms import *

LabelBase.register(name="Arial", fn_regular="static/fonts/arial-unicode-ms.ttf")
LabelBase.register(name="Symbola", fn_regular="static/fonts/Symbola_hint.ttf")
LabelBase.register(name="WISHFUL", fn_regular="static/fonts/WISHFULWAVES.ttf")
LabelBase.register(name="Glitch", fn_regular="static/fonts/CFGlitchCity-Regular.ttf")
LabelBase.register(name="Pixel", fn_regular="static/fonts/pixelplay.ttf")


class A_Error(FloatLayout):
    def close(self):
        close_popup()


class Invalid_Form(FloatLayout):
    def close(self):
        close_form()


class Invalid_Password(FloatLayout):
    def close(self):
        close_pass()


class Configuration(FloatLayout):

    def set_s(self, value):
        if value == "400x600":
            Window.size = (440, 600)
        if value == "600x800":
            Window.size = (625, 800)
        if value == "800x900":
            Window.size = (800, 900)

    def close(self):
        close_config()


class LogWindow(Screen):

    def __init__(self, **kwargs):
        super(LogWindow, self).__init__(**kwargs)

    def on_pre_enter(self):
        Window.set_title("Login")

    def submitBtn(self):
        if db.validate(self.username, self.password):
            return True
        else:
            show_popup()


class CreateWindow(Screen):
    namee = ObjectProperty(None)
    user = ObjectProperty(None)
    password = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CreateWindow, self).__init__(**kwargs)

    def on_pre_enter(self):
        Window.set_title("Create")

    def submit(self):
        if self.namee.text != "" and self.user.text != "":
            if self.password.text != "" and len(self.password.text) >= 6:
                db.add_user(self.user, self.password, self.namee)
            else:
                show_pass()
        else:
            show_form()


class CalcWindow(Screen):
    operated = False
    dot_bef = False
    sign_bef = False

    def __init__(self, **kwargs):
        super(CalcWindow, self).__init__(**kwargs)

    def on_pre_enter(self):
        Window.set_title("Calculator")

    def conf(self):
        show_config()

    def sqroot(self, num):
        self.display.text = square_root(num)

    def elevate_2(self, num):
        self.display.text = elevate_2_f(num)

    def elevate_3(self, num):
        self.display.text = elevate_3_f(num)

    def percentage(self, num):
        self.display.text = percentage_f(num)

    def negate(self, num):
        if negate_f(num) == None:
            pass
        else:
            self.display.text = negate_f(num)

    def calculate(self, calculation):
        self.display.text = calculate_f(calculation)


class SciCalcWindow(Screen):
    operated = False
    dot_bef = False
    sign_bef = False

    def __init__(self, **kwargs):
        super(SciCalcWindow, self).__init__(**kwargs)

    def on_pre_enter(self):
        Window.set_title("Calculator")

    def conf(self):
        show_config()

    def sqroot(self, num):
        self.display.text = square_root(num)

    def elevate_2(self, num):
        self.display.text = elevate_2_f(num)

    def elevate_3(self, num):
        self.display.text = elevate_3_f(num)

    def percentage(self, num):
        self.display.text = percentage_f(num)

    def negate(self, num):
        if negate_f(num) == None:
            pass
        else:
            self.display.text = negate_f(num)

    def absolute(self, num):
        if negate_f(num) == None:
            pass
        else:
            self.display.text = absolute_f(num)

    def factorial(self, num):
        self.display.text = str(factorial_f(num))

    def calculate(self, calculation):
        self.display.text = calculate_f(calculation)


class ProCalcWindow(Screen):
    op = "DEC"

    def __init__(self, **kwargs):
        super(ProCalcWindow, self).__init__(**kwargs)
        self.num_bin = "0"
        self.num_oct = "0"
        self.num_dec = "0"
        self.num_hex = "0"

    def on_pre_enter(self):
        Window.set_title("Calculator")

    def conf(self):
        show_config()

    def binary_o(self, num):
        return bin8(num)

    def binary_d(self, num):
        return bin_(num)

    def binary_h(self, num):
        return bin16(num)

    def octal_b(self, num):
        return oct2(num)

    def octal_d(self, num):
        return oct_(num)

    def octal_h(self, num):
        return oct16(num)

    def decimal_b(self, num):
        return dec2(num)

    def decimal_o(self, num):
        return dec8(num)

    def decimal_h(self, num):
        return dec16(num)

    def hexa_b(self, num):
        return hex2(num)

    def hexa_o(self, num):
        return hex8(num)

    def hexa_d(self, num):
        return hex_(num)


class VolumeWindow(Screen):

    def on_pre_enter(self):
        Window.set_title("Calculator")

    def conf(self):
        show_config()

    def conversion(self, value, op1, op2):

        if (op1 == "Milliliters" or op1 == "Cubic centimeters") and op2 == "Litters":
            x = ml2l(value)
        if (op1 == "Milliliters" or op1 == "Cubic centimeters") and op2 == "Cubic meters":
            if 9 < float(value) < 100:
                x = '%.8f' % float(ml2m(value))
            elif 0 <= float(value) < 10 and "." in value and len(value) == 6:
                x = '%.10f' % float(ml2m(value))
            elif 0 <= float(value) < 10 and "." in value and len(value) == 5:
                x = '%.9f' % float(ml2m(value))
            elif 0 <= float(value) < 10 and "." in value and len(value) == 4:
                x = '%.8f' % float(ml2m(value))
            elif 0 <= float(value) < 10 and "." in value:
                x = '%.7f' % float(ml2m(value))
            elif 0 <= float(value) < 10:
                x = '%.6f' % float(ml2m(value))
            else:
                x = ml2m(value)
        if op1 == "Litters" and (op2 == "Milliliters" or op2 == "Cubic centimeters"):
            x = l2ml(value)
        if op1 == "Litters" and op2 == "Cubic meters":
            x = l2m(value)
        if op1 == "Cubic meters" and (op2 == "Milliliters" or op2 == "Cubic centimeters"):
            x = m2ml(value)
        if op1 == "Cubic meters" and op2 == "Litters":
            x = m2l(value)
        if (op1 == op2) or (op1 == "Milliliters" and op2 == "Cubic centimeters") or (
                op1 == "Cubic centimeters" and op2 == "Milliliters"):
            x = value
        self.display.text = x


class LengthWindow(Screen):

    def on_pre_enter(self):
        Window.set_title("Calculator")

    def conf(self):
        show_config()

    def conversion(self, value, op1, op2):
        x = conversion_op(value, op1, op2)
        self.display.text = x


class CreditsWindow(Screen):
    sys_version = sysv()
    message = "このアプリを使用していただき\n" \
              "        ありがとうございます。\n" \
              "私はあなたがそれをたくさん楽し\n" \
              "         むことを願っています!"
    sign = "- エディ・ヘルナンデス・コト"

    def conf(self):
        show_config()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("sources/my.kv")
db = DataBase("sources/users.txt")
popupWindow = Popup(title="Authentication Error", title_font="Symbola", content=A_Error(), size_hint=(1, .25),
                    pos_hint={"x": 0.001, "y": 0.001}, auto_dismiss=False, separator_height="0dp", title_align="center",
                    title_size="22dp", title_color=[1, 190 / 255, 1, 1])

Invalid_F = Popup(title="Invalid Form", title_font="Symbola", content=Invalid_Form(), size_hint=(1, .25),
                  pos_hint={"x": 0.001, "y": 0.001}, auto_dismiss=False, separator_height="0dp", title_align="center",
                  title_size="22dp", title_color=[1, 190 / 255, 1, 1])

Invalid_P = Popup(title="Invalid Form", title_font="Symbola", content=Invalid_Password(), size_hint=(1, .25),
                  pos_hint={"x": 0.001, "y": 0.001}, auto_dismiss=False, separator_height="0dp", title_align="center",
                  title_size="22dp", title_color=[1, 190 / 255, 1, 1])

Configure = Popup(title="Configuration", content=Configuration(), size_hint=(1, .8), separator_height="0dp",
                  title_align="center", title_font="Symbola", title_size="28sp", auto_dismiss=False)


def show_popup():
    popupWindow.open()


def show_config():
    Configure.open()


def show_form():
    Invalid_F.open()


def show_pass():
    Invalid_P.open()


def close_popup():
    popupWindow.dismiss()


def close_config():
    Configure.dismiss()


def close_form():
    Invalid_F.dismiss()


def close_pass():
    Invalid_P.dismiss()


class MyApp(App):

    def build(self):
        self.title = "Login"
        self.icon = 'static/icons/Calculator-icon.png'
        return kv


if __name__ == "__main__":
    MyApp().run()
