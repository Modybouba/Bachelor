[app]

# Nom de l'application
title = MyArduinoApp

# Package
package.name = MyArduinoapp
package.domain = org.test

# Version de l'application (optionnel)
version = 1.0.0

# Chemin vers le fichier principal de votre application
source.dir = .

# Extensions de fichiers à inclure dans la source
source.include_exts = py,png,jpg,kv,atlas

# Dossiers à exclure
source.exclude_dirs = tests, bin, .git, __pycache__

# Dépendances de l'application (à adapter selon les besoins)
requirements = python3,kivy,bleak

# Autorisations nécessaires pour l'application Android
android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN

# Orientations prises en charge
orientation = portrait

# Option pour indiquer si l'application doit être en plein écran ou non
fullscreen = 0

# Icone de l'application (optionnel, à adapter)
icon.filename = icon.png

# Présplash de l'application (optionnel, à adapter)
presplash.filename = presplash.png

# SDK et NDK paths
[buildozer]
android.sdk_path = /home/boubadiallo/.buildozer/android/platform/android-sdk
android.ndk_path = /home/boubadiallo/.buildozer/android/platform/android-ndk-r21e

