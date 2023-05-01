import requests
from bs4 import BeautifulSoup
import csv

names=[]
listing_titles=[]
handle=[]
url = 'https://collabstr.com/influencers?p=instagram&c=lifestyle+Fashion+Beauty+Travel+Health+%26+Fitness+Food+%26+Drink+Model+Comedy+%26+Entertainment+Art+%26+Photography+Entrepreneur+%26+Business+Music+%26+Dance+Family+%26+Children+Animals+%26+Pets+Athlete+%26+Sports+Education+Adventure+%26+Outdoors+Celebrity+%26+Public+Figure+Actor+Gaming+&ct=united+states&l=Los+Angeles%2C+CA%2C+United+States&l_id=99001&pg=6'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
name_data = soup.find_all('div', class_ = 'profile-listing-owner-name')
for name in name_data:
    names.append(name.text)

listing_title_data = soup.find_all('h3', class_='profile-listing-title')
for listing_title in listing_title_data:
    listing_titles.append(listing_title.text)

data = soup.find_all('div', class_ = 'profile-listing-holder')
for div in data:
    links = div.find_all('a', href=True)
    for link in links:
        handle.append('@'+link['href'][1:-12])
 
with open('info5.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=';',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Name','Listing Title','Handle'])
    for i in range(len(names)):
        writer.writerow([names[i],listing_titles[i],handle[i]])