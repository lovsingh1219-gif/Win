from kivy.app import App
from kivy.uix.label import Label


class NameApp(App):
    def build(self):
        return Label(
            text="Kush Singh",
            font_size="40sp"
        )


NameApp().run()