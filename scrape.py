import requests
import bs4

list_of_urls = ['http://www.acceptancerate.com/alabama', 'http://www.acceptancerate.com/alaska', 'http://www.acceptancerate.com/arizona',
'http://www.acceptancerate.com/arkansas', 'http://www.acceptancerate.com/california', 'http://www.acceptancerate.com/colorado',
'http://www.acceptancerate.com/connecticut', 'http://www.acceptancerate.com/delaware', 'http://www.acceptancerate.com/florida',
'http://www.acceptancerate.com/georgia', 'http://www.acceptancerate.com/hawaii', 'http://www.acceptancerate.com/idaho',
'http://www.acceptancerate.com/illinois', 'http://www.acceptancerate.com/indiana', 'http://www.acceptancerate.com/iowa',
'http://www.acceptancerate.com/kansas', 'http://www.acceptancerate.com/kentucky', 'http://www.acceptancerate.com/louisiana',
'http://www.acceptancerate.com/maine', 'http://www.acceptancerate.com/maryland', 'http://www.acceptancerate.com/massachusetts',
'http://www.acceptancerate.com/michigan', 'http://www.acceptancerate.com/minnesota', 'http://www.acceptancerate.com/mississippi',
'http://www.acceptancerate.com/missouri', 'http://www.acceptancerate.com/montana', 'http://www.acceptancerate.com/nebraska',
'http://www.acceptancerate.com/nevada', 'http://www.acceptancerate.com/new-hampshire', 'http://www.acceptancerate.com/new-jersey',
'http://www.acceptancerate.com/new-york', 'http://www.acceptancerate.com/new-mexico', 'http://www.acceptancerate.com/north-carolina',
'http://www.acceptancerate.com/north-dakota', 'http://www.acceptancerate.com/ohio', 'http://www.acceptancerate.com/oklahoma',
'http://www.acceptancerate.com/oregon', 'http://www.acceptancerate.com/pennsylvania', 'http://www.acceptancerate.com/rhode-island',
'http://www.acceptancerate.com/south-carolina', 'http://www.acceptancerate.com/south-dakota', 'http://www.acceptancerate.com/tennessee',
'http://www.acceptancerate.com/texas', 'http://www.acceptancerate.com/utah', 'http://www.acceptancerate.com/vermont',
'http://www.acceptancerate.com/virginia', 'http://www.acceptancerate.com/washington', 'http://www.acceptancerate.com/west-virginia',
'http://www.acceptancerate.com/wisconsin', 'http://www.acceptancerate.com/wyoming']

def parse_and_read_file(input_text):

	soup = bs4.BeautifulSoup(response.text)
	f = open("file.csv", "a")

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

	for [i, j] in zipped:
		line = ",".join([i, j])
		f.write(line + '\n')

	f.close()

for item in list_of_urls:
	response = requests.get(item)
	parse_and_read_file(response)
