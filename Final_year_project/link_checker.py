import pyperclip
import time
from urllib.parse import urlparse  # For basic URL validation
from win10toast import ToastNotifier  # For Windows 10 notifications

def is_valid_url(url):
  """Checks if the provided string is a valid URL."""
  try:
    parsed_url = urlparse(url)
    return parsed_url.scheme and parsed_url.netloc
  except (ValueError, AttributeError):
    return False

def notify(title, message, icon_path=None):  # Optional icon argument
  toaster = ToastNotifier()
  toaster.show_toast(title, message, icon_path=icon_path)

def main():
  prev_clipboard_content = None
  while True:
    try:
      new_clipboard_content = pyperclip.waitForPaste()  # Wait for new content
      if new_clipboard_content and new_clipboard_content != prev_clipboard_content:
        # Check if content is a valid URL
        if is_valid_url(new_clipboard_content):
          notify("Copied URL ",f"Its a URL")
        else:
          notify("Copied Content", f"Not a URL")
        prev_clipboard_content = new_clipboard_content
    except KeyboardInterrupt:
      print("\nExiting program...")
      break

if __name__ == "__main__":
  # Make sure you have pyperclip and win10toast installed:
  # pip install pyperclip win10toast
  main()
