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

    title = soup.find_all("a", class_="card-title h5")
    address = soup.find_all("p", class_="card-subtitle mt-0")
    
    index = 0
    

    for i in range(len(title)):
        quote = {}
        quote['title'] = title[i].text.strip()
        file.write(title[i].text)
        file.write("\n")

        add = address[index].text.strip()
        quote['address'] = add[12:]
        file.write(address[index].text.strip())
        file.write("\n")
        
        ph = address[index+1].text.strip()
        quote['phone'] = ph[5:29]
        file.write(address[index+1].text.strip())
        file.write("\n")
        file.write("\n")
        index += 2
        count += 1

        quotes.append(quote)  

    print("Wrote", count, "items")

filename = 'collegedata.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['title','address','phone'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
file.close()