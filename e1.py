import requests
from bs4 import BeautifulSoup as bs
election_id = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
resp = requests.get(election_id)
soup = bs(resp.content , "html.parser")
ID = soup.find_all("tr", "election_item")
for row in ID:
    print(row.find("td", "year first").string)
    print(row.get("id").replace("election-id-", ""))
