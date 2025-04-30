"# captcha_python" 
##CAPTCHA Verification Application
A Python and Tkinter desktop app for text-based CAPTCHA verification. It shows a random string on a canvas with distortions and noise, letting users confirm they’re not bots.
#Features
6-character CAPTCHA (letters/digits) with text distortion, noise, and lines.
GUI with input field, "Verify" and "Refresh" buttons.
Enter key support for verification.
Success/error messages with auto-refresh on wrong attempts.
Uses only Python’s standard Tkinter library.
#Requirements
Python 3.6+
Tkinter
#Installation
Clone or download the repo:
git clone https://github.com/toshtosh08/captcha_python.git
Verify Tkinter:
python -m tkinter
A test window should pop up. On Linux, install Tkinter if needed:
sudo apt-get install python3-tk
#Usage
Go to the project folder:
cd <repository-directory>
Run the app:
python captcha_gui.py
Use the CAPTCHA:
See distorted text in the window.
Type it into the input field.
Click "Verify" or press Enter.
Correct: get a success message. Incorrect: new CAPTCHA loads.
Click "Refresh" for a new CAPTCHA.
#Code Structure
File: captcha_gui.py
Class: CaptchaApp
Sets up Tkinter UI.
Generates random CAPTCHA text.
Draws CAPTCHA with effects.
Manages verification/refresh.
Methods:
generate_captcha_text(): Makes random string.
draw_captcha(): Shows CAPTCHA with distortions.
verify_captcha(): Checks input.
refresh_captcha(): Creates new CAPTCHA.
#Troubleshooting
No Tkinter:
Check Python install.
Linux: sudo apt-get install python3-tk.
Window not appearing:
Look for terminal errors.
Confirm Tkinter is installed.
Input problems:
Click input field first.
CAPTCHA is case-insensitive.
#License Unlicensed, for educational use. Modify freely.
#Contact File a GitHub issue for questions or ideas.
