[app]
title = My Test App
package.name = mytestapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

# Жестко прописываем актуальные рабочие версии Android
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools_version = 33.0.0

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
