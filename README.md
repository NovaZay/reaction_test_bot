# 🖱️ Auto-Clicker

Automates mouse clicks on a specific screen pixel when it changes to a green color. Perfect for repetitive tasks, games, or pixel-based detection.

---

## 📑 Table of Contents

- 📌 [Introduction](#-introduction)  
- 📦 [Requirements](#-requirements)  
- ⚙️ [Installation](#️-installation)  
- 🚀 [Usage](#-usage)  
- 🛠️ [Configuration](#-configuration)  
- 🔍 [How It Works](#-how-it-works)  
- ❓ [Troubleshooting](#-troubleshooting)  
- 🛑 [Stopping the Script](#-stopping-the-script)  
- 📝 [License](#-license)  
- 🤝 [Contributing](#-contributing)  
- 👤 [Author](#-author)  
- 🙏 [Acknowledgments](#-acknowledgments)  

---

## 📌 Introduction

This is a simple Python script that uses the `pyautogui` library to automatically click a specific screen location when a certain pixel turns green. It’s useful for automating visual-based interactions.

---

## 📦 Requirements

- Python 3.x (tested on Python 3.8 and 3.9)  
- [`pyautogui`](https://pypi.org/project/pyautogui/) (`pip install pyautogui`)  
- [`keyboard`](https://pypi.org/project/keyboard/) (`pip install keyboard`)  
- A computer with a screen (obviously!)

---

## ⚙️ Installation

1. Download and install Python from [python.org](https://www.python.org/).  
2. Open your terminal or command prompt and install the required libraries:

   ```bash
   pip install pyautogui keyboard
   ```

3. Clone this repository or download the `auto_clicker.py` script manually.

---

## 🚀 Usage

Run the script with:

```bash
python auto_clicker.py
```

- The script will start monitoring the target pixel.
- Once it detects the pixel has turned green, it will automatically perform a mouse click.

---

## 🛠️ Configuration

- **Stop key:** `"F10"` by default

You can customize these settings by editing the following variables in the script:

```python
stop_key = 'F10'
```

---

## 🔍 How It Works

1. Takes a screenshot of the screen using `pyautogui`.  
2. Retrieves the color of the pixel at the specified coordinates.  
3. Compares the pixel’s RGB color with the target green color.  
4. If it matches, performs a mouse click at the specified position.  
5. Continues running until the user presses the configured stop key.

---

## ❓ Troubleshooting

- Make sure the pixel position exactly matches the area you want to monitor.  
- Use a color picker tool to get the exact RGB value for your target pixel.  
- Try increasing the delay between checks if the script is too fast or unresponsive.  
- Still having issues? Add debug prints or try running with a `-d` flag if supported:

```bash
python auto_clicker.py -d
```

---

## 🛑 Stopping the Script

To stop the script safely, press the key configured in the `stop_key` variable (default is `'F10'`).  
The script listens for this key in the background and exits gracefully when pressed.

---

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing

Contributions are welcome!  
If you'd like to improve or extend the project, fork the repository and submit a pull request.  
Be sure to include a clear description of your changes and any relevant tests or documentation.

---

## 👤 Author

NovaZay

---

## 🙏 Acknowledgments

- [`pyautogui`](https://github.com/asweigart/pyautogui) by Al Sweigart  
- [`keyboard`](https://github.com/boppreh/keyboard) by Bastian Raschke  

---
