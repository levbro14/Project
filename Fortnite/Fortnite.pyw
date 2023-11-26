import requests
import tkinter as tk
from tkinter import ttk

def click():
    player_name = entry.get()
    api_key = 'e6854e8f-b89c-4011-9a17-dcdfee426b8e'
    platform = 'epic'
    
    base_url = f"https://fortnite-api.com/v2/stats/br/v2?name={player_name}&accountType={platform}"
    headers = {'Authorization': api_key}
    
    try:
        response = requests.get(base_url, headers=headers)
        data = response.json()
	
        # Обработка данных
        # Ваши действия с полученными данными здесь
	
        print(data)
        status = data.get("status")
        if(status != 200):
            label1.config(text="Игрок не найден!")
        else:
            a = data.get("data")
            acc = a.get("account")
            name = acc.get("name")
            id = acc.get("id")
            BP = a.get("battlePass")
            lvl = BP.get("level")
            percent = BP.get("progress")
            stats = a.get("stats")
            all = stats.get("all")
            overall = all.get("overall")
            score = overall.get("score")
            wins = overall.get("wins")
            top3 = overall.get("top3")
            top5 = overall.get("top5")
            top6 = overall.get("top6")
            top10 = overall.get("top10")
            top12 = overall.get("top12")
            top25 = overall.get("top25")
            kills = overall.get("kills")
            deaths = overall.get("deaths")
            kd = overall.get("kd")
            matches = overall.get("matches")
            winRate = overall.get("winRate")
            minutesPlayed = overall.get("minutesPlayed")
            playersOutlived = overall.get("playersOutlived")
            lastModified = overall.get("lastModified")

            label1.config(text=f"Ваш ник: {name}\n" + f"Ваш id Epic: {id}\n" + f"Уровень бп: {lvl}| {percent}%\n" + f"Счет: {score}\n" + f"Побед: {wins}\n" + f"Топ 3: {top3}\n" + f"Топ 5: {top5}\n" + f"Топ 6: {top6}\n" + f"Топ 10: {top10}\n" + f"Топ 12: {top12}\n"
                      + f"Топ 25: {top25}\n" + f"Убийства: {kills}\n" + f"Смерти: {deaths}\n" + f"КД: {kd}\n" + f"Матчей: {matches}\n" + f"Процент победы: {winRate}\n"
                      + f"Сыгранные минуты: {minutesPlayed}\n" + f"Игроков пережил: {playersOutlived}\n" + f"Последнее обновление: {lastModified}\n")
    
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        
root = tk.Tk()
root.geometry("400x500")
root.title("Fortnite Stats")
root.resizable (width=False, height=False)



label = ttk.Label(root, text='Введите ник в фортнайте:', font="Arial")
label.pack()

entry = ttk.Entry(root, width=30)
entry.pack(pady=10)

button = ttk.Button(root, text='Узнать', command=click)
button.pack(pady=5)

label1 = ttk.Label(root, text='Здесь будет ваша статистика', font="Arial")
label1.pack()



root.mainloop()
