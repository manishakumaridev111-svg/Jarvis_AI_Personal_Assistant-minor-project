from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
    QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextEdit, QSizePolicy)
from PyQt6.QtGui import QMovie, QFont
from PyQt6.QtCore import Qt, QSize, QThread, pyqtSignal
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Backend'))
from Chatbot import chat
from PyQt6.QtCore import QThread, pyqtSignal
from Backend.TextToSpeech import speak

class ResponseThread(QThread):
    response_ready = pyqtSignal(str)

    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        response = chat(self.text)
        self.response_ready.emit(response)


class MicThread(QThread):
    text_ready = pyqtSignal(str)

    def run(self):
        from SpeechToText import listen
        text = listen()
        if text:  # ← too indented!
            self.text_ready.emit(text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jarvis")

        self.setStyleSheet("QMainWindow { background-color: black; }")

        # Central widget + main vertical layout
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # --- GIF BACKGROUND LABEL ---
        self.gif_label = QLabel()
        self.gif_label.setScaledContents(False)
        self.gif_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.movie = QMovie("C:/Users/hi/Desktop/jarvis/Frontend/Graphics/Jarvis.gif")
        self.gif_label.setMovie(self.movie)
        print(self.movie.isValid())
        self.movie.start()
        self.gif_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # --- HEADLINE (overlaid on gif using absolute pos won't work with layout,
        #     so we stack using a container) ---
        gif_container = QWidget()
        gif_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        gif_container.setStyleSheet("background: transparent;")
        gif_stack = QVBoxLayout(gif_container)
        gif_stack.setContentsMargins(0, 0, 0, 0)

        headline = QLabel("JARVIS AI Voice Assistant")
        headline.setAlignment(Qt.AlignmentFlag.AlignCenter)
        headline.setFont(QFont("Consolas", 30))
        headline.setStyleSheet("color: #00cfff; background-color: transparent;")
        headline.setFixedHeight(60)

        gif_stack.addWidget(headline)
        gif_stack.addWidget(self.gif_label)

        # --- CHAT BOX ---
        self.chat_box = QTextEdit()
        self.chat_box.setReadOnly(True)
        self.chat_box.setFont(QFont("Consolas", 18))
        self.chat_box.setFixedHeight(300)
        self.chat_box.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.chat_box.setStyleSheet("""
            QTextEdit {
                background-color: #050505;
                color: #00cfff;
                border: none;
                padding: 10px;
            }
        """)
        self.chat_box.append("Jarvis: Hello! How can I assist you?")

        # --- INPUT ROW ---
        input_widget = QWidget()
        input_widget.setFixedHeight(50)
        input_widget.setStyleSheet("background-color: #030303;")
        input_row = QHBoxLayout(input_widget)
        input_row.setContentsMargins(10, 6, 10, 6)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type here...")
        self.input_box.setFont(QFont("Consolas", 16))
        self.input_box.setStyleSheet("""
            QLineEdit {
                background-color: #0d0d0d;
                color: #00cfff;
                border: 1px solid #00cfff;
                border-radius: 14px;
                padding: 6px 14px;
            }
        """)
        self.input_box.returnPressed.connect(self.send_message)

        send_btn = QPushButton("Send")
        send_btn.setFixedSize(80, 40)
        send_btn.setStyleSheet("""
            QPushButton {
                background-color: #00cfff;
                color: black;
                border-radius: 14px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #80e8ff; }
        """)
        send_btn.clicked.connect(self.send_message)

        mic_btn = QPushButton("🎤")
        mic_btn.setFixedSize(50, 35)
        mic_btn.setStyleSheet("""
            QPushButton {
                background-color: #00cfff;
                border-radius: 14px;
                font-size: 16px;
            }
        """)
        mic_btn.clicked.connect(self.listen_voice)

        input_row.addWidget(self.input_box)
        input_row.addWidget(send_btn)
        input_row.addWidget(mic_btn)

        # Assemble main layout
        main_layout.addWidget(gif_container)   # stretches
        main_layout.addWidget(self.chat_box)
        main_layout.addWidget(input_widget)

    def send_message(self):
        text = self.input_box.text().strip()
        if not text:
            return
        self.chat_box.append(f"You: {text}")
        self.input_box.clear()
        self.thread = ResponseThread(text)
        self.thread.response_ready.connect(lambda r: self.handle_response(r))
        self.thread.start()

    def handle_response(self, r):
        self.chat_box.append(f"Jarvis: {r}\n")
        speak(r)

    def listen_voice(self):
        self.chat_box.append("Jarvis: Listening...")
        self.mic_thread = MicThread()
        self.mic_thread.text_ready.connect(self.input_box.setText)
        self.mic_thread.text_ready.connect(lambda: self.send_message())
        self.mic_thread.start()

app = QApplication(sys.argv)
window = MainWindow()
window.showFullScreen()
sys.exit(app.exec())