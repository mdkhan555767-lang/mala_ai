[app]
title = Mala AI
package.name = malaai
package.domain = org.mala.ai
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,WAKE_LOCK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

[buildozer]
log_level = 2
warn_on_root = 1
