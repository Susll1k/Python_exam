import requests
import json
import sqlite3
import random 
import datetime 

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "882a19a336msh2d87cb1285dd9a2p1ff906jsn685793001db2",
	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

response = requests.get(url, headers=headers)


with open('movies.json', 'w') as file:
    file.write(json.dumps(response.json(), indent=4))


# movies = response.json()
# for movie in movies:

#     name =movie.get('title', 'Unkhow')
#     genre=movie.get('genre', 'Unkhow')[0]
#     year=movie.get('year', 'Unkhow')
#     description=movie.get('description', 'Unkhow')
#     rating=float(movie.get('rating', 'Unkhow'))

#     name = name.replace('"', "'")
#     genre = genre.replace('"', "'")
#     description = description.replace('"', "'")



#     cursor.execute(f'INSERT INTO movies (name, genre, year, description, rating) VALUES("{name}", "{genre}", {year}, "{description}", {rating})')

#     connection.commit()

# cinemas=['Евразия Cinema7','Arman Asia Park','Arsenal','Chaplin Khan Shatyr','Chaplin Mega Silk Way']
# addres=['ул. Петрова, 24 А/1, ТЦ «Евразия-3», 3 этаж','пр. Кабанбай Батыра, 21 ТРЦ «Азия парк»','ул. Ы. Алтынсарина, 4','пр. Туран 37, ТРЦ «Хан Шатыр», 2 этаж', 'ТРЦ MEGA Silk Way (территория EXPO), 2 этаж, Chaplin MEGA Silk Way']

# i=0

# for cinema in cinemas:
#     cursor.execute(f'INSERT INTO cinemas (name, addres) VALUES("{cinema}", "{addres[i]}")')
#     i+=1
#     connection.commit()






 
# afishas = [ 
#     { 
#         'movie_id': 1, 
#         'cinema_id': 1, 
#         'price': 1000, 
#         'data': "2022-01-01", 
#         'time': "10:00:00", 
#         'capacity': 100, 
#     } 
# ] 
 
# start_date = datetime.date.today() 
# end_date = datetime.date(2024, 5, 30) 
# start_time = datetime.time(16, 0, 0) 
# end_time = datetime.time(0, 0, 0) 
 
# moves_id = [random.randint(1, 100) for i in range(1, 51)] 
# cinemas_id = [random.randint(1,5) for i in range(1, 51)] 
# price  = [random.randint(1000,5000) for i in range(1, 51)] 
 
# gap = int((end_date - start_date).total_seconds()) 
 
# dates = [start_date + datetime.timedelta(seconds=random.randint(0, gap)) for i in range(1, 51)] 
 
# times = [f'{random.randint(16, 23)}:{random.randint(0, 5)}0:00' for i in range(1, 51)] 
 
# capacity = [random.randint(50, 100) for i in range(1, 51)] 
 
# for i in range(0, 50): 
#     cursor.execute(f"INSERT INTO afisha (movie_id, cinema_id, price, date, time, capacity) VALUES ({moves_id[i]}, {cinemas_id[i]}, {price[i]}, {dates[i]}, '{times[i]}', {capacity[i]})" 
#     ) 
#     connection.commit()


# afishas = [i for i in range(1,51)]
# rooms = [random.randint(1,6) for i in range(1,51)]
# rows = [random.randint(1,16) for i in range(1,151)]
# columns = [random.randint(1,16) for i in range(1,151)]

# id=0
# for i in range(0, 150, 3):
#     cursor.execute(f'INSERT INTO place (afisha_id, room, row, seat) VALUES ({afishas[id]}, {rooms[id]}, {rows[i]}, {columns[i]})')
#     cursor.execute(f'INSERT INTO place (afisha_id, room, row, seat) VALUES ({afishas[id]}, {rooms[id]}, {rows[i+1]}, {columns[i+1]})')
#     cursor.execute(f'INSERT INTO place (afisha_id, room, row, seat) VALUES ({afishas[id]}, {rooms[id]}, {rows[i+2]}, {columns[i+2]})')
#     id+=1

#     connection.commit()

