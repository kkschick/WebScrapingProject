import requests
import bs4
import csv

response = requests.get('http://www.acceptancerate.com/california')
soup = bs4.BeautifulSoup(response.text)
f = csv.writer(open("file.csv", "w"))

college_list = []

college_names = soup.find_all('a')

for link in college_names[59:]:
    names = link.contents[0]
    college_list.append(names)

acceptance_list = []

acceptance_rates = soup.find_all("td", { "class" : "fs26" })

for item in acceptance_rates:
	percentage = item.contents[0]
	acceptance_list.append(percentage)

zipped = zip(college_list, acceptance_list)

for (i, j) in zipped:
	f.writerow((i, j))