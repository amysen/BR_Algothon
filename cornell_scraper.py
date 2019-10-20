# import libraries
from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup

quote_page = "https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=Machine+Learning&terms-0-field=title&classification-computer_science=y&classification-economics=y&classification-eess=y&classification-mathematics=y&classification-physics=y&classification-physics_archives=all&classification-q_biology=y&classification-q_finance=y&classification-statistics=y&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date=2009&date-to_date=2019&date-date_type=announced_date_first&abstracts=show&size=200&order=announced_date_first&start=3200"

page = urlopen(quote_page).read()

soup = BeautifulSoup(page, 'html.parser')

papersAll = soup.find("h1", attrs={"class": "title is-clearfix"}).text

total_papers = papersAll.strip().split(" ")[3]

individualTitles = []


for line in soup.find_all("p", attrs={"class": "title is-5 mathjax"}):
	line = line.text
	line = line.strip()
	line = line.replace("\n", "")
	line = line.replace(",", "")
	line = line.split("originally announced")
	individualTitles.append(line)
	

individualAnnounceDate = []

for line in soup.find_all("p", attrs={"class": "is-size-7"}):
	line = line.text
	line = line.strip()
	line = line.replace("\n", "")
	line = line.replace(",", "")
	line = line.split("originally announced")
	
	if (len(line) == 2):
		individualAnnounceDate.append(line[1][1:-1])


individualAuthors = []
for line in soup.find_all("p", attrs={"class": "authors"}):
	line = line.text
	line = line.replace("\n", "")[8:]
	# line = line.replace(",", "")
	line = ' '.join(line.split())
	# line = line.split(",")
	print(line)
	individualAuthors.append(line)



for i in range(len(individualAnnounceDate)):
	with open("index.csv", "a") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([individualTitles[i][0], individualAnnounceDate[i], individualAuthors[i]])


