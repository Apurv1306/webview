# main.py
import os, threading, webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

# ---------- 1. Start backend ----------
def _start_backend():
    from app import app as flask_app      # import your Flask instance
    flask_app.run(host="0.0.0.0", port=5000, threaded=True)

threading.Thread(target=_start_backend, daemon=True).start()

# ---------- 2. Simple WebView front ----------
class Root(BoxLayout):
    pass

class FaceAppMobile(App):
    def build(self):
        from kivy_garden.webview import WebView
        root = Root(orientation="vertical")
        root.add_widget(
            WebView(url="http://127.0.0.1:5000")   # loads app.html routed by Flask
        )
        return root

if __name__ == "__main__":
    FaceAppMobile().run()
