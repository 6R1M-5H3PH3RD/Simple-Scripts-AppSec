#This code creates a queue of URLs to crawl and a thread pool with 4 threads. 
#Each thread takes a URL from the queue, crawls the page, extracts the links from the HTML, and adds them to the queue.
#Using multithreading allows you to crawl multiple pages simultaneously, which can significantly speed up your crawler. 
#The breadth-first search algorithm ensures that the crawler visits the pages in the order they are discovered, rather than going deep into one part of the website before visiting other parts.
#Keep in mind that you should always respect the website's terms of service and robots.txt file when web crawling, and be gentle by not sending too many requests too quickly. 
#You should also consider using a cache to store the results of your requests and a rotating proxy service to avoid getting blocked.


from bs4 import BeautifulSoup
import requests
from queue import Queue

# Set of visited URLs
visited = set()

# Function to crawl a single page
def crawl_page(url):
    # Make the request and parse the response
    response = requests.get(url)
    html = response.text
    # Parse the HTML with Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")
    # Find all the links in the HTML
    links = soup.find_all("a")
    # Extract the URLs from the links
    urls = [link.get("href") for link in links]
    # Add the current URL to the set of visited URLs
    visited.add(url)
    # Add the extracted URLs to the queue
    for url in urls:
        if url not in visited:
            url_queue.put(url)

# Function to handle threading
def handle_threading(url_queue):
    while True:
        # Get the next URL from the queue
        url = url_queue.get()
        # Crawl the page
        crawl_page(url)
        # Mark the task as done
        url_queue.task_done()

# Create a queue to hold the URLs
url_queue = Queue()

# Add the starting URL to the queue
url_queue.put("https://example.com")

# Create a thread pool with 4 threads
for i in range(4):
    thread = threading.Thread(target=handle_threading, args=(url_queue,))
    thread.daemon = True
    thread.start()

# Wait for all tasks to be completed
url_queue.join()
