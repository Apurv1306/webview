[app]
title = FaceApp
package.name = faceapp
package.domain = com.example
source.dir = .
source.include_exts = py,html,js,css,png,jpg,jpeg,kv
version = 0.1.0                         # ←- required!

# Python & C-extensions your project needs
requirements = python3, kivy==2.3.0, kivy_garden.webview, flask, requests, opencv-python-headless, numpy, cython, pillow

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.accept_sdk_license = True       # speeds up CI

# uncomment if you need a custom icon
# icon.filename = %(source.dir)s/icon.png
