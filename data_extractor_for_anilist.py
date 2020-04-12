import requests
from bs4 import BeautifulSoup
import bs4
import json
from selenium import webdriver
import os


def download_image(url, filename):
    file_extension = url.split('.')[-1]
    open(filename + '.' + file_extension, 'wb').write(requests.get(url).content)


# Welcome Message
print('Data Extractor for AniList | By: Nicholas Dawson')
print('Initializing Web Driver...')

# Setup Web Driver
options = webdriver.FirefoxOptions()
options.headless = True
browser = webdriver.Firefox(firefox_options=options)


def download_data(url):
    # Parse URL to get filename friendly title
    file_title = ' - '.join(url.split('/')[3:6])
    
    # Download Init Message
    print(file_title)
    print('=' * 12)
    
    # Create Directory
    if not os.path.isdir(file_title):
        os.makedirs(file_title)

    # Get Site
    print('Loading Webpage...')
    browser.get(url)

    # Parse HTML
    print('Parsing Webpage...')
    html = BeautifulSoup(browser.page_source, 'lxml')

    # Parse data from website
    print('Finding metadata...')
    anime_data = {}

    # Added try except because some pages don't have a banner
    try:
        banner_image = html.find('div', {'class': 'banner'})['style']
        banner_image = banner_image[banner_image.find('"') + 1:banner_image.rfind('"')]
        anime_data.update({'Banner Image': banner_image})
    except TypeError:
        banner_image = False
    cover_image = html.find('img', {'class': 'cover'})['src']
    anime_data.update({'Cover Image': cover_image})
    title = html.find('h1').text.strip()
    anime_data.update({'Title': title})
    description = html.find('p', {'class': 'description'}).text
    anime_data.update({'Description': description})


    for x in html.find('div', {'class': 'data'}):
        # Ensure only tags are processed, not comments and other elements
        if type(x) == bs4.element.Tag:
            key = x.find('div', {'class': 'type'}).text

            # To process a data-list
            if x['class'] == ['data-set', 'data-list']:
                value = []
                for item in x.find('div', {'class': 'value'}):
                        value.append(item.text.strip().strip(','))

            # To process a normal data-set
            else:
                try:
                    value = x.find('div', {'class': 'value'}).text.strip()
                except AttributeError:
                    value = x.find('a', {'class': 'value'}).text.strip()
                if key == 'Episode\n\t\t\tDuration\n\t\t':
                    key = 'Episode Duration'
                elif key == '\n\t\t\tDuration\n\t\t':
                    key = 'Duration'

            # Add key & value pair to the data dict
            anime_data.update({key: value})

    tags = []

    for x in html.findAll('div', {'class': 'tag'}):
        tag = x.a.text.replace('\n', '').replace('\t', '')
        rank = x.div.text
        tags.append([tag, rank])

    anime_data.update({'tags': dict(tags)})

    print('Saving metadata to "data.json"...')
    open(file_title + '/data.json', 'w').write(json.dumps(anime_data))

    print('Downloading Images...')
    if banner_image:
        download_image(banner_image, file_title + '/banner')
    download_image(cover_image, file_title + '/cover')

    print('Done!')
    print('=' * 12)

try:
    # Ask user for mode (list | url)
    print('What download mode would you like?')
    print('list: downloads data for all links in a text file')
    print('url: downloads data for a single link')
    mode = input('(list | url): ')

    # List Mode
    if mode in ['list', 'List', 'l', 'L']:
        txt = input('Enter Text Document Filename: ')
        for x in open(txt, 'r').read().split('\n'):
            download_data(x)

    # URL Mode
    elif mode in ['url', 'URL', 'Url', 'u', 'U']:
        # Ask for url
        url = input('Paste the URL: ')
        download_data(url)
        while True:
            another_download = input('Download another or quit (enter url | quit): ')
            if another_download not in ['quit', 'q', 'Q', 'Quit', 'exit', 'Exit']:
                # Ask for url
                url = input('Paste the URL: ')
                download_data(url)
            else:
                break
                
finally:
    browser.quit()




