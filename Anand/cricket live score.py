import requests

def get_live_cricket_scores():
    url = "http://site.web.api.espn.com/apis/site/v2/sports/cricket/summary?event=123456"
    # Replace the event ID with the actual event ID you want to fetch the scores for
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            
            # Extract relevant information from the JSON response
            match_status = data['header']['status']
            team_1 = data['competitions'][0]['competitors'][0]['team']['name']
            team_2 = data['competitions'][0]['competitors'][1]['team']['name']
            team_1_score = data['competitions'][0]['competitors'][0]['score']
            team_2_score = data['competitions'][0]['competitors'][1]['score']
            
            # Print the live score information
            print("Match Status:", match_status)
            print(team_1, "vs", team_2)
            print(team_1, "Score:", team_1_score)
            print(team_2, "Score:", team_2_score)
            
        else:
            print("Failed to fetch live cricket scores. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

# Call the function to get live cricket scores
get_live_cricket_scores()
