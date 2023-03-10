# AppSec-Simple-Python-Script-Collection
This repository is intended for educational use and contains scripts that may be useful for research.

## [SensitiveDataExposure.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SensitiveDataExposure.py)
- This program uses regular expressions to search for hardcoded credentials, PII, IP address & URL from source code and log files

## [SimpleSDEv2.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SimpleSDEv2.py)
- This is the complete program that searches for hardcoded credentials, PII, IP addresses, and URLs in source code files and log files with no extension in a given directory and its subdirectories, stores the results in an HTML table, removes duplicates, and provides the severity and confidence of each result.

## [SimpleSSTIDetector.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SimpleSSTIDetector.py)
- Server-side template injection (SSTI) is a type of vulnerability that occurs when an application processes user-supplied input as a template, allowing an attacker to inject arbitrary code into the template and execute it on the server.
- This code checks for common template tags and payloads that may indicate an SSTI vulnerability. 
- It uses regular expressions to search for the template tags and simple string comparisons to check for the payloads.
- Keep in mind that this is a very basic SSTI detector and may not detect all possible SSTI vulnerabilities. 
- It is important to thoroughly test and validate user input to prevent SSTI vulnerabilities in your application.

## [SimpleSensitiveDataExposure.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SimpleSensitiveDataExposure.py)
- This script will search for hardcoded credentials, PII, IP addresses, and URLs in all the files in the source_code_folder and its subfolders, using the regular expressions defined at the beginning of the script. If any of these are found, the script will write a row in the HTML table with the file name, line number, and the matching strings. The resulting HTML file can be opened in a web browser to view the results in a tabular format.

## [SimpleWebCrawler.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SimpleWebCrawler.py)
- This is example of an efficient web crawler in Python using the requests library, multithreading, and a breadth-first search algorithm.
- This code creates a queue of URLs to crawl and a thread pool with 4 threads. 
- Each thread takes a URL from the queue, crawls the page, extracts the links, and adds them to the queue.
- EUsing multithreading allows you to crawl multiple pages simultaneously, which can significantly speed up your crawler.
- The breadth-first search algorithm ensures that the crawler visits the pages in the order they are discovered, rather than going deep into one part of the website before visiting other parts.
- Keep in mind that you should always respect the website's terms of service and robots.txt file when web crawling, and be gentle by not sending too many requests too quickly. 
- You should also consider using a cache to store the results of your requests and a rotating proxy service to avoid getting blocked.

## [SimpleWebScrapper.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SimpleWebScrapper.py)
- This code creates a queue of URLs to scrape and a thread pool with 4 threads. 
- Each thread takes a URL from the queue, scrapes the page, and saves the data. 
- Using multithreading allows you to scrape multiple pages simultaneously, which can significantly speed up your scraper.
- Keep in mind that you should always respect the website's terms of service and robots.txt file when web scraping, and be gentle by not sending too many requests too quickly. 
- You should also consider using a cache to store the results of your requests and a rotating proxy service to avoid getting blocked.

## [URLfetcher.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/URLfetcher.py)
- This code creates a queue of URLs to crawl and a thread pool with 4 threads. 
- Each thread takes a URL from the queue, crawls the page, extracts the links from the HTML, and adds them to the queue.
- Using multithreading allows you to crawl multiple pages simultaneously, which can significantly speed up your crawler. 
- The breadth-first search algorithm ensures that the crawler visits the pages in the order they are discovered, rather than going deep into one part of the website before visiting other parts.
- Keep in mind that you should always respect the website's terms of service and robots.txt file when web crawling, and be gentle by not sending too many requests too quickly. 
- You should also consider using a cache to store the results of your requests and a rotating proxy service to avoid getting blocked.

## [XSSFinder.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/XSSFinder.py)
### To create an advanced XSS (Cross-Site Scripting) detector using Python, you can use a combination of regular expressions and HTML parsing to search for potential XSS vulnerabilities in a given website.

### Here is a high-level overview of the steps you can follow to create an advanced XSS detector:
- Import the necessary modules: To start, you will need to import the requests module to make HTTP requests to the website, and the re and html modules to work with regular expressions and parse HTML.
- Define a function to make an HTTP request to the website: This function should take in a URL and make an HTTP GET request to the website. It should return the HTML content of the website as a string.
- Define a function to parse the HTML content: This function should take in the HTML content of the website as a string and parse it using the html module. It should return a list of HTML elements that contain user-inputted data.
- Define a function to search for XSS vulnerabilities: This function should take in the list of HTML elements that contain user-inputted data and search for potential XSS vulnerabilities using a combination of regular expressions and HTML parsing. It should return a list of potential XSS vulnerabilities.
- Define the main function and put everything together: In the main function, you can prompt the user for the website URL and then call the other functions to make an HTTP request to the website, parse the HTML content, and search for XSS vulnerabilities. You can then print the list of potential XSS vulnerabilities to the console.
- Here is some sample code that illustrates how you can implement these steps:

