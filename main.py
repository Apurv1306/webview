# main.py
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# ---------- start Flask backend in a background thread ----------
def _start_backend():
    from app import app as flask_app            # import the Flask object
    flask_app.run(host="0.0.0.0", port=5000, threaded=True)

threading.Thread(target=_start_backend, daemon=True).start()

# ---------- simple WebView front end ----------
class FaceAppMobile(App):
    def build(self):
        from kivy_garden.webview import WebView
        root = BoxLayout(orientation="vertical")
        root.add_widget(
            WebView(url="http://127.0.0.1:5000")  # loads app.html via Flask
        )
        return root

if __name__ == "__main__":
    FaceAppMobile().run()
