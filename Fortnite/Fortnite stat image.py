from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def get_fortnite_stats(api_key, player_name):
    
    url = f'https://fortnite-api.com/v2/stats/br/v2?name={player_name}'
    headers = {'Authorization': api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        return data
    else:
        print(f'Error: {response.status_code}')
        print(response.text)
        return None

def create_stats_image(data):
    
    image = Image.new('RGB', (800, 600), 'white')
    draw = ImageDraw.Draw(image)

    font_path = 'C:/Windows/Fonts/Arial.ttf'
    font = ImageFont.truetype(font_path, 20)

    draw.text((10, 10), f"Игрок: {data['account']['name']}", fill='black', font=font)
    draw.text((10, 40), f"Уровень БП: {data['battlePass']['level']}", fill='black', font=font)
    draw.text((180, 40), f"Процент: {data['battlePass']['progress']}", fill='black', font=font)

    # Добавьте другие элементы статистики по вашему усмотрению

    image_bytes = BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    return image_bytes

def display_image(image_bytes):
    # Отображение изображения
    image = Image.open(image_bytes)
    image.show()

api_key = 'e6854e8f-b89c-4011-9a17-dcdfee426b8e'
player_name = 'levletsplay'

player_stats = get_fortnite_stats(api_key, player_name)

if player_stats:
    image_bytes = create_stats_image(player_stats)
    display_image(image_bytes)
