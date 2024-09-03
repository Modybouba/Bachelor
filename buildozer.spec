[app]
# (my_app_name) Name Ihrer Anwendung
title = My Arduino App

# (org.example.myapp) Paketname (muss einzigartig sein)
package.name = myarduinoapp

# (com.example) Domain für die Anwendung
package.domain = org.myarduino

# (1.0) Version der Anwendung
version = 1.0

# Dateien und Verzeichnisse, die in die .apk-Datei aufgenommen werden
source.include_exts = py,png,jpg,kv,atlas

# Dateien oder Verzeichnisse, die von der .apk-Datei ausgeschlossen werden
source.exclude_exts = spec

# (main.py) Hauptdatei der Anwendung
source.main = main.py

# (.) Quelle des Codes
source.dir = .

# Konfiguration der Verteilungsdatei
# Erstellen Sie ein Kivy-Paket mit den Kivy-Abhängigkeiten
requirements = python3, kivy, bleak, asyncio, setuptools, android




# Zusätzliche Argumente, die an p4a übergeben werden
#p4a = --sdk_dir=$HOME/.buildozer/android/platform/android-sdk

# Unterstützte Bildschirmorientierung
orientation = portrait

# Berechtigungen für die Anwendung deaktivieren
# Berechtigungen für die Android-Anwendung (z. B. Netzwerkzugriff, Bluetooth)
android.permissions = INTERNET, ACCESS_NETWORK_STATE, BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_WIFI_STATE, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION


# Wenn Sie spezifische Konfigurationsdateien oder Daten benötigen, können Sie sie hier angeben
android.add_asset_dirs = assets

# Fügen Sie hier Ihre Symboldateien hinzu
android.icon = icon.png

# Mindest-API für unterstütztes Android
android.minapi = 21

# Maximale unterstützte Android-API
android.maxapi = 33

# Ziel-SDK für die Erstellung
android.sdk = 33

# Architektur der Android-Anwendung (armeabi-v7a für 32 Bit, arm64-v8a für 64 Bit)
android.archs = arm64-v8a


# Aktivierung von Cython-Optimierungen
cython.optimize = 1

[buildozer]
# SDK et NDK paths
android.sdk_path = /home/boubadiallo/.buildozer/android/platform/android-sdk
android.ndk_path = /home/boubadiallo/.buildozer/android/platform/android-ndk-r21e
