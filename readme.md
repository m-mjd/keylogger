# Keylogger

## Description

The Keylogger is a Python application that captures and logs keystrokes. It uses the `pynput` library to listen for keyboard events and logs the captured keystrokes along with the system's hardware information.

## Features

- Logs keystrokes in real-time
- Captures and displays system information including:
  - Computer name
  - Operating system and version
  - CPU information
  - Total RAM
  - Total hard disk space

## Requirements

- Python 3.x
- `pynput` module
- `psutil` module

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/m-mjd/keylogger.git
   cd keylogger
   ```

2. **Install the required packages:**

   ```bash
   pip install pynput psutil
   ```

3. **Run the application:**

   ```bash
   python keylogger.py
   ```

## Usage

1. Launch the application.
2. The application will start logging keystrokes and display them in the console.
3. System information will be displayed when the application starts.

## Code Overview

- `computer_info`: Dictionary storing system information using `platform` and `psutil` modules.
- `on_press`: Function to capture and print keystrokes.
  - Tries to log the character of the key if available.
  - Logs the key name for special keys (like Shift, Ctrl, etc.).
- `Listener`: Pynput's Listener to monitor keyboard events and trigger `on_press`.

## License

This project is licensed under the MIT License.

---

# کیلاگر

## توضیحات

کیلاگر یک برنامه پایتون است که ضربه‌های کلید را ضبط و ثبت می‌کند. این برنامه از کتابخانه `pynput` برای شنیدن رویدادهای صفحه‌کلید استفاده می‌کند و ضربه‌های کلید را همراه با اطلاعات سخت‌افزاری سیستم ثبت می‌کند.

## ویژگی‌ها

- ثبت ضربه‌های کلید در زمان واقعی
- ضبط و نمایش اطلاعات سیستم شامل:
  - نام کامپیوتر
  - سیستم عامل و نسخه آن
  - اطلاعات CPU
  - کل RAM
  - فضای کل دیسک سخت

## نیازمندی‌ها

- Python 3.x
- ماژول `pynput`
- ماژول `psutil`

## نصب

1. **کلون کردن مخزن:**

   ```bash
   git clone https://github.com/m-mjd/keylogger.git
   cd keylogger
   ```

2. **نصب پکیج‌های مورد نیاز:**

   ```bash
   pip install pynput psutil
   ```

3. **اجرای برنامه:**

   ```bash
   python keylogger.py
   ```

## استفاده

1. برنامه را راه‌اندازی کنید.
2. برنامه شروع به ثبت ضربه‌های کلید کرده و آنها را در کنسول نمایش می‌دهد.
3. اطلاعات سیستم در زمان شروع برنامه نمایش داده می‌شود.

## مرور کد

- `computer_info`: دیکشنری ذخیره‌سازی اطلاعات سیستم با استفاده از ماژول‌های `platform` و `psutil`.
- `on_press`: تابعی برای ضبط و چاپ ضربه‌های کلید.
  - تلاش برای ثبت کاراکتر کلید در صورت وجود.
  - ثبت نام کلید برای کلیدهای خاص (مانند Shift، Ctrl و غیره).
- `Listener`: شنونده Pynput برای نظارت بر رویدادهای صفحه‌کلید و اجرای `on_press`.

## مجوز

این پروژه تحت مجوز MIT است.
