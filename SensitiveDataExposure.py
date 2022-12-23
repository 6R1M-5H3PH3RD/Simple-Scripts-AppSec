#This program uses regular expressions to search for hardcoded credentials, PII, IP address & URL from source code and log files

import re

def search_for_credentials(file_path):
  # Read the contents of the file
  with open(file_path, 'r') as f:
    contents = f.read()

  # Search for hardcoded credentials using regular expressions
  credential_patterns = [
    r'username[\s]*=[\s]*[\'\"](.+?)[\'\"]',
    r'password[\s]*=[\s]*[\'\"](.+?)[\'\"]',
    r'passwd[\s]*=[\s]*[\'\"](.+?)[\'\"]',
    r'secret[\s]*=[\s]*[\'\"](.+?)[\'\"]',
    r'access_key[\s]*=[\s]*[\'\"](.+?)[\'\"]',
    r'secret_key[\s]*=[\s]*[\'\"](.+?)[\'\"]'
  ]

  credentials = []
  for pattern in credential_patterns:
    matches = re.findall(pattern, contents)
    for match in matches:
      credentials.append(match)

  # Search for PII using regular expressions
  pii_patterns = [
    r'[\w\.-]+@[\w\.-]+',  # Email addresses
    r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',  # Phone numbers
    r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'  # IP addresses
  ]

  pii = []
  for pattern in pii_patterns:
    matches = re.findall(pattern, contents)
    for match in matches:
      pii.append(match)

  # Search for URLs using regular expressions
  url_patterns = [
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',  # URLs
  ]

  urls = []
  for pattern in url_patterns:
    matches = re.findall(pattern, contents)
    for match in matches:
      urls.append(match)

  # Print the results
  print('Hardcoded credentials:', credentials)
  print('PII:', pii)
  print('IP addresses:', ip_addresses)
  print('URLs:', urls)

# Test the function
search_for_credentials('/path/to/file.txt')
