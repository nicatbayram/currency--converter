import sys
import requests
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLineEdit, QComboBox, QPushButton, 
                            QLabel, QGraphicsDropShadowEffect, QFrame)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, QTimer
from PyQt6.QtGui import QColor, QIcon, QLinearGradient, QPalette, QFont
from pathlib import Path

class CurrencyWidget(QFrame):
    def __init__(self, label_text, parent=None):
        super().__init__(parent)
        self.setObjectName("currencyWidget")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        
        label = QLabel(label_text)
        label.setObjectName("fieldLabel")
        
        self.combo = QComboBox()
        self.combo.setObjectName("currencyCombo")
        self.combo.setFixedHeight(45)
        
        layout.addWidget(label)
        layout.addWidget(self.combo)
        
        # Add shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 50))
        shadow.setOffset(0, 2)
        self.setGraphicsEffect(shadow)

class ModernCurrencyConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.api_key = ""  # Get free from https://www.exchangerate-api.com/
        self.base_url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/"
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Modern Currency Converter')
        self.setMinimumSize(600, 700)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Header
        header = QLabel("Currency Converter")
        header.setObjectName("header")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)
        
        # Amount input
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")
        self.amount_input.setObjectName("amountInput")
        self.amount_input.setFixedHeight(45)
        layout.addWidget(self.amount_input)
        
        # Currency selection widgets
        self.from_currency = CurrencyWidget("From Currency")
        self.to_currency = CurrencyWidget("To Currency")
        
        # Currency layout
        currencies_layout = QHBoxLayout()
        currencies_layout.addWidget(self.from_currency)
        currencies_layout.addWidget(self.to_currency)
        layout.addLayout(currencies_layout)
        
        # Convert button
        self.convert_btn = QPushButton("Convert")
        self.convert_btn.setObjectName("convertButton")
        self.convert_btn.setFixedHeight(50)
        self.convert_btn.clicked.connect(self.convert_currency)
        layout.addWidget(self.convert_btn)
        
        # Result display
        self.result_frame = QFrame()
        self.result_frame.setObjectName("resultFrame")
        result_layout = QVBoxLayout(self.result_frame)
        
        self.result_label = QLabel()
        self.result_label.setObjectName("resultLabel")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_layout.addWidget(self.result_label)
        
        self.update_time = QLabel()
        self.update_time.setObjectName("updateTime")
        self.update_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_layout.addWidget(self.update_time)
        
        layout.addWidget(self.result_frame)
        
        # Add stretches for better spacing
        layout.addStretch()
        
        # Load currencies and apply styles
        self.load_currencies()
        self.apply_styles()
        
        # Setup animations
        self.setup_animations()

    def setup_animations(self):
        # Button hover animation
        self.convert_btn.enterEvent = lambda e: self.animate_button(True)
        self.convert_btn.leaveEvent = lambda e: self.animate_button(False)
        
        # Result frame animation
        self.result_animation = QPropertyAnimation(self.result_frame, b"geometry")
        self.result_animation.setDuration(300)
        self.result_animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    def animate_button(self, hover):
        animation = QPropertyAnimation(self.convert_btn, b"pos")
        animation.setDuration(100)
        current_pos = self.convert_btn.pos()
        
        if hover:
            animation.setEndValue(QPoint(current_pos.x(), current_pos.y() - 2))
        else:
            animation.setEndValue(QPoint(current_pos.x(), current_pos.y()))
            
        animation.start()

    def load_currencies(self):
        currencies = [
            "USD", "EUR", "GBP", "JPY", "AUD", "CAD", 
            "CHF", "CNY", "INR", "SGD", "TRY", "AZN"
        ]
        
        for currency in currencies:
            self.from_currency.combo.addItem(currency)
            self.to_currency.combo.addItem(currency)
            
        self.from_currency.combo.setCurrentText("USD")
        self.to_currency.combo.setCurrentText("EUR")

    def convert_currency(self):
        try:
            amount = float(self.amount_input.text())
            from_curr = self.from_currency.combo.currentText()
            to_curr = self.to_currency.combo.currentText()
            
            response = requests.get(f"{self.base_url}{from_curr}")
            data = response.json()
            rate = data["conversion_rates"][to_curr]
            
            converted = amount * rate
            self.result_label.setText(f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}")
            self.update_time.setText(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Animate result frame
            self.result_animation.start()
            
        except ValueError:
            self.result_label.setText("Please enter a valid amount")
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")

    def apply_styles(self):
        # Define the stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                          stop:0 #2C3E50, stop:1 #3498DB);
            }
            
            QLabel#header {
                color: white;
                font-size: 32px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            
            QLineEdit#amountInput {
                background: rgba(255, 255, 255, 0.9);
                border: none;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
                color: #2C3E50;
            }
            
            #currencyWidget {
                background: rgba(255, 255, 255, 0.9);
                border-radius: 8px;
                padding: 10px;
            }
            
            #fieldLabel {
                color: #2C3E50;
                font-size: 14px;
                font-weight: bold;
            }
            
            QComboBox#currencyCombo {
                background: white;
                border: none;
                border-radius: 4px;
                padding: 5px;
                font-size: 16px;
                color: #2C3E50;
            }
            
            QComboBox#currencyCombo::drop-down {
                border: none;
                padding-right: 10px;
            }
            
            QPushButton#convertButton {
                background: #27AE60;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
                padding: 10px;
            }
            
            QPushButton#convertButton:hover {
                background: #2ECC71;
            }
            
            #resultFrame {
                background: rgba(255, 255, 255, 0.9);
                border-radius: 8px;
                padding: 20px;
                margin-top: 20px;
            }
            
            #resultLabel {
                color: #2C3E50;
                font-size: 24px;
                font-weight: bold;
            }
            
            #updateTime {
                color: #7F8C8D;
                font-size: 12px;
                margin-top: 10px;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Use Fusion style for better cross-platform consistency
    
    # Set default font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    converter = ModernCurrencyConverter()
    converter.show()
    sys.exit(app.exec())
