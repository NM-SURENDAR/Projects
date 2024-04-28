import pyperclip
import time
from urllib.parse import urlparse  # For basic URL validation
import requests
import os
API_KEY = os.environ.get("VIRUSTOTAL_API_KEY")
# Rest of  code using the API_KEY variable for VirusTotal API calls
BASE_URL = "https://www.virustotal.com/api/v3/urls"

def is_valid_url(url):
  """Checks if the provided string is a valid URL."""
  try:
    parsed_url = urlparse(url)
    return parsed_url.scheme and parsed_url.netloc
  except (ValueError, AttributeError):
    return False

def analyze_url(url):
  """Makes an API call to VirusTotal and analyzes the response."""
  headers = {"Authorization": f"Bearer {API_KEY}"}
  params = {"url": url}
  try:
    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()  # Raise an error for non-200 status codes

    # Extract data for notification (optional)
    data = response.json()
    positives = data.get("positives", 0)
    return f"Positives: {positives}"  # You can customize the report here
  except requests.exceptions.RequestException as e:
    return f"Error: {e}"

def main():
  prev_clipboard_content = None
  prev_report = None  # Store the analysis report for the previous URL

  while True:
    try:
      new_clipboard_content = pyperclip.waitForPaste()  # Wait for new content
      if new_clipboard_content:
        # Check if content is a valid URL
        if is_valid_url(new_clipboard_content):
          # Check if previous report exists for this URL (using cache)
          if prev_clipboard_content == new_clipboard_content and prev_report:
            print(f"Previously Analyzed - {prev_report}")  # Print report (optional)
          else:
            analysis_result = analyze_url(new_clipboard_content)
            print(f"Analysis Report:\n{analysis_result}")  # Print analysis report
            prev_report = analysis_result  # Update cache with new report
          prev_clipboard_content = new_clipboard_content  # Update previous content
        #else:
          # No need to notify about non-URL content (optional)
          # You can uncomment this if you want to inform about non-URLs
          # print(f"Copied Content: {new_clipboard_content} (Not a URL)")
    except KeyboardInterrupt:
      print("\nExiting program...")
      break

if __name__ == "__main__":
  # Make sure you have pyperclip and requests installed:
  # pip install pyperclip requests
  main()
