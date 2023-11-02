from bs4 import BeautifulSoup
import requests
import csv

soup = BeautifulSoup(requests.get('http://localhost:3000').text, 'lxml')
#soup = BeautifulSoup(open('index.html'), 'lxml')
print(soup.prettify())

article = soup.find('div', class_='post')
print(article)

csv_file = open('data.csv', 'w', newline='')
writer = csv.writer(csv_file)

writer.writerow(['title', 'summary', 'link'])

for blog in soup.find_all('div', class_='post'):
    title = article.h3.a.text
    summary = article.p.text
    link = "http://localhost:3000{0}".format(article.h3.a['href'])
    # print(title, summary, link)
    row = ['title', 'summary', 'link']
    writer.writerow(row)

csv_file.close()

for data in soup.find_all('td', class_='data'):
    print(data.text)