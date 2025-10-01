from bs4 import BeautifulSoup 
import requests 
import re 


  
# function to extract html document from given url 
def getHTMLdocument(url): 
      
    # request for HTML document of given url 
    response = requests.get(url) 
      
    # response will be provided in JSON format 
    return response.text 
  
    
# assign required credentials 
# assign URL 
url_to_scrape = "https://mannahouseinc.org/our-services/breakfast/"
  
# create document 
html_document = getHTMLdocument(url_to_scrape) 
  
# create soap object 
soup = BeautifulSoup(html_document, 'html.parser') 


print(soup.prettify)

with open('output.txt', 'w') as file:
    # Write content to the file
    file.write(str(soup.prettify))