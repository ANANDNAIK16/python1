from pycricbuzz import cricbuzz
c=cricbuzz()
matches=c.matches()
for match in matches:
    print(match)
    if  (match['mchstate']!='nextlive'):
        print(c.livescore(match['id']))
        print(c.commentary(match['id']))
        print(c.scorecard(match['id']))