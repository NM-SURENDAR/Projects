import requests
from plyer import notification
import time
import clipboard
import re
import requests
from plyer import notification  # using plyer for notifications
from tkinter import * #using tkinter for UI
from tkinter.font import Font 
import threading #To control start and stop actions of a function
def is_url(text):
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(url_regex, text) is not None


def check_url_safety(url, api_key):
    api_url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': api_key, 'resource': url}
    try:
        response = requests.get(api_url, params=params)
        result = response.json()

        if 'response_code' not in result:
            raise KeyError("Response code not found in the API response.")
        
        if result['response_code'] == 0:
            notification_title = "URL Safety Check"
            notification_message = "The URL is not found in the VirusTotal database."
        else:
            positives = result.get('positives', 0)
            total = result.get('total', 0)
            if positives == 0:
                notification_title = "URL Safety Check"
                notification_message = " No detections found,This URL is clean and safe to visit. Enjoy browsing!"
            else:
                notification_title = "Potentially Harmful URL Detected"
                notification_message = f"MALICIOUS URL!--The URL is potentially harmful. Detected by {positives}/{total} scanners on VirusTotal."
        call_notofication(notification_title,notification_message)#calling a notification function
        # Send notification
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    api_key = "your api key"
    # url_to_check = 'https://www.google.com'
    previous_clipboard_content=None
    while not stop_event.is_set():
        current_clipboard_content=clipboard.paste()
        if current_clipboard_content!= previous_clipboard_content: 
            url=current_clipboard_content
            if is_url(url) is True: 
                check_url_safety(url, api_key)
        previous_clipboard_content=current_clipboard_content
        time.sleep(1)
def call_notofication(notification_title,notification_message):
    notification.notify(title=notification_title
    ,message=notification_message
    ,app_name='VirusTotal URL Checker'
    ,timeout=10 ) # Notification timeout in seconds)
#code for UI
#functions for start and stop buttons
stop_event=threading.Event()
def start_monitoring():
    threading.Thread(target=main).start()
    call_notofication("URL_SAFETY_CHECKER","STARTS RUNNING IN BACKGROUND")
def stop_monitoring():
    stop_event.set()
def stop_monitoring_and_exit():
    call_notofication("URL_SAFETY_CHECKER","STOPS RUNNING")
    stop_monitoring()
    root.destroy()
#
root =Tk()
root.configure(bg="light blue")
root.title("Welcome")
root.geometry("1366x768")
title_font = Font(family="Arial", size=40, weight="bold")
label1 = Label(root, text="URL SAFETY CHECKER", fg="blue", bg="light blue", font=title_font)
label1.place(x=683, y=40, anchor="center")
label2 = Label(root, text="URL Checker: Monitor Clipboard for URLs", fg="green", bg="light blue", font=("Arial", 20))
label2.place(x=683, y=300, anchor="center")
#buttons
button_font = Font(family="Arial", size=16, weight="bold")
bt1 = Button(root, text="START", bg="#25D366", fg="#ffffff", font=button_font, command=start_monitoring, padx=20, pady=10)
bt1.place(x=250,y=490)

bt2 = Button(root, text="STOP", bg="#25D366", fg="#ffffff", font=button_font, command=stop_monitoring_and_exit, padx=20, pady=10)
bt2.place(x=1000,y=490)
root.mainloop()
