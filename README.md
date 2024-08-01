# QR Code Generator App

A Django application for generating QR codes. This project uses the `qrcode` package to create QR codes from provided data and display them within a web interface.

## Features

- Generate QR codes from user-provided data
- Display generated QR codes on the web page
- Customize QR code size and error correction level

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.0 or higher

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

5. **Access the app:**

Open your web browser and navigate to `http://127.0.0.1:8000` to use the QR Code generator.

## Usage

1. **Navigate to the QR Code Generator page.**
2. **Enter the data you want to encode in the QR code.**
3. **Click on the "Generate" button to create the QR code.**
4. **View and download the generated QR code image.**

## Configuration

You can customize the QR code generation by modifying the `views.py` file in the `qr` app. The `qrcode` package settings can be adjusted to change the size, error correction level, and other parameters.

## Dependencies

- [Django](https://www.djangoproject.com/) - Web framework
- [qrcode](https://pypi.org/project/qrcode/) - Library for generating QR codes

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [qrcode](https://pypi.org/project/qrcode/) - For QR code generation
- [Django](https://www.djangoproject.com/) - For the web framework
