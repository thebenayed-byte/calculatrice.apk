from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CalcApp(App):
    def build(self):
        layout = GridLayout(cols=4)

        self.result = TextInput(font_size=40, readonly=True, multiline=False)
        layout.add_widget(self.result)

        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "C","0","=","+"
        ]

        for b in buttons:
            btn = Button(text=b, font_size=32)
            btn.bind(on_press=self.click)
            layout.add_widget(btn)

        return layout

    def click(self, instance):
        t = instance.text

        if t == "C":
            self.result.text = ""
        elif t == "=":
            try:
                self.result.text = str(eval(self.result.text))
            except:
                self.result.text = "Erreur"
        else:
            self.result.text += t


CalcApp().run()
