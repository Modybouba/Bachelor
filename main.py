from kivy.config import Config  # Importiere die Konfigurationsklasse von Kivy

# Set multisamples to 0
Config.set('graphics', 'multisamples', '0')  # Setze die Multisampling-Einstellung auf 0

from kivy.app import App  # Importiere die Hauptklasse der Kivy-Anwendung
from kivy.lang import Builder  # Importiere das Builder-Modul für die KV-Dateiverarbeitung
import socket  # Importiere das Socket-Modul für Netzwerkoperationen
from kivy.uix.screenmanager import ScreenManager, Screen


# Load the KV file
Builder.load_file("myarduino.kv")  # Lade die KV-Datei für das Design der Benutzeroberfläche

class LoginScreen(Screen):  # Definition der Klasse für den Anmeldebildschirm
    def connect(self, instance):  # Methode zum Verbinden, wenn die Anmeldetaste gedrückt wird
        password = (self.ids.password_input.
                    text)  # Abrufen des eingegebenen Passworts
        if password == '1234':  # Überprüfen, ob das Passwort korrekt ist
            self.ids.result_label.text = 'Anmeldung erfolgreich!'  # Setzen des Erfolgsmeldungstextes
            self.manager.current = 'main'  # Wechsel zum Hauptbildschirm
        else:
            self.ids.result_label.text = 'Falscher Code eingegeben.'  # Setzen des Fehlermeldungstextes

class MainScreen(Screen):  # Definition der Klasse für den Hauptbildschirm
    def disconnect(self):  # Methode zum Trennen der Verbindung
        self.manager.current = 'login'  # Wechsel zurück zum Anmeldebildschirm

    def turn_on_led(self):  # Methode zum Einschalten der LED über WLAN
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Socket erstellen
            self.client_socket.connect(('192.168.2.105', 12345))  # Verbindung zum Arduino herstellen
            self.client_socket.sendall(b'1')  # Befehl zum Einschalten der LED senden
            print("LED turned on via Wi-Fi")  # Ausgabe, dass die LED über WLAN eingeschaltet wurde
        except Exception as e:
            print(f"Error turning on LED via Wi-Fi: {e}")  # Fehlerbehandlung für das Einschalten über WLAN

    def turn_off_led(self):  # Methode zum Ausschalten der LED über WLAN
        try:
            self.client_socket.sendall(b'0')  # Befehl zum Ausschalten der LED senden
            print("LED turned off via Wi-Fi")  # Ausgabe, dass die LED über WLAN ausgeschaltet wurde
            self.client_socket.close()  # Socket-Verbindung schließen
        except Exception as e:
            print(f"Error turning off LED via Wi-Fi: {e}")  # Fehlerbehandlung für das Ausschalten über WLAN

    def connect_wifi(self):  # Methode zum Verbinden über WLAN
        try:
            print("Trying to connect via Wi-Fi")
            arduino_ip = '192.168.2.105'
            arduino_port = 12345
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((arduino_ip, arduino_port))
            print("Connected via Wi-Fi")
            client_socket.sendall(b'Hello Arduino!')
            data = client_socket.recv(1024)
            print("Received data from Arduino:", data)
            client_socket.close()
        except Exception as e:
            print(f"Error connecting via Wi-Fi: {e}")

class MyArduinoApp(App):  # Hauptklasse der Kivy-Anwendung
    def build(self):  # Methode zum Erstellen des App-Layouts
        self.sm = ScreenManager()  # Screen-Manager-Instanz erstellen
        login_screen = LoginScreen(name='login')  # Anmeldebildschirm erstellen
        self.sm.add_widget(login_screen)  # Anmeldebildschirm zur Screen-Manager hinzufügen
        main_screen = MainScreen(name='main')  # Hauptbildschirm erstellen
        self.sm.add_widget(main_screen)  # Hauptbildschirm zur Screen-Manager hinzufügen
        return self.sm  # Rückgabe des Screen-Managers für den App-Build-Prozess

if __name__ == '__main__':  # Überprüfen, ob das Skript direkt ausgeführt wird
    MyArduinoApp().run()  # Starten der Kivy-Anwendung
