import requests
import bs4
link = "https://www.cricbuzz.com/live-cricket-scorecard/71607/sl-vs-uae-3rd-match-group-b-icc-cricket-world-cup-qualifiers-2023"

res=requests.get(link)
soup = bs4.BeautifulSoup(res.text,'html.parser')

details = soup.select('.cb-col .cb-col-100 .cb-scrd-hdr-rw')
for i in details:
    print(i.getText())