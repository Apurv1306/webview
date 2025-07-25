[app]
title = FaceApp
package.name = faceapp
package.domain = com.example
source.dir = .
source.include_exts = py,html,js,css,png,jpg,jpeg,kv
version = 0.1.0

requirements = python3, kivy==2.3.0, kivy_garden.webview, flask, requests, opencv-python-headless, numpy, cython, pillow

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.accept_sdk_license = True


# ──────────────────────────────────────────────
# NEW SECTION ─ fixes “No section: 'buildozer'”

[buildozer]
log_level   = 1           # 0=errors, 1=info, 2=debug
warn_on_root = 1          # required token! (default “1”)
# build_dir  = ./.buildozer
# bin_dir    = ./bin
