import sqlite3


connection = sqlite3.connect('database.db')

cursor = connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS cinemas (id INTEGER PRIMARY KEY, name TEXT, addres TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, year INTEGER, description TEXT, rating REAL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS afisha (id INTEGER PRIMARY KEY, movie_id INTEGER, cinema_id INTEGER, price INTEGER, date DATE, time TIME, capacity INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS place (id INTEGER PRIMARY KEY, afisha_id INTEGER, room INTEGER, row INTEGER, seat INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS ticket (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, place_id INTEGER)')

create_table()



class User():
    def __init__(self):
        pass
    def set_name(self):
        while True:
            try:
                name=input('Напиши свое имя: ')
                if name.isdigit():
                    raise ValueError()
                break
            except:
                print('Ошибка!')
            
        self.name=name

class Tiket(User):
    def __init__(self):
        pass
    
    def show_cinemas(self, afishas):

        i=1
        while True:
            cursor.execute(f"SELECT name FROM cinemas WHERE id = {i}")
            print(f'\n{i}) {cursor.fetchall()[0][0]}\n')
            for afisha in afishas:
                if afisha[2] == i:
                    cursor.execute(f"SELECT name FROM movies WHERE id = {afisha[1]}")
                    print(f'{cursor.fetchall()[0][0]}, Дата и время: {afisha[4]}, {afisha[5]}, Стоимость: {afisha[3]}')
            i+=1
            if i == 6:
                break
        while True:
            try:
                cinema=int(input('Выбери кинотеатр (введи номер который указан рядом с названием нужного вам кинотеатра от 1 до 5): '))
                if cinema < 1:
                    print("Введи от 1 до 5")
                elif cinema > 5:
                    print("Введи от 1 до 5")
                else:
                    break
            except ValueError:
                print("Введи цифру")
        self.id_cinema=cinema
    
    def movie_selection(self, afishas):
        cursor.execute(f"SELECT name FROM cinemas WHERE id = {self.id_cinema}")
        print(f'\n{self.id_cinema}) {cursor.fetchall()[0][0]}')
        i=1
        list_id_movie=[]
        for afisha in afishas:
            if afisha[2] == self.id_cinema:
                cursor.execute(f"SELECT name FROM movies WHERE id = {afisha[1]}")
                name=cursor.fetchall()[0][0]
                print(f'{i}) {name}, Дата и время: {afisha[4]}, {afisha[5]}, Стоимость: {afisha[3]} \n')
                
                cursor.execute(f"SELECT genre FROM movies WHERE name = '{name}'")
                genre=cursor.fetchall()[0][0]

                cursor.execute(f"SELECT year FROM movies WHERE name = '{name}'")
                year=cursor.fetchall()[0][0]

                cursor.execute(f"SELECT description FROM movies WHERE name = '{name}'")
                description=cursor.fetchall()[0][0]

                cursor.execute(f"SELECT rating FROM movies WHERE name = '{name}'")
                rating=cursor.fetchall()[0][0]

                cursor.execute(f"SELECT id FROM movies WHERE name = '{name}'")
                id=cursor.fetchall()[0][0]
                list_id_movie.append(id)



                print(f'Description:\nGenre: {genre}\nYear: {year}\nDescription: {description}\nRating: {rating}\n')
                i+=1
        while True:
            try:
                movie=int(input(f'Выбери фильм (введи номер который указан рядом с названием нужного вам фильма от 1 до {i-1}): '))
                if movie < 1:
                    print(f"Введи от 1 до {i-1}")
                elif movie > i-1:
                    print(f"Введи от 1 до {i-1}")
                else:
                    break
            except ValueError:
                print("Введи цифру")
        self.id_movie=list_id_movie[movie-1]
        cursor.execute(f"SELECT id FROM afisha WHERE movie_id={self.id_movie} AND cinema_id = {self.id_cinema}")
        self.afisha_id=cursor.fetchall()[0][0]

    def place(self):
        cursor.execute(f"SELECT * FROM place WHERE afisha_id = {self.afisha_id}")
        places=cursor.fetchall()
        print(f'Зал: {places[0][2]}')
        i=1
        for place in places:
            print(f"{i}) Ряд: {place[3]}, Место: {place[4]}")
            i+=1
        while True:
            try:
                place=int(input(f'Выбери место (введи номер который указан рядом с понравившимся вам места от 1 до {len(places)}): '))
                if place < 1:
                    print(f"Введи от 1 до {len(places)}")
                elif place > len(places):
                    print(f"Введи от 1 до {len(places)}")
                else:
                    break
            except ValueError:
                print("Введи цифру")
        self.id_place=place
        
        


class Cheakout():
    def __init__(self) -> None:
        pass
    def creating_receipt(self):
        pass

print("\nПриветствую вас на TikeSusl!")
print('Здесь есть множество различных фильмов')
user=User()
tiket=Tiket()
user.set_name()
cursor.execute("SELECT * FROM afisha")
afishas = cursor.fetchall()
# print(afishas)

tiket.show_cinemas(afishas)
tiket.movie_selection(afishas)

print('Теперь выбери место!')
print('Вот все свободные места.')
tiket.place()




    