### This is the complete program that searches for potential XSS vulnerabilities in a given website using a combination of regular expressions and HTML parsing. It prompts the user for the website URL, makes an HTTP request to the website, parses the HTML content, and searches for XSS vulnerabilities. 
- It then prints the list of potential XSS vulnerabilities to the console.
- If you want HTML table from the data/findings then uncomment the bottom code which will generate an HTML table from the data and store it in the html_table variable
## [SensitiveDataExposure.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SensitiveDataExposure.py)
- This program uses regular expressions to search for hardcoded credentials, PII, IP address & URL from source code and log files

## [SimpleSDEv2.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SimpleSDEv2.py)
- This is the complete program that searches for hardcoded credentials, PII, IP addresses, and URLs in source code files and log files with no extension in a given directory and its subdirectories, stores the results in an HTML table, removes duplicates, and provides the severity and confidence of each result.

## [SimpleSSTIDetector.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SimpleSSTIDetector.py)
- Server-side template injection (SSTI) is a type of vulnerability that occurs when an application processes user-supplied input as a template, allowing an attacker to inject arbitrary code into the template and execute it on the server.
- This code checks for common template tags and payloads that may indicate an SSTI vulnerability. 
- It uses regular expressions to search for the template tags and simple string comparisons to check for the payloads.
- Keep in mind that this is a very basic SSTI detector and may not detect all possible SSTI vulnerabilities. 
- It is important to thoroughly test and validate user input to prevent SSTI vulnerabilities in your application.

## [SimpleSensitiveDataExposure.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SimpleSensitiveDataExposure.py)
- This script will search for hardcoded credentials, PII, IP addresses, and URLs in all the files in the source_code_folder and its subfolders, using the regular expressions defined at the beginning of the script. If any of these are found, the script will write a row in the HTML table with the file name, line number, and the matching strings. The resulting HTML file can be opened in a web browser to view the results in a tabular format.

## [SimpleWebCrawler.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SimpleWebCrawler.py)
- This is example of an efficient web crawler in Python using the requests library, multithreading, and a breadth-first search algorithm.
- This code creates a queue of URLs to crawl and a thread pool with 4 threads. 
- Each thread takes a URL from the queue, crawls the page, extracts the links, and adds them to the queue.
- EUsing multithreading allows you to crawl multiple pages simultaneously, which can significantly speed up your crawler.
- The breadth-first search algorithm ensures that the crawler visits the pages in the order they are discovered, rather than going deep into one part of the website before visiting other parts.
- Keep in mind that you should always respect the website's terms of service and robots.txt file when web crawling, and be gentle by not sending too many requests too quickly. 
- You should also consider using a cache to store the results of your requests and a rotating proxy service to avoid getting blocked.

## [SimpleWebScrapper.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/SimpleWebScrapper.py)
- This code creates a queue of URLs to scrape and a thread pool with 4 threads. 
- Each thread takes a URL from the queue, scrapes the page, and saves the data. 
- Using multithreading allows you to scrape multiple pages simultaneously, which can significantly speed up your scraper.
- Keep in mind that you should always respect the website's terms of service and robots.txt file when web scraping, and be gentle by not sending too many requests too quickly. 
- You should also consider using a cache to store the results of your requests and a rotating proxy service to avoid getting blocked.

## [URLfetcher.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/URLfetcher.py)
- This code creates a queue of URLs to crawl and a thread pool with 4 threads. 
- Each thread takes a URL from the queue, crawls the page, extracts the links from the HTML, and adds them to the queue.
- Using multithreading allows you to crawl multiple pages simultaneously, which can significantly speed up your crawler. 
- The breadth-first search algorithm ensures that the crawler visits the pages in the order they are discovered, rather than going deep into one part of the website before visiting other parts.
- Keep in mind that you should always respect the website's terms of service and robots.txt file when web crawling, and be gentle by not sending too many requests too quickly. 
- You should also consider using a cache to store the results of your requests and a rotating proxy service to avoid getting blocked.

## [XSSFinder.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/XSSFinder.py)
### To create an advanced XSS (Cross-Site Scripting) detector using Python, you can use a combination of regular expressions and HTML parsing to search for potential XSS vulnerabilities in a given website.

### Here is a high-level overview of the steps you can follow to create an advanced XSS detector:
- Import the necessary modules: To start, you will need to import the requests module to make HTTP requests to the website, and the re and html modules to work with regular expressions and parse HTML.
- Define a function to make an HTTP request to the website: This function should take in a URL and make an HTTP GET request to the website. It should return the HTML content of the website as a string.
- Define a function to parse the HTML content: This function should take in the HTML content of the website as a string and parse it using the html module. It should return a list of HTML elements that contain user-inputted data.
- Define a function to search for XSS vulnerabilities: This function should take in the list of HTML elements that contain user-inputted data and search for potential XSS vulnerabilities using a combination of regular expressions and HTML parsing. It should return a list of potential XSS vulnerabilities.
- Define the main function and put everything together: In the main function, you can prompt the user for the website URL and then call the other functions to make an HTTP request to the website, parse the HTML content, and search for XSS vulnerabilities. You can then print the list of potential XSS vulnerabilities to the console.
- Here is some sample code that illustrates how you can implement these steps:

