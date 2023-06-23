import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}

#goes to all pages
file = open('data.txt', 'w')
count = 0
quotes = []
for i in range(0,120,10):
    URL = "https://targetstudy.com/colleges/engineering-colleges-in-chennai.html"+"?recNo="+str(i)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html5lib")    

    title = soup.find_all("a", class_='card-title h5')

    print(i,"th page completed")
    for i in title:
        college_url = i['href']
        response = requests.get(college_url, headers=headers)
        html = BeautifulSoup(response.content, 'html5lib')
        quote = {}

        title = html.find('h1', class_="d-inline-block")
        quote['title'] = title.text.strip()
        # print(title.text)
        
        address = html.find_all(class_="pmd-list-title")
        
        add = address[0].text.strip()
        quote['address'] = add[:-7]
        # print(add[:-7])
        
        ph = address[1].text.strip()
        quote['phone'] = ph[:24]
        # print(phone[:24])
        quotes.append(quote)

    
filename = 'collegedata.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['title','address','phone'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
file.close()      
        
    