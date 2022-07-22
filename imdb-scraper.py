import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm

# Shortcut for pool manager which arranges connections
http = urllib3.PoolManager()

# Scraping target URL
url = 'https://www.imdb.com/chart/top/'
# Gets the data and .data property gives the code acces to json file
url_data = http.request('GET', url).data
# Converts the url_data into a xml file
url_data_xml = BeautifulSoup(url_data, 'lxml')

i = 1

# Finds tags with given classes
# findAll stores them in movieList
movieList_general = url_data_xml.find('tbody', attrs={'class': 'lister-list'})
movieList = movieList_general.findAll('tr')

print("IMDb's Top 250 Movies of All Time")
# Iterates through the list tqdm is for the loading bar at the end
for td_item in tqdm(movieList):
    # Finds title column
    header = td_item.findChildren('td', attrs={'class': 'titleColumn'})

    # Prints the iterations after finding children
    print(str(i) + '. Movie: ' + str((header[0].findChildren('a'))
          [0].contents[0].encode('utf-8').decode('ascii', 'ignore')) + ' ' + str((header[0].findChildren('span'))
          [0].contents[0].encode('utf-8').decode('ascii', 'ignore')))

    i += 1
