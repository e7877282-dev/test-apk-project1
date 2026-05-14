from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.lbl = Label(text="Моё первое Android-приложение!", font_size='20sp')
        layout.add_widget(self.lbl)
        btn = Button(text="Нажми меня", font_size='18sp')
        btn.bind(on_press=self.click_btn)
        layout.add_widget(btn)
        return layout

    def click_btn(self, instance):
        self.lbl.text = "Кнопка успешно работает!"

if __name__ == "__main__":
    TestApp().run()

