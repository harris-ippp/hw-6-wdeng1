import requests
from bs4 import BeautifulSoup as bs
election_id = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
resp = requests.get(election_id)
soup = bs(resp.content , "html.parser")
ID = soup.find_all("tr", "election_item")
with open("ELECTION_ID", "w") as out:
    for row in ID:
        v1 = row.find("td", "year first").string
        v2 = row.get("id").replace("election-id-", "")
        out.write("{} {}\n".format(v1, v2))
