from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import threading
import time

class MalaAIApp(App):
    def build(self):
        self.title = "Mala AI - VIP Boss Mode"
        self.is_boss_mode = False
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.status_label = Label(
            text="[ Guest Mode Active ]\nSay the passphrase to unlock VIP Boss Mode.",
            markup=True,
            font_size='18sp',
            halign='center'
        )
        layout.add_widget(self.status_label)
        
        self.action_button = Button(
            text="Activate Voice Recognition",
            font_size='16sp',
            size_hint=(1, 0.3),
            background_color=(0.1, 0.6, 0.8, 1)
        )
        self.action_button.bind(on_press=self.simulate_voice_command)
        layout.add_widget(self.action_button)
        
        return layout

    def simulate_voice_command(self, instance):
        self.status_label.text = "Listening for voice command..."
        threading.Thread(target=self._verify_boss).start()

    def _verify_boss(self):
        time.sleep(2)
        self.is_boss_mode = True
        self.status_label.text = "[ VIP BOSS MODE UNLOCKED ]\nWelcome back, Boss! All systems under your control."
        self.action_button.text = "Boss Commands Ready"

if __name__ == '__main__':
    MalaAIApp().run()
