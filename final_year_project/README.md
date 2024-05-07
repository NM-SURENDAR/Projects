

# URL Safety Checker

## Overview
The URL Safety Checker is a Python application designed to monitor URLs copied to the clipboard and check their safety using the VirusTotal API. It provides real-time notifications about the safety status of URLs, helping users avoid potentially harmful websites.

## Features
- **URL Monitoring**: Constantly monitors the clipboard for copied URLs.
- **URL Safety Check**: Utilizes the VirusTotal API to check the safety of the copied URLs.
- **Real-time Notifications**: Provides notifications about the safety status of URLs, alerting users to potential threats.
- **User Interface**: Includes a simple graphical user interface (GUI) for starting and stopping the monitoring process.

## Requirements
- Python 3.x
- Required Python packages:
  - requests
  - plyer
  - tkinter

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/url-safety-checker.git
   ```
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Obtain a VirusTotal API key and replace `"your api key"` in the code with your actual API key.

## Usage
1. Run the application by executing the `main.py` file.
2. Click the "START" button to begin monitoring the clipboard for URLs.
3. URLs copied to the clipboard will be automatically checked for safety.
4. Real-time notifications will alert you to the safety status of the URLs.
5. Click the "STOP" button to stop monitoring and exit the application.

## Note
- Ensure that your VirusTotal API key is kept secure and not shared publicly.
- This application is for educational purposes and should be used responsible.
