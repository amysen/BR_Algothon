#hi
import scholarly

# search_query = scholarly.search_keyword('Machine Learning')
arr = []
for a in scholarly.search_pubs_custom_url("/scholar?q=%22machine+learning%22&hl=en&as_sdt=1%2C5&as_ylo=2009&as_yhi=2019"):
	arr.append(a)


title = [p.bib['title'] for p in scholarly.search_pubs_query('machine learning')]
auth = [p.bib['author'] for p in scholarly.search_pubs_query('machine learning')]
year = [p.bib['year'] for p in scholarly.search_pubs_query('machine learning')]

for p in (scholarly.search_pubs_query('machine learning')):
    print(p)
    title.append(p.bib['title'])
    auth.append(p.author)
    year.append(p.year)

# print(title)
# print(auth)
# print(year)

for i in range(len(title)):
    with open("index.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(title[i], auth[i], year[i])

print(arr)