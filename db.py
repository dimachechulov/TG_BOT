import sqlite3

class Sqliter:
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.db.cursor()

    def db_table_val(self, user_id, user_name, user_register):
        self.cursor.execute('INSERT INTO users (user_id, user_name, user_register) VALUES (?, ?, ?)', (user_id, user_name, user_register))
        self.db.commit()

    def update_domain(self, domain):
        self.cursor.execute("SELECT * FROM collections_films")
        collections_films = self.cursor.fetchall()
        print(len(collections_films))
        data = [(collections_film[1], collections_film[5].split('/embed/')[1]) for collections_film in collections_films if not collections_film[5].startswith(domain)]
        data = list(set(data))
        print(len(data))
        for collections_film in data:
            domain_url_l = collections_film[1]
            domain_url = domain+'/embed/'+domain_url_l
            # print(domain_url)
            self.update_iframe_url(collections_film[0], domain_url)
        self.cursor.execute("SELECT * FROM favorites")
        favorite_films = self.cursor.fetchall()
        data2 = [(favorite_film[0], favorite_film[5].split('/embed/')[1]) for favorite_film in favorite_films if not favorite_film[5].startswith(domain)]
        data2 = list(set(data2))
        print(len(data2))
        for favorite_film in data2:
            domain_url_l = favorite_film[1]
            domain_url = domain+'/embed/'+domain_url_l
            # print(domain_url)
            self.update_favorite_url(favorite_film[0], domain_url)

    def update_iframe_url(self,id, domain):
        self.cursor.execute("UPDATE collections_films SET url = ? WHERE id = ?", (domain, id))
        self.db.commit()

    def update_favorite_url(self,id, domain):
        self.cursor.execute("UPDATE favorites SET url = ? WHERE film_id = ?", (domain, id))
        self.db.commit()

    def get_films(self, collection_id: int):
        self.cursor.execute("SELECT * FROM collections_films WHERE collection_id = ?", (collection_id,))
        collections_films = self.cursor.fetchall()
        return collections_films

    def get_film_by_id(self, film_id: int):
        self.cursor.execute("SELECT * FROM collections_films WHERE id = ?", (film_id,))
        first_film = self.cursor.fetchall()
        return first_film


    def get_users_day_reg(self, date):
        self.cursor.execute(f"SELECT user_id FROM users WHERE user_register = ?", (date,))
        result = self.cursor.fetchall()
        return len(result)

    def get_favorites(self, user_id):
        self.cursor.execute(f"SELECT * FROM favorites WHERE user_id = ?", (user_id,))
        result = self.cursor.fetchall()
        return result




    def add_favorite(self, data: list):
        self.cursor.execute('INSERT INTO favorites (film_id, user_id, name, date, genre, url, poster, type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', data)
        self.db.commit()

    def del_favorite(self, film_id):
        self.cursor.execute('DELETE FROM films WHERE film_id = ?', (film_id,))
        self.db.commit()



    def add_film(self,data):
        self.cursor.execute('INSERT INTO films (code, name, date, dlitel, description, poster) VALUES (?, ?, ?, ?, ?, ?)',data)
        self.db.commit()

    def get_film(self,film_id):
        self.cursor.execute(f"SELECT * FROM films WHERE code = ?", (film_id,))  # поменять бд
        result = self.cursor.fetchall()
        return result

    def get_film1(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(code as INTEGER) as code FROM films")
        codes = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(name as TEXT) as name FROM films")
        names = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(date as TEXT) as date FROM films")
        dates = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(dlitel as TEXT) as dlitel FROM films")
        genres = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(description as TEXT) as description FROM films")
        urls = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(poster as TEXT) as poster FROM films")
        posters = [row[0] for row in cur.fetchall()]
        data = []
        for i in range(len(codes)):
            temp = []
            temp.append(codes[i])
            temp.append(names[i])
            temp.append(dates[i])
            temp.append(genres[i])
            temp.append(urls[i])
            temp.append(posters[i])
            data.append(temp)
        return data

    def del_film(self, film_id):
        films = self.get_film1()
        error = True
        for film in films:
            if film[0]==int(film_id):
                error = False
        if(error):
            raise IOError("Такого нет")
        self.cursor.execute('DELETE FROM films WHERE code = ?', (film_id,))
        self.db.commit()

    def add_series(self,data):
        self.cursor.execute('INSERT INTO series (code, name, date, dlitel, description, poster) VALUES (?, ?, ?, ?, ?, ?)',data)
        self.db.commit()

    def get_series(self,serial_id):
        self.cursor.execute(f"SELECT * FROM series WHERE code = ?", (serial_id,))#поменять бд
        result = self.cursor.fetchall()
        return result

    def get_series1(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(code as INTEGER) as code FROM series")
        codes = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(name as TEXT) as name FROM series")
        names = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(date as TEXT) as date FROM series")
        dates = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(dlitel as TEXT) as dlitel FROM series")
        genres = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(description  as TEXT) as description FROM series")
        urls = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(poster as TEXT) as poster FROM series")
        posters = [row[0] for row in cur.fetchall()]
        data = []
        for i in range(len(codes)):
            temp = []
            temp.append(codes[i])
            temp.append(names[i])
            temp.append(dates[i])
            temp.append(genres[i])
            temp.append(urls[i])
            temp.append(posters[i])
            data.append(temp)
        return data
    def del_series(self, series_id):
        series = self.get_series1()
        print(series)
        error = True
        for ser in series:
            if ser[0]==int(series_id):
                print("YEs")
                error = False
        if(error):
            print("YEsss")
            raise IOError("Такого нет")
        self.cursor.execute('DELETE FROM series WHERE code = ?', (series_id,))
        self.db.commit()

    def add_chanel(self,data):
        print(data)
        self.cursor.execute('INSERT INTO chanels (name,id,url) VALUES (?,?,?)',data)
        self.db.commit()
    def get_chanels(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(name as TEXT) as name FROM chanels")
        names = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(id as INTEGER) as id FROM chanels")
        ids = [row[0] for row in cur.fetchall()]
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(url as TEXT) as url FROM chanels")
        urls = [row[0] for row in cur.fetchall()]
        data = []
        for i in range(len(ids)):
            temp = []
            temp.append(names[i])
            temp.append(ids[i])
            temp.append(urls[i])
            data.append(temp)
        return data

    def del_chanel(self, chanel_id):
        chanels = self.get_chanels()
        error = True
        for ser in chanels:
            if ser[1] == int(chanel_id):
                error = False
        if (error):
            raise IOError("Такого нет")
        self.cursor.execute('DELETE FROM chanels WHERE id = ?', (chanel_id,))
        self.db.commit()

    def get_admins(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        with con:
            cur = con.cursor()
            cur.execute("SELECT cast(id as INTEGER) as id FROM admins")
        users_id = [row[0] for row in cur.fetchall()]
        return users_id
    def add_admin(self,id_admin):
        self.cursor.execute('INSERT INTO admins (id) VALUES (?)',id_admin)
        self.db.commit()

    def del_admin(self, admin_id):
        data = self.get_admins()
        error = True
        print(data)
        for item in data:
            if item == int(admin_id):
                error = False
        if(error):
            raise IOError("Такого нет")
        self.cursor.execute('DELETE FROM admins WHERE id = ?', (admin_id,))
        self.db.commit()

    def insert_telegram_link(link):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (list_channels) VALUES (?)", (link,))
        conn.commit()

    def check_subscription(user_id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(
            "SELECT link FROM telegram_links WHERE link IN (SELECT channel_link FROM subscriptions WHERE user_id=?)",
            (user_id,))
        links = c.fetchall()
        conn.close()
        if links:
            return True
        else:
            return False

