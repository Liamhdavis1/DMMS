import sys

from PySide6.QtCore import Qt
from PySide6.QtNetwork import QTcpSocket
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class LedControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ESP32 LED Control")
        self.setMinimumSize(400, 240)

        # Default IP address of an ESP32 Access Point
        self.esp32_ip = "192.168.4.1"
        self.esp32_port = 5000

        self.socket = QTcpSocket(self)
        self.socket.connected.connect(self.on_connected)
        self.socket.disconnected.connect(self.on_disconnected)
        self.socket.readyRead.connect(self.on_ready_read)
        self.socket.errorOccurred.connect(self.on_error)

        self.status_label = QLabel("Not connected")
        self.status_label.setAlignment(Qt.AlignCenter)

        self.led_label = QLabel("LED state: Unknown")
        self.led_label.setAlignment(Qt.AlignCenter)

        self.connect_button = QPushButton("Connect to ESP32")
        self.connect_button.clicked.connect(self.connect_to_esp32)

        self.on_button = QPushButton("Turn LED ON")
        self.on_button.clicked.connect(self.send_led_on)

        self.off_button = QPushButton("Turn LED OFF")
        self.off_button.clicked.connect(self.send_led_off)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.on_button)
        button_layout.addWidget(self.off_button)

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.led_label)
        layout.addWidget(self.connect_button)
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def connect_to_esp32(self):
        self.status_label.setText(
            f"Connecting to {self.esp32_ip}:{self.esp32_port}..."
        )
        self.socket.connectToHost(self.esp32_ip, self.esp32_port)

    def send_led_on(self):
        self.send_command("LED_ON")

    def send_led_off(self):
        self.send_command("LED_OFF")

    def send_command(self, command):
        if self.socket.state() != QTcpSocket.SocketState.ConnectedState:
            self.status_label.setText("Not connected to ESP32")
            return

        self.socket.write(f"{command}\n".encode())
        self.status_label.setText(f"Sent: {command}")

    def on_connected(self):
        self.status_label.setText("Connected to ESP32")

    def on_disconnected(self):
        self.status_label.setText("Disconnected from ESP32")

    def on_ready_read(self):
        while self.socket.canReadLine():
            message = bytes(self.socket.readLine()).decode().strip()

            if message == "LED_IS_ON":
                self.led_label.setText("LED state: ON")
            elif message == "LED_IS_OFF":
                self.led_label.setText("LED state: OFF")

    def on_error(self, error):
        self.status_label.setText(f"Connection error: {self.socket.errorString()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LedControlWindow()
    window.show()
    sys.exit(app.exec())