#This script uses the requests library to send a request to a given URL and check the response status code. If the status code is 200 (which indicates a successful request), then the access control check is considered to have passed. If the status code is anything other than 200, then the access control check is considered to have failed.
#You can modify this script to suit your specific needs. For example, you could add additional checks to verify that the response headers or body contain the expected values, or you could add logic to handle different types of HTTP status codes.
#This script now includes additional checks for the response status code, headers, and body, and it can handle basic HTTP authentication. 
#It also allows you to test multiple URL paths and read a list of URLs from a data file. You can modify this script further to suit your specific needs.

import requests

def check_access_control(url, headers, auth=None):
  # Send a request to the URL with the specified headers and authentication credentials
  r = requests.get(url, headers=headers, auth=auth)

  # Check the response status code and headers
  if r.status_code == 200:
    print(f'Access control check: PASSED for {url}')
  elif r.status_code == 401:
    print(f'Access control check: FAILED (401 Unauthorized) for {url}')
  else:
    print(f'Access control check: UNKNOWN for {url} (status code: {r.status_code})')

  # Check for the presence of a specific header
  if 'X-Custom-Header' in r.headers:
    print(f'Custom header found: {r.headers["X-Custom-Header"]}')
  else:
    print('Custom header not found')

  # Check for a specific string in the response body
  if 'expected string' in r.text:
    print('Expected string found in response body')
  else:
    print('Expected string not found in response body')

# Test the function with a few URLs and headers
urls = ['http://example.com/path1', 'http://example.com/path2']
headers = {'User-Agent': 'Mozilla/5.0'}
auth = requests.auth.HTTPBasicAuth('username', 'password')
for url in urls:
  check_access_control(url, headers, auth)

# Read URLs from a data file and test them
with open('urls.txt', 'r') as f:
  for url in f:
    check_access_control(url.strip(), headers, auth)

