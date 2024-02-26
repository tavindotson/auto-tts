# This script will scrape an element on a given webpage for a list of links
# and then dump the text from a specific element into a .txt file

# Optional if you put your own .txt in the /files folder

import requests
from bs4 import BeautifulSoup
import os

def extract_content_and_save(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        chapter_title = soup.find('h1', class_='gh-article-title').text.strip()
        content_div = soup.find('div', class_='gh-content gh-canvas')
        chapter_content = content_div.text.strip()
        filename = f"{chapter_title}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(chapter_content)
        print(f"Saved content to {filename}")
    else:
        print(f"Failed to fetch content from {url}")

def main():
    base_url = int(input("Enter the url to scrape: "))
    for i in range(137):
        url = base_url + str(i) + "/"
        extract_content_and_save(url)

if __name__ == "__main__":
    print("Just a heads up, this script usually requires some editing before it will work.")
    print("You can load text files into /files and skip this step")
    main()