### This is the complete program that searches for potential XSS vulnerabilities in a given website using a combination of regular expressions and HTML parsing. It prompts the user for the website URL, makes an HTTP request to the website, parses the HTML content, and searches for XSS vulnerabilities. 
- It then prints the list of potential XSS vulnerabilities to the console.
- If you want HTML table from the data/findings then uncomment the bottom code which will generate an HTML table from the data and store it in the html_table variable.

## [BrokenAccessControl.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/BrokenAccessControl.py)
- This script uses the requests library to send a request to a given URL and check the response status code. 
- If the status code is 200 (which indicates a successful request), then the access control check is considered to have passed. 
- If the status code is anything other than 200, then the access control check is considered to have failed.
- You can modify this script to suit your specific needs. 
- For example, you could add additional checks to verify that the response headers or body contain the expected values, or you could add logic to handle different types of HTTP status codes.

### To detect broken access control, you can use a variety of techniques, such as:
1. Manual testing: You can manually test access control mechanisms by attempting to access restricted resources or functions using different combinations of user accounts, permissions, and input values.
2. Automated testing: You can use tools such as vulnerability scanners or web application firewalls to automatically test access control mechanisms and detect potential vulnerabilities.
3. Code review: You can review the code of your application to ensure that proper access control checks are in place and are being implemented correctly.
4. Log analysis: You can analyze logs of access to your application to identify any unauthorized access or attempts to access restricted resources.
5. Network monitoring: You can use network monitoring tools to detect and alert on any suspicious traffic that may indicate an attempt to bypass access control mechanisms.
### Overall, it is important to regularly test and monitor access control mechanisms to ensure that they are functioning correctly and are not being bypassed by attackers.

### To Do list for broken Access control script
1. Add additional checks: You can add additional checks to the script to verify that the response headers or body contain the expected values. For example, you could check for the presence of a specific header or for a particular string in the response body.
2. Handle different status codes: Currently, the script only checks for a status code of 200. You can modify the script to handle different status codes and perform different actions based on the code received. For example, you could check for a status code of 401 (unauthorized) to indicate that access control has failed.
3. Use authentication: If the resource you are trying to access requires authentication, you can modify the script to include authentication credentials. You can use the requests.auth module to handle basic authentication, or you can use an HTTP library such as http.client to handle more advanced authentication schemes.
4. Test multiple URL paths: You can modify the script to test multiple URL paths within the same domain, rather than just a single URL. This can help you identify any areas of the application where access control may be weaker.
5. Incorporate a data file: You can create a data file that contains a list of URLs to test, and modify the script to read from this file and test each URL in turn. This can make it easier to test a large number of URLs without having to modify the script itself.

### By adding these additional features, you can create a more comprehensive and advanced broken access control detection script.


## [PublicS3AccessibleBucets.py](https://github.com/6R1M-5H3PH3RD/Simple-Scripts-AppSec/blob/main/PublicS3AccessibleBucets.py)
### Python script for scanning publicly available S3 buckets:

- This script first connects to the S3 service using the boto3.client() function and initializes an empty list to store the names of publicly available buckets. It then uses the s3.list_buckets() function to list all of the buckets in the account and iterates through them.

- For each bucket, the script uses the s3.get_bucket_acl() function to get the permissions of the bucket and checks if the bucket has public read or write permissions using an if statement that checks the Permission and Grantee fields in the Grants list. If the bucket has public read or write permissions, it is added to the public_buckets list.

- The script then prints the names of the publicly available buckets, as well as their locations, versioning status, and contents. To do this, it uses the s3.get_bucket_location() and s3.get_bucket_versioning() functions to get the location and versioning status of each bucket, and the s3.list_objects() function to list the objects in the bucket.

- Finally, the script stores the result in HTML tabular format by constructing an HTML table using the names, locations, versioning status, and contents of the publicly available buckets.

### TODO:PublicS3AccessibleBucets.py
- This script can be modified to handle different types of permissions, such as "PublicWrite" or "PublicReadWrite", by adding additional conditions to the if statement that checks the Permission field. It can also be modified to check for specific grantees by modifying the if statement to compare the Grantee field with the desired grantee. Additionally, the script can be modified to check additional properties of the bucket, such as the bucket's location or versioning status, by adding additional functions or conditions to the if statements. Finally, the script can be modified to check the contents of the bucket for specific files or patterns by adding additional logic to iterate through the objects in the bucket and check for the desired files or patterns.

