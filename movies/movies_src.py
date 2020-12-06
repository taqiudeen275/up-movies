from bs4 import BeautifulSoup
import requests

# intializing
get_site = requests.get('http://toxicwap.com/New_Movies/')
site = BeautifulSoup(get_site.content, 'html.parser')

# finding the list of movies
li = site.find_all('li')

#list of movies names
movies_names = [a.find('a').get_text() for a in li]

# list of movies links
movies_links = [a.find('a', href=True)['href'] for a in li]


# geting a single movies link
moviel = movies_links[3]
get_movie = requests.get(f'{moviel}')
movie = BeautifulSoup(get_movie.content, 'html.parser')
# mlink -- single movie proceed to download link
mlink = movie.find('a', href=True)['href']

get_proceed_to_download = requests.get(f'{mlink}')
proceed_movie = BeautifulSoup(get_proceed_to_download.content, 'html.parser')
download_links_ul = proceed_movie.find_all('li')


print(download_links_ul)
# download_links = download_links_ul.find_all('a', href=True)['href']

# print(download_links)