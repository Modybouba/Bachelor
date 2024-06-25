[app]

# Nom de votre application
title = MyArduinoApp

# Nom du package
package.name = myarduinoapp

# Version de votre application
version = 0.1

# Domaine du package
package.domain = org.example
# (str) Source code where the main.py is located
source.dir = .

# Extensions à inclure
source.include_exts = py,png,jpg,kv,atlas

# Bibliothèques nécessaires
requirements = python3,kivy,bleak

# Permissions Android
android.permissions = INTERNET

# Désactiver le support multithread
android.multithreaded = 0

# SDK et NDK paths
[buildozer]
android.sdk_path = /home/boubadiallo/.buildozer/android/platform/android-sdk
android.ndk_path = /home/boubadiallo/.buildozer/android/platform/android-ndk-r21e
