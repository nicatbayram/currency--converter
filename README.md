# Currency Converter

A sleek and user-friendly currency conversion application developed with PyQt6. The application uses the ExchangeRate API for real-time exchange rates.

<img width="400" alt="1" src="https://github.com/user-attachments/assets/321beb5b-cc07-4818-9d91-ed14a84a4163" />
<img width="400" alt="2" src="https://github.com/user-attachments/assets/bddec307-2eee-411c-ad26-8c437f30819c" />



## Features

- Modern and responsive user interface
- Real-time currency exchange rate updates
- Animated UI elements
- Support for 12 different currencies
- Shadow effects and gradient background
- Error handling and user feedback

## Requirements

- Python 3.6 or higher
- PyQt6
- requests

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nicatbayram/currency--converter.git
cd currency--converter
```

2. Install required packages:
```bash
pip install PyQt6 requests
```

3. Get ExchangeRate API key:
- Visit [ExchangeRate-API](https://www.exchangerate-api.com/)
- Create a free account
- Get your API key
- Update the `api_key` variable in the `ModernCurrencyConverter` class with your API key

## Usage

To start the application:

```bash
python main.py
```

To convert currency:

1. Enter the amount you want to convert
2. Select the source currency
3. Select the target currency
4. Click the "Convert" button

## Supported Currencies

- USD (United States Dollar)
- EUR (Euro)
- GBP (British Pound Sterling)
- JPY (Japanese Yen)
- AUD (Australian Dollar)
- CAD (Canadian Dollar)
- CHF (Swiss Franc)
- CNY (Chinese Yuan)
- INR (Indian Rupee)
- SGD (Singapore Dollar)
- TRY (Turkish Lira)
- AZN (Azerbaijani Manat)

## Customization

You can modify the CSS styles in the `apply_styles()` method to change the application's appearance. Colors used in the current theme:

- Background: #2C3E50 to #3498DB (gradient)
- Convert button: #27AE60
- Text colors: #2C3E50 (dark), #7F8C8D (light)

## Code Structure

```python
class CurrencyWidget(QFrame):
    # Handles currency selection widgets with shadow effects
    
class ModernCurrencyConverter(QMainWindow):
    # Main application window with the following methods:
    # - initUI(): Sets up the user interface
    # - setup_animations(): Configures UI animations
    # - load_currencies(): Populates currency options
    # - convert_currency(): Handles conversion logic
    # - apply_styles(): Applies CSS styling
```

## Error Handling

The application includes error handling for:
- Invalid input amounts
- API connection issues
- Invalid currency selections


## Contributing

1. Fork the repository
2. Create your Feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments

- [ExchangeRate-API](https://www.exchangerate-api.com/) for providing exchange rate data
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) for the UI framework

## Development

To modify the application:

1. Update currency list:
```python
currencies = [
    "USD", "EUR", "GBP", # Add more currencies here
]
```

2. Modify UI styles:
```python
self.setStyleSheet("""
    # Update styles here
""")
```

3. Add new features:
- Extend the `ModernCurrencyConverter` class
- Add new widgets to the UI
- Implement additional currency conversion features


