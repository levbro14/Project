import requests

url = 'https://fortnite-api.com/images/map_ru.png'  # Замените на URL нужного вам файла

response = requests.get(url)

if response.status_code == 200:
	with open('map_ru.png', 'wb') as file:
		file.write(response.content)

	print('Файл успешно загружен')
else:
	print('Не удалось загрузить файл. Код статуса:', response.status_code)




