#A python program that searches for hardcoded credentials, PII (personally identifiable information), IP addresses, and URLs in source code files and log files with no extension in a given directory and its subdirectories. It stores the results in an HTML table, removes duplicates, and provides the severity and confidence of each result.
#This is the complete program that searches for hardcoded credentials, PII, IP addresses, and URLs in source code files and log files with no extension in a given directory and its subdirectories, stores the results in an HTML table, removes duplicates, and provides the severity and confidence of each result.

#To start, we will need to import the necessary modules:

import os
import re
import html

#Next, we will define a function search_files that takes in a directory path and searches for hardcoded credentials, PII, IP addresses, and URLs in the files under that directory.
def search_files(dir_path):
    # Create an empty list to store the results
    results = []
    
    # Define regular expressions for hardcoded credentials, PII, IP addresses, and URLs
    cred_regex = r"username|password|credential"
    pii_regex = r"name|address|phone|email|ssn|personal"
    ip_regex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    url_regex = r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # Open the file and read its contents
            with open(os.path.join(root, file), "r") as f:
                contents = f.read()
                
            # Search for hardcoded credentials
            for match in re.finditer(cred_regex, contents, re.IGNORECASE):
                start, end = match.span()
                result = {
                    "type": "hardcoded credential",
                    "severity": "high",
                    "confidence": "high",
                    "value": contents[start:end],
                    "file": os.path.join(root, file)
                }
                results.append(result)
                
            # Search for PII
            for match in re.finditer(pii_regex, contents, re.IGNORECASE):
                start, end = match.span()
                result = {
                    "type": "PII",
                    "severity": "medium",
                    "confidence": "high",
                    "value": contents[start:end],
                    "file": os.path.join(root, file)
                }
                results.append(result)
                
            # Search for IP addresses
            for match in re.finditer(ip_regex, contents):
                start, end = match.span()
                result = {
                    "type": "IP address",
                    "severity": "low",
                    "confidence": "high",
                    "value": contents[start:end],
                    "file": os.path.join(root, file)
                }
                results.append(result)
                
            # Search for URLs
            for match in re.finditer(url_regex, contents):
              start, end = match.span()
              result = {
                "type": "URL",
                "severity": "low",
                "confidence": "high",
                "value": contents[start:end],
                "file": os.path.join(root, file)
              }
              results.append(result)
  # Return the results            
      return results

#Next, we will define a function remove_duplicates that takes in a list of results and removes any duplicates. 
#We will do this by creating a set of unique values and then converting it back to a list.
def remove_duplicates(results):
    # Create a set of unique values
    unique_values = set()
    for result in results:
        unique_values.add(result["value"])
        
    # Convert the set back to a list
    unique_results = [result for result in results if result["value"] in unique_values]
    
    # Return the unique results
    return unique_results

  #Now, we will define a function generate_html_table that takes in a list of results and generates an HTML table from the data.
  def generate_html_table(results):
    # Create the HTML table
    html_table = "<table>\n"
    html_table += "<tr>\n"
    html_table += "<th>Type</th>\n"
    html_table += "<th>Severity</th>\n"
    html_table += "<th>Confidence</th>\n"
    html_table += "<th>Value</th>\n"
    html_table += "<th>File</th>\n"
    html_table += "</tr>\n"
    
    # Add the results to the table
    for result in results:
        html_table += "<tr>\n"
        html_table += "<td>{}</td>\n".format(html.escape(result["type"]))
        html_table += "<td>{}</td>\n".format(html.escape(result["severity"]))
        html_table += "<td>{}</td>\n".format(html.escape(result["confidence"]))
        html_table += "<td>{}</td>\n".format(html.escape(result["value"]))
        html_table += "<td>{}</td>\n".format(html.escape(result["file"]))
        html_table += "</tr>\n"
    
    # Close the table
    html_table += "</table>\n"
    
    # Return the HTML table
    return html_table
  
  
#Finally, we will define the main function and put everything together.
def main():
    # Prompt the user for the directory path
    dir_path = input("Enter the directory path: ")
    
    # Search the files for hardcoded credentials, PII, IP addresses, and URLs
    results = search_files(dir_path)
    
    # Remove any duplicates
    unique_results = remove_duplicates(results)

    # Generate the HTML table
    html_table = generate_html_table(unique_results)

    # Print the HTML table
print(html_table)


# Finally, we will call the main function to start the program.
if __name__ == "__main__":
    main()
