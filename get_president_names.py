from web_scraping import get_parsed_url

url = 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States'
page_soup = get_parsed_url(url)
table = page_soup.findAll('table', {'class': 'wikitable'})
table_rows = table[0].find_all('tr')
# print(table_rows[2].find_all('td')[3].a.getText())
working_data = table_rows[2:]

for row in working_data:
    if len(row.find_all('td')) >= 4:
        print(row.find_all('td')[3].a.getText())