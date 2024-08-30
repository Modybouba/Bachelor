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

# Konfiguration der Verteilungsdatei
# Erstellen Sie ein Kivy-Paket mit den Kivy-Abhängigkeiten
requirements = python3, kivy, bleak, asyncio, threading, kivy.uix.screenmanager, kivy.uix.screen, kivy.clock, kivy.lang, socket

# Zusätzliche Argumente, die an p4a übergeben werden
p4a = --sdk_dir=$HOME/.buildozer/android/platform/android-sdk

# Unterstützte Bildschirmorientierung
orientation = portrait

# Berechtigungen für die Anwendung deaktivieren
# Berechtigungen für die Android-Anwendung (z. B. Netzwerkzugriff, Bluetooth)
android.permissions = INTERNET, ACCESS_NETWORK_STATE, BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_WIFI_STATE

# Wenn Sie spezifische Konfigurationsdateien oder Daten benötigen, können Sie sie hier angeben
android.add_asset_dirs = assets

# Fügen Sie hier Ihre Symboldateien hinzu
android.icon = icon.png

# (index.html) Index-Datei Ihrer Webanwendung
# Diese Option wird nur verwendet, wenn Sie eine Webanwendung erstellen
# android.wv_server.index_file = index.html

# Weitere C-, C++- oder nativen Abhängigkeiten (z.B. SDL, Gstreamer)
# android.add_javac =

# Wenn Sie AAR-Dateien für die Abhängigkeiten Ihres Projekts verwenden, fügen Sie sie hier hinzu
# android.add_aars =

# Mindest-API für unterstütztes Android
android.minapi = 21

# Maximale unterstützte Android-API
android.maxapi = 33

# Ziel-SDK für die Erstellung
android.sdk = 33

# Architektur der Android-Anwendung (armeabi-v7a für 32 Bit, arm64-v8a für 64 Bit)
# android.archs = armeabi-v7a

# Aktivierung von Cython-Optimierungen
cython.optimize = 1

# Unterstützung für AOT-Python-Code hinzufügen
# android.aot = true

# Unterstützung für das Python-Tracing-Modul hinzufügen
# android.trace = true

# Verwenden Sie SDL2 nicht, wenn Sie spezielle Anforderungen an die Ereignisverwaltung haben oder spezielle Multimedia-Bibliotheken verwenden
# android.bootstrap = sdl2

# Verschiedene Build-Optionen
# android.ndk_api = 21
# android.logcat_filters = *:S python:D

# SDK et NDK paths
[buildozer]
android.sdk_path = /home/boubadiallo/.buildozer/android/platform/android-sdk
android.ndk_path = /home/boubadiallo/.buildozer/android/platform/android-ndk-r21e
