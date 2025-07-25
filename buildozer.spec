[app]
title = FaceApp
package.name = faceapp
package.domain = com.example
source.dir = .
source.include_exts = py,html,js,css,png,jpg,jpeg,kv
# bundle all static files:
presplash.filename = %(source.dir)s/app.html

requirements = python3, kivy==2.3.0, kivy_garden.webview, flask, requests, opencv-python-headless, numpy, cython, pillow

orientation = portrait
android.permissions = CAMERA, INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# Speed up CI:
android.accept_sdk_license = True
