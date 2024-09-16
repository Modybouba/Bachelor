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
source.include_exts = py,png,jpg,kv,atlas,json,txt

# Dateien oder Verzeichnisse, die von der .apk-Datei ausgeschlossen werden
source.exclude_exts = spec

# (main.py) Hauptdatei der Anwendung
source.main = main.py

# (.) Quelle des Codes
source.dir = .

# Konfiguration der Verteilungsdatei
# Erstellen Sie ein Kivy-Paket mit den Kivy-Abhängigkeiten
requirements = python3,kivy==2.3.0,bleak,asyncio,setuptools,android,pyjnius,plyer


# (1) Aktivieren des Debug-Modus für die Android-APK
android.debug = 1

# Zusätzliche Argumente, die an p4a (python-for-android) übergeben werden
p4a = --sdk_dir=$HOME/.buildwsl ozer/android/platform/android-sdk

# Unterstützte Bildschirmorientierung (Hoch- und Querformat)
orientation = portrait,landscape

# Berechtigungen für die Android-Anwendung (z. B. Netzwerkzugriff, Bluetooth)
android.permissions = android.permission.INTERNET,android.permission.BLUETOOTH,android.permission.ACCESS_COARSE_LOCATION,android.permission.WRITE_EXTERNAL_STORAGE,android.permission.READ_EXTERNAL_STORAGE,android.permission.ACCESS_NETWORK_STATE,android.permission.BLUETOOTH_PRIVILEGED,android.permission.BLUETOOTH_SCAN,android.permission.BLUETOOTH_CONNECT,android.permission.BLUETOOTH_ADMIN,android.permission.BLUETOOTH_ADVERTISE,android.permission.ACCESS_FINE_LOCATION,BLUETOOTH,ACCESS_COARSE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE,BLUETOOTH_PRIVILEGED,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,BLUETOOTH_ADMIN,BLUETOOTH_ADVERTISE,ACCESS_FINE_LOCATION

# Python-Version für die Android-Anwendung
android.python_version = 3

# Wenn spezifische Konfigurationsdateien oder Daten benötigt werden
android.add_asset_dirs = assets

# Pfad zum App-Symbol
android.icon = icon.png

# Mindest-API für unterstütztes Android
android.minapi = 21

# Maximale unterstützte Android-API
android.maxapi = 34

# Ziel-SDK für die Erstellung
#android.sdk = 33

# Architektur der Android-Anwendung (armeabi-v7a für 32 Bit, arm64-v8a für 64 Bit)
android.archs = armeabi-v7a, arm64-v8a

# Aktivierung von Cython-Optimierungen
cython.optimize = 1

[buildozer]
# (int) Log-Level (0 = nur Fehler, 1 = Info, 2 = Debug (mit Konsolenausgabe))
log_level = 2

# Pfade für das Android SDK und NDK
android.sdk_path = /home/boubadiallo/.buildozer/android/platform/android-sdk
android.ndk_path = /home/boubadiallo/.buildozer/android/platform/android-ndk-r25b
