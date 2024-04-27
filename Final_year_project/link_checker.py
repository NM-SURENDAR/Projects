import pyperclip
import time
from urllib.parse import urlparse  # For basic URL validation

def is_valid_url(url):
  """Checks if the provided string is a valid URL."""
  try:
    parsed_url = urlparse(url)
    return parsed_url.scheme and parsed_url.netloc
  except (ValueError, AttributeError):
    return False

def main():
  prev_clipboard_content = None  # Store previous content
  while True:
    try:
      new_clipboard_content = pyperclip.waitForPaste()  # Wait for new content
      if new_clipboard_content and new_clipboard_content != prev_clipboard_content:
        # Check if content is a valid URL
        if is_valid_url(new_clipboard_content):
          print(f"Copied content is a URL: {new_clipboard_content}")
        else:
          print(f"Copied content is not a URL: {new_clipboard_content}")
        prev_clipboard_content = new_clipboard_content  # Update previous content
    except KeyboardInterrupt:
      print("\nExiting program...")
      break

if __name__ == "__main__":
  main()
