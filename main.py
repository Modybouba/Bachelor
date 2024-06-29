from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import socket
import asyncio
from bleak import BleakClient, BleakScanner

# Lade die KV-Datei, die die Benutzeroberflächendefinition enthält
Builder.load_file("myarduino.kv")

# Warteschlange für asynchrone Aufrufe
async_call_queue = asyncio.Queue()

# Definition des Login-Bildschirms
class LoginScreen(Screen):
    # Methode zur Verbindung, um das Passwort zu überprüfen
    def connect(self, instance):
        password = self.ids.password_input.text
        if password == '1234':
            self.ids.result_label.text = 'Anmeldung erfolgreich!'  # Wenn das Passwort korrekt ist
            self.manager.current = 'main'  # Wechselt zum Hauptbildschirm
        else:
            self.ids.result_label.text = 'Falscher Code eingegeben.'  # Wenn das Passwort falsch ist

# Definition des Hauptbildschirms
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.bt_socket = None  # Initialisierung des Bluetooth-Sockets

    # Methode zum Trennen und Zurückkehren zum Login-Bildschirm
    def disconnect(self):
        self.manager.current = 'login'

    # Methode zum Einschalten der LED über WLAN
    def turn_on_led(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(('192.168.2.106', 12345))
            self.client_socket.sendall(b'1')
            print("LED über WLAN eingeschaltet")
        except Exception as e:
            print(f"Fehler beim Einschalten der LED über WLAN: {e}")

    # Methode zum Ausschalten der LED über WLAN
    def turn_off_led(self):
        try:
            self.client_socket.sendall(b'0')
            print("LED über WLAN ausgeschaltet")
            self.client_socket.close()
        except Exception as e:
            print(f"Fehler beim Ausschalten der LED über WLAN: {e}")

    # Coroutine zum Einschalten der LED über Bluetooth
    async def turn_on_led_bluetooth(self):
        try:
            print("Suche nach Geräten...")
            devices = await BleakScanner.discover()
            print(f"{len(devices)} Geräte gefunden.")

            device = next((d for d in devices if d.address == "58:DD:C3:C4:0A:24"), None)
            if device:
                print(f"Verbindung zum Gerät: {device}")
                async with BleakClient(device) as client:
                    print("Verbunden mit dem Gerät.")
                    await client.connect()
                    await client.write_gatt_char("19B10001-E8F2-537E-4F6C-D104768A1214", b'1')
                    print("LED über Bluetooth eingeschaltet")
            else:
                print("Bluetooth-Gerät nicht gefunden.")
        except Exception as e:
            print(f"Fehler beim Einschalten der LED über Bluetooth: {e}")

    # Coroutine zum Ausschalten der LED über Bluetooth
    async def turn_off_led_bluetooth(self):
        try:
            devices = await BleakScanner.discover()
            device = next((d for d in devices if d.address == "58:DD:C3:C4:0A:24"), None)
            if device:
                async with BleakClient(device) as client:
                    await client.connect()
                    await client.write_gatt_char("19B10001-E8F2-537E-4F6C-D104768A1214", b'0')
                    print("LED über Bluetooth ausgeschaltet")
            else:
                print("Bluetooth-Gerät nicht gefunden.")
        except Exception as e:
            print(f"Fehler beim Ausschalten der LED über Bluetooth: {e}")

    # Methode zum Hinzufügen eines asynchronen Aufrufs zur Warteschlange
    def add_async_call(self, coro_func):
        asyncio.ensure_future(async_call_queue.put(coro_func))

    # Methode zum Verarbeiten von asynchronen Aufrufen aus der Warteschlange
    async def process_async_calls(self):
        while True:
            coro_func = await async_call_queue.get()
            await coro_func()

    # Methode zum Aufrufen der Coroutine zum Einschalten der LED über Bluetooth
    def call_turn_on_led_bluetooth(self):
        self.add_async_call(self.turn_on_led_bluetooth)

    # Methode zum Aufrufen der Coroutine zum Ausschalten der LED über Bluetooth
    def call_turn_off_led_bluetooth(self):
        self.add_async_call(self.turn_off_led_bluetooth)

# Hauptklasse der Anwendung
class MyArduinoApp(App):
    def build(self):
        self.sm = ScreenManager()
        login_screen = LoginScreen(name='login')
        self.sm.add_widget(login_screen)
        main_screen = MainScreen(name='main')
        self.sm.add_widget(main_screen)
        return self.sm

    def on_start(self):
        asyncio.ensure_future(self.sm.get_screen('main').process_async_calls())

# Hauptprogramm
if __name__ == '__main__':
    MyArduinoApp().run()
