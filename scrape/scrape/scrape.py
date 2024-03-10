from bs4 import BeautifulSoup
import requests
import os
class Scrape:
   
    def scrape(self, url):
        # give your url here
        # get the url
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            # get the text using soup
            text = soup.get_text()
            visible_text = text.strip()
            # removing extralines
            cleaned_text_line = [line for line in visible_text.splitlines() if line.strip()]
            cleaned_text = '\n'.join(cleaned_text_line)
        else:
            print("Text content not found on the page.")
        
        # create a folder and save the extracted file
        page_name = os.path.basename(url)
        filename = f'scraped_pages/{page_name}.txt'

        # Create the "scraped_pages" folder if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        # Save the scraped text to the specified file
        with open(filename, 'w', encoding='utf-8') as output_file:
            output_file.write(cleaned_text)
        return filename