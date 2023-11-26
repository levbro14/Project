import requests

player_name = input("Введите ник: ")
platform = 'epic'  # Замените на платформу игрока (pc, xbox, psn)
api_key = 'e6854e8f-b89c-4011-9a17-dcdfee426b8e'

base_url = f"https://fortnite-api.com/v2/stats/br/v2?name={player_name}&platform={platform}&image=all"
headers = {'Authorization': api_key}

try:
	response = requests.get(base_url, headers=headers)
	data = response.json()
	
	
	text = data.get("data")
	print(text)
	
	img = text.get("image")
	req = requests.get(img)
	open(f"{player_name} statistics.png",'wb').write(req.content)
	
	
except Exception as e:
	print(f"Произошла ошибка: {e}")



