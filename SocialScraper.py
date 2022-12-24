#Example of how you could write a Python script that scrapes data from LinkedIn, Twitter, and Facebook and stores the results in an HTML table.
#First, you will need to install the BeautifulSoup and requests Python libraries, which are used for parsing HTML and making HTTP requests, respectively. 
# To get the output in tabular format uncomment generate_html_table() function at the bottom
#You can install them using the following commands
#pip install beautifulsoup4
#pip install requests
#Next, you will need to import the necessary modules and define three functions, one for each website, that take a URL as an argument and return the data you are interested in. 



from bs4 import BeautifulSoup
import requests

def scrape_linkedin_profile(url):
    # Make a GET request to the LinkedIn profile page
    response = requests.get(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the element containing the name of the person
    name_element = soup.find('h1', {'class': 'pv-top-card-section__name'})
    # Extract the text of the element
    name = name_element.text
    # Find the element containing the job title of the person
    title_element = soup.find('h2', {'class': 'pv-top-card-section__headline'})
    # Extract the text of the element
    title = title_element.text
    # Return the name and title as a tuple
    return (name, title)

def scrape_twitter_profile(url):
    # Make a GET request to the Twitter profile page
    response = requests.get(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the element containing the name of the person
    name_element = soup.find('h1', {'class': 'ProfileHeaderCard-name'})
    # Extract the text of the element
    name = name_element.text
    # Find the element containing the username of the person
    username_element = soup.find('span', {'class': 'ProfileHeaderCard-screennameLink u-linkComplex js-nav'})
    # Extract the text of the element
    username = username_element.text
    # Return the name and username as a tuple
    return (name, username)

def scrape_facebook_profile(url):
    # Make a GET request to the Facebook profile page
    response = requests.get(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the element containing the name of the person
    name_element = soup.find('h1', {'class': '_1dpq'})
    # Extract the text of the element
    name = name_element.text
    # Find the element containing the username of the person
    username_element = soup.find('a', {'class': '_5pb8 _2dgj _29hk _29hj'})
    # Extract the text of the element
    username = username_element.text
    # Return the name and username as a tuple
    return (name, username)

#Next, you will need to define a function that generates an HTML table containing the scraped data. 
#This function should take a list of tuples, where each tuple contains the name and other data for a person, and return an HTML string representing the table.
def generate_html_table(data):
  # Start building the HTML string
  html = '<table>\n'
  # Add a row for the table headers
  html += '  <tr>\n'
  html += '    <th>Name</th>\n'
  html += '    <th>Other Data</th>\n'
  html += '  </tr>\n'
  # Add a row for each person
  for name, other in data:
      html += '  <tr>\n'
      html += f'    <td>{name}</td>\n'
      html += f'    <td>{other}</td>\n'
      html += '  </tr>\n'
    # End the HTML string
  html += '</table>'
  return html

  
  #Finally, you will need to write the main function that ties everything together. 
  #This function should prompt the user for the URLs of the LinkedIn, Twitter, and Facebook profiles they want to scrape, call the appropriate scraping function for each URL, and generate an HTML table containing the results.
  
  def main():
    # Prompt the user for the LinkedIn URL
    linkedin_url = input('Enter the LinkedIn URL: ')
    # Scrape the LinkedIn profile and store the results in a list
    linkedin_data = [scrape_linkedin_profile(linkedin_url)]
    # Prompt the user for the Twitter URL
    twitter_url = input('Enter the Twitter URL: ')
    # Scrape the Twitter profile and store the results in a list
    twitter_data = [scrape_twitter_profile(twitter_url)]
    # Prompt the user for the Facebook URL
    facebook_url = input('Enter the Facebook URL: ')
    # Scrape the Facebook profile and store the results in a list
    facebook_data = [scrape_facebook_profile(facebook_url)]
    # Combine the data from all three websites into a single list
    data = linkedin_data + twitter_data + facebook_data
    # Generate an HTML table containing the combined data
    html = generate_html_table(data)
    # Print the HTML table
    print(html)

if __name__ == '__main__':
    main()

    
### To modify the functions to extract different types of data from LinkedIn, Twitter, and Facebook, you will need to modify the scrape_linkedin_profile(), scrape_twitter_profile(), and scrape_facebook_profile() functions to use the appropriate HTML elements and attributes to extract the data you are interested in.
### For example, to extract the location of a LinkedIn profile, you could use the following code
##def scrape_linkedin_profile(url):
##    # Make a GET request to the LinkedIn profile page
##    response = requests.get(url)
##    # Parse the HTML content of the page
##    soup = BeautifulSoup(response.text, 'html.parser')
##    # Find the element containing the name of the person
##    name_element = soup.find('h1', {'class': 'pv-top-card-section__name'})
##    # Extract the text of the element
##    name = name_element.text
##    # Find the element containing the job title of the person
##    title_element = soup.find('h2', {'class': 'pv-top-card-section__headline'})
##    # Extract the text of the element
##    title = title_element.text
##    # Find the element containing the location of the person
##    location_element = soup.find('h3', {'class': 'pv-top-card-section__location'})
##    # Extract the text of the element
##    location = location_element.text
##    # Return the name, title, and location as a tuple
##    return (name, title, location)
##
##  
## 
### To extract the number of followers of a Twitter profile, you could use the following code
##
##def scrape_twitter_profile(url):
##    # Make a GET request to the Twitter profile page
##    response = requests.get(url)
##    # Parse the HTML content of the page
##    soup = BeautifulSoup(response.text, 'html.parser')
##    # Find the element containing the name of the person
##    name_element = soup.find('h1', {'class': 'ProfileHeaderCard-name'})
##    # Extract the text of the element
##    name = name_element.text
##    # Find the element containing the username of the person
##    username_element = soup.find('span', {'class': 'ProfileHeaderCard-screennameLink u-linkComplex js-nav'})
##    # Extract the text of the element
##    username = username_element.text
##    # Find the element containing the number of followers of the person
##    followers_element = soup.find('li', {'class': 'ProfileNav-item ProfileNav-item--followers'})
##    # Extract the text of the element
##    followers = followers_element.find('span', {'class': 'ProfileNav-value'}).text
##    # Return the name, username, and number of followers as a tuple
##    return (name, username, followers)
##
##  
## 
###To extract the number of friends of a Facebook profile, you could use the following code
##def scrape_facebook_profile(url):
##    # Make a GET request to the Facebook profile page
##    response = requests.get(url)
##    # Parse the HTML content of the page
##    soup = BeautifulSoup(response.text, 'html.parser')
##    # Find the element containing the name of the person
##    name_element = soup.find('h1', {'class': '_1dpq'})
##    # Extract the text of the element
##    name = name_element.text
##    # Find the element containing the username of the person
##    username_element = soup.find('a', {'class': '_5pb8 _2dgj _29hk _29hj'})
##    # Extract the text of the element
##    username = username_element.text
##    # Find the element containing the number of friends of the person
##    friends_element = soup.find('a', {'class': '_5pb8 _2dgj _29hk _29hj'}, text='Friends')
##    # Extract the text of the element
##    friends = friends_element.find_next_sibling('span').text
##    # Return the name, username, and number of friends as a tuple
##    return (name, username, friends)
##
##  
##  
###To customize the HTML table to fit your needs, you can modify the generate_html_table() function to add or remove table columns, change the text of the table headers, and modify the way the data is displayed in the table cells.
###For example, to add a third column to the table to display the location of LinkedIn profiles and the number of followers and friends of Twitter and Facebook profiles, you could modify the generate_html_table() function as follows:
##
##def generate_html_table(data):
##    # Start building the HTML string
##    html = '<table>\n'
##    # Add a row for the table headers
##    html += '  <tr>\n'
##    html += '    <th>Name</th>\n'
##    html += '    <th>Other Data</th>\n'
##    html += '    <th>Location/Followers/Friends</th>\n'
##    html += '  </tr>\n'
##    # Add a row for each person
##    for name, other, location in data:
##        html += '  <tr>\n'
##        html += f'    <td>{name}</td>\n'
##        html += f'    <td>{other}</td>\n'
##        html += f'    <td>{location}</td>\n'
##        html += '  </tr>\n'
##    # End the HTML string
##    html += '</table>'
##    return html


  ## #To change the text of the table headers, you can simply modify the text between the <th> tags. 
##  #For example, to change the third column header to "Location" for LinkedIn profiles, "Followers" for Twitter profiles, and "Friends" for Facebook profiles, you could modify the generate_html_table() function as follows:
##  def generate_html_table(data):
##    # Start building the HTML string
##    html = '<table>\n'
##    # Add a row for the table headers
##    html += '  <tr>\n'
##    html += '    <th>Name</th>\n'
##    html += '    <th>Other Data</th>\n'
##    html += '    <th>Location</th>\n'
##    html += '  </tr>\n'
##    # Add a row for each LinkedIn profile
##    for name, other, location in data:
##        html += '  <tr>\n'
##        html += f'    <td>{name}</td>\n'
##        html += f'    <td>{other}</td>\n'
##        html += f'    <td>{location}</td>\n'
##        html += '  </tr>\n'
##    # Add a row for each Twitter profile
##    for name, other, followers in data:
##        html += '  <tr>\n'
##        html += f'    <td>{name}</td>\n'
##        html += f'    <td>{other}</td>\n'
##        html += f'    <td>{followers}</td>\n'
##        html += '  </tr>\n'
##    # Add a row for each Facebook profile
##    for name, other, friends in data:
##        html += '  <tr>\n'
##        html += f'    <td>{name}</td>\n'
##        html += f'    <td>{other}</td>\n'
##        html += f'    <td>{friends}</td>\n'
##        html += '  </tr>\n'
##    # End the HTML string
##    html += '</table>'
##    return html
##
###To modify the way the data is displayed in the table cells by using formatting tags such as <b>, <i>, and <u>, you can include these tags within the text of the table cells when generating the HTML string.
###For example, to make the text of the first column bold, you could modify the generate_html_table() function as follows:
##
##def generate_html_table(data):
##    # Start building the HTML string
##    html = '<table>\n'
##    # Add a row for the table headers
##    html += '  <tr>\n'
##    html += '    <th>Name</th>\n'
##    html += '    <th>Other Data</th>\n'
##    html += '    <th>Location/Followers/Friends</th>\n'
##    html += '  </tr>\n'
##    # Add a row for each person
##    for name, other, location in data:
##        html += '  <tr>\n'
##        html += f'    <td><b>{name}</b></td>\n'
##        html += f'    <td>{other}</td>\n'
##        html += f'    <td>{location}</td>\n'
##        html += '  </tr>\n'
##    # End the HTML string
##    html += '</table>'
##    return html
##
##
###You can also use the <i> tag to make the text italic, and the <u> tag to underline the text.
###To apply additional formatting using CSS styles, you can include a style attribute within the <td> tags and specify the desired styles as a value. For example, to change the text color to red, you could modify the generate_html_table() function as follows:
##def generate_html_table(data):
##    # Start building the HTML string
##    html = '<table>\n'
##    # Add a row for the table headers
##    html += '  <tr>\n'
##    html += '    <th>Name</th>\n'
##    html += '    <th>Other Data</th>\n'
##    html += '    <th>Location/Followers/Friends</th>\n'
##    html += '  </tr>\n'
##    # Add a row for each person
##    for name, other, location in data:
##        html += '  <tr>\n'
##        html += f'    <td style="color: red;">{name}</td>\n'
##        html += f'    <td>{other}</td>\n'
##        html += f'    <td>{location}</td>\n'
##        html += '  </tr>\n'
##    # End the HTML string
##    html += '</table>'
##    return html
##
##  #You can specify multiple styles by separating them with a semicolon. For example, to change the text color to red and make it italic, you could use the following code:
##  html += f'    <td style="color: red; font-style: italic;">{name}</td>\n'
##
 
  
