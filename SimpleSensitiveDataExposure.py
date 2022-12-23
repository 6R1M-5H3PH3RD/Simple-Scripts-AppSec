#Python program that can search for hardcoded credentials, personally identifiable information (PII), IP addresses, and URLs in source code files and log files recursively, and generate an HTML report with the results
#This script will search for hardcoded credentials, PII, IP addresses, and URLs in all the files in the source_code_folder and its subfolders, using the regular expressions defined at the beginning of the script. If any of these are found, the script will write a row in the HTML table with the file name, line number, and the matching strings. The resulting HTML file can be opened in a web browser to view the results in a tabular format.

import os
import re
import html

# Regular expressions for detecting hardcoded credentials, PII, IP addresses, and URLs
credential_pattern = re.compile(r'username[\s]*:[\s]*[\S]+[\s]*,[\s]*password[\s]*:[\s]*[\S]+')
pii_pattern = re.compile(r'(?:(?:[^\s,]+@[^\s,]+\.[^\s,]+)|(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))')
ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')

# Create an HTML file to store the results
html_file = open('results.html', 'w')

# Write the HTML header
html_file.write('<html>\n')
html_file.write('<head>\n')
html_file.write('<style>\n')
html_file.write('table, th, td {\n')
html_file.write('border: 1px solid black;\n')
html_file.write('border-collapse: collapse;\n')
html_file.write('}\n')
html_file.write('th, td {\n')
html_file.write('padding: 5px;\n')
html_file.write('}\n')
html_file.write('</style>\n')
html_file.write('</head>\n')
html_file.write('<body>\n')
html_file.write('<table>\n')
html_file.write('<tr>\n')
html_file.write('<th>File</th>\n')
html_file.write('<th>Line Number</th>\n')
html_file.write('<th>Hardcoded Credentials</th>\n')
html_file.write('<th>PII</th>\n')
html_file.write('<th>IP Address</th>\n')
html_file.write('<th>URL</th>\n')
html_file.write('</tr>\n')

# Recursively search through the source code folder and its subfolders
for root, dirs, files in os.walk('source_code_folder'):
    for file in files:
        # Open the file
        f = open(os.path.join(root, file), 'r')

        # Read the file line by line

        line_number = 0
        for line in f:
            line_number += 1

            # Search for hardcoded credentials, PII, IP addresses, and URLs in the line
            credentials = credential_pattern.findall(line)
            pii = pii_pattern.findall(line)
            ip_addresses = ip_pattern.findall(line)
            urls = url_pattern.findall(line)

            # If any of these are found, write a row in the HTML table with the file name, line number, and the matching strings
            if credentials or pii or ip_addresses or urls:
                html_file.write('<tr>\n')
                html_file.write('<td>' + os.path.join(root, file) + '</td>\n')
                html_file.write('<td>' + str(line_number) + '</td>\n')
                html_file.write('<td>' + ', '.join(credentials) + '</td>\n')
                html_file.write('<td>' + ', '.join(pii) + '</td>\n')
                html_file.write('<td>' + ', '.join(ip_addresses) + '</td>\n')
                html_file.write('<td>' + ', '.join(urls) + '</td>\n')
                html_file.write('</tr>\n')

# Close the HTML file
html_file.write('</table>\n')
html_file.write('</body>\n')
html_file.write('</html>\n')
html_file.close()

