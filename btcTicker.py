# !/usr/bin/python
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

import datetime
import time

from getStampTicker import GetTicker

class BigLabel(Label):
    """ Big label class """
    def __init__(self, *args, **kwargs):
        super(BigLabel, self).__init__(*args, **kwargs)


class BigTextInput(TextInput):
    """ Big label class """
    def __init__(self, *args, **kwargs):
        super(BigTextInput, self).__init__(*args, **kwargs)


class RootWidget(BoxLayout):
    """Root Kivy accordion widget class"""
    btc_multiplier_input = ObjectProperty()
    btc_amount_input = ObjectProperty()
    multiplied_btc_amount_input = ObjectProperty()
    usd_amount_input = ObjectProperty()
    multiplied_usd_amount_input = ObjectProperty()
    last_updated_text = ObjectProperty()

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.last_BTCUSD_price = 0.0
        self.last_time_checked = 0
        Clock.schedule_once(self.checkTicker, 0.1)
        Clock.schedule_interval(self.checkTicker, 3)

    def checkTicker(self, dt):
        self.last_BTCUSD_price, self.last_time_checked = GetTicker()
        print(self.last_BTCUSD_price, self.last_time_checked)
        try:
            temp_time = time.strftime('%H:%M:%S', time.localtime(self.last_time_checked))
            self.last_updated_text.text = "Last updated from Bitstamp @ [color=00ff00]{0}[/color]\nLast price (USD/BTC) was [color=ffff00]{1:0.2f}[/color] $/BTC".format(temp_time, self.last_BTCUSD_price)
            self.multiplied_usd_amount_input.text = "{0:.2f}".format(float(self.btc_amount_input.text)*float(self.last_BTCUSD_price)*float(self.btc_multiplier_input.text))
            self.multiplied_btc_amount_input.text = "{0:.3f}".format(float(self.usd_amount_input.text)/(float(self.last_BTCUSD_price)*float(self.btc_multiplier_input.text)))
        except:
            print("updated FAILED")




class btcTickerApp(App):
    def build(self):
        root = RootWidget()
        return root


if __name__ == '__main__':
    Config.set('kivy', 'exit_on_escape', 0)
    Config.set('kivy', 'window_icon', "./favicon.ico")
    Config.set('input', 'mouse', 'mouse,disable_multitouch')
    btcTickerApp().run()


