import requests
from bs4 import BeautifulSoup as bs

files = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"
resp = requests.get(files)
soup = bs(resp.content , "html.parser")

for line in open("ELECTION_ID"):
    a = line.split()
    file_name = a[0] + ".csv"
    files = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(a[1])
    with open(file_name, "w") as out:
        out.write(resp.text)
