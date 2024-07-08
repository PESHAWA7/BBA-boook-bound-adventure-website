from flask import Flask, render_template, request, redirect, url_for, flash, session
import json
from datetime import timedelta
import requests
import random
import datetime
import turtle

app = Flask(__name__)

app.secret_key = "ksksknxnbc"
end_point = "https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key=yourAPIKey"
SEARCH_1 = "world"
SEARCH_2 = "Business"
SEARCH_3 = "Sport"
SEARCH_4 = "Science"
SEARCH_5 = "Tech"
SEARCH_6 = "Health"

COPYRIGHT_TIME = datetime.datetime.now().year

endpoint_use = f"https://www.googleapis.com/books/v1/volumes?q={SEARCH_1}&key=yourAPIKey"
API_KEY = "AIzaSyBc5pWMjZJcE_ZS3yc6WYHy2KxWNffzjt0"
app.permanent_session_lifetime = timedelta(weeks=4)
search_data = None


def color():
    bootstrap_colors = ["primary", "success", "danger", "warning", "info", "secondary"]
    color_boot_1 = random.choice(bootstrap_colors)
    color_boot_2 = random.choice(bootstrap_colors)
    if color_boot_2 == color_boot_1:
        color_boot_2 = random.choice(bootstrap_colors)
    color_boot_3 = random.choice(bootstrap_colors)
    if color_boot_3 == color_boot_2:
        color_boot_3 = random.choice(bootstrap_colors)
    return color_boot_3, color_boot_2, color_boot_1


def get_quotes():
    API_KEY_2 = "7eK6Za7uBE3G6LoJ52dPrQ==kP8Vi0rHpbpPl2LH"
    category = 'dreams'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': f'{API_KEY_2}'})
    if response.status_code == requests.codes.ok:
        list1 = response.json()
        quote = list1[0]["quote"]
        author = list1[0]["author"]
        category = list1[0]["category"]
        return quote, author, category
    else:
        print("Error:", response.status_code, response.text)

@app.route(f'/{SEARCH_2}')
def Business():
    book_data = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q={SEARCH_2}&filter=free-ebooks&key={API_KEY}&maxResults=30")
    print(book_data.raise_for_status())

    book_data = book_data.json()
    books = book_data['items']

    some_random_book = [random.choice(books) for i in range(1, 9)]

    data_1 = some_random_book[0]["volumeInfo"]["title"]
    data_2 = some_random_book[1]["volumeInfo"]["title"]
    data_3 = some_random_book[2]["volumeInfo"]["title"]
    data_4 = some_random_book[3]["volumeInfo"]["title"]
    data_5 = some_random_book[4]["volumeInfo"]["title"]

    image_1 = some_random_book[0]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_2 = some_random_book[1]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_3 = some_random_book[2]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_4 = some_random_book[3]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_5 = some_random_book[4]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_6 = some_random_book[5]["volumeInfo"]["imageLinks"]["thumbnail"]

    images = [image_1, image_2, image_3, image_4, image_5, image_6]
    titles = [data_1, data_2, data_3, data_4, data_5]
    len_number = len(images)

    quote = get_quotes()[0]
    author = get_quotes()[1]
    category = get_quotes()[2]

    return render_template('home.html'
                           , images=images, titles=titles, len_number=len_number
                           , some_random_book=some_random_book
                           , color_boot_1=color()[0], color_boot_2=color()[1], color_boot_3=color()[2]
                           , quote=quote, author=author, category=category, COPYRIGHT_TIME=COPYRIGHT_TIME)


@app.route(f'/{SEARCH_3}')
def Sport():
    book_data = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q={SEARCH_3}&filter=free-ebooks&key={API_KEY}&maxResults=30")
    print(book_data.raise_for_status())

    book_data = book_data.json()
    books = book_data['items']

    some_random_book = [random.choice(books) for i in range(1, 9)]

    data_1 = some_random_book[0]["volumeInfo"]["title"]
    data_2 = some_random_book[1]["volumeInfo"]["title"]
    data_3 = some_random_book[2]["volumeInfo"]["title"]
    data_4 = some_random_book[3]["volumeInfo"]["title"]
    data_5 = some_random_book[4]["volumeInfo"]["title"]

    image_1 = some_random_book[0]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_2 = some_random_book[1]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_3 = some_random_book[2]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_4 = some_random_book[3]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_5 = some_random_book[4]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_6 = some_random_book[5]["volumeInfo"]["imageLinks"]["thumbnail"]

    images = [image_1, image_2, image_3, image_4, image_5, image_6]
    titles = [data_1, data_2, data_3, data_4, data_5]
    len_number = len(images)

    quote = get_quotes()[0]
    author = get_quotes()[1]
    category = get_quotes()[2]

    return render_template('home.html'
                           , images=images, titles=titles, len_number=len_number
                           , some_random_book=some_random_book
                           , color_boot_1=color()[0], color_boot_2=color()[1], color_boot_3=color()[2]
                           , quote=quote, author=author, category=category, COPYRIGHT_TIME=COPYRIGHT_TIME)

@app.route(f'/{SEARCH_4}')
def Science():
    book_data = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q={SEARCH_4}&filter=free-ebooks&key={API_KEY}&maxResults=30")
    print(book_data.raise_for_status())

    book_data = book_data.json()
    books = book_data['items']

    some_random_book = [random.choice(books) for i in range(1, 9)]

    data_1 = some_random_book[0]["volumeInfo"]["title"]
    data_2 = some_random_book[1]["volumeInfo"]["title"]
    data_3 = some_random_book[2]["volumeInfo"]["title"]
    data_4 = some_random_book[3]["volumeInfo"]["title"]
    data_5 = some_random_book[4]["volumeInfo"]["title"]

    image_1 = some_random_book[0]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_2 = some_random_book[1]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_3 = some_random_book[2]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_4 = some_random_book[3]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_5 = some_random_book[4]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_6 = some_random_book[5]["volumeInfo"]["imageLinks"]["thumbnail"]

    images = [image_1, image_2, image_3, image_4, image_5, image_6]
    titles = [data_1, data_2, data_3, data_4, data_5]
    len_number = len(images)

    quote = get_quotes()[0]
    author = get_quotes()[1]
    category = get_quotes()[2]

    return render_template('home.html'
                           , images=images, titles=titles, len_number=len_number
                           , some_random_book=some_random_book
                           , color_boot_1=color()[0], color_boot_2=color()[1], color_boot_3=color()[2]
                           , quote=quote, author=author, category=category, COPYRIGHT_TIME=COPYRIGHT_TIME)

@app.route(f'/{SEARCH_5}')
def Tech():
    book_data = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q={SEARCH_5}&filter=free-ebooks&key={API_KEY}&maxResults=30")
    print(book_data.raise_for_status())

    book_data = book_data.json()
    books = book_data['items']

    some_random_book = [random.choice(books) for i in range(1, 9)]

    data_1 = some_random_book[0]["volumeInfo"]["title"]
    data_2 = some_random_book[1]["volumeInfo"]["title"]
    data_3 = some_random_book[2]["volumeInfo"]["title"]
    data_4 = some_random_book[3]["volumeInfo"]["title"]
    data_5 = some_random_book[4]["volumeInfo"]["title"]

    image_1 = some_random_book[0]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_2 = some_random_book[1]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_3 = some_random_book[2]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_4 = some_random_book[3]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_5 = some_random_book[4]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_6 = some_random_book[5]["volumeInfo"]["imageLinks"]["thumbnail"]

    images = [image_1, image_2, image_3, image_4, image_5, image_6]
    titles = [data_1, data_2, data_3, data_4, data_5]
    len_number = len(images)

    quote = get_quotes()[0]
    author = get_quotes()[1]
    category = get_quotes()[2]

    return render_template('home.html'
                           , images=images, titles=titles, len_number=len_number
                           , some_random_book=some_random_book
                           , color_boot_1=color()[0], color_boot_2=color()[1], color_boot_3=color()[2]
                           , quote=quote, author=author, category=category)

@app.route(f'/{SEARCH_6}')
def Health():
    book_data = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q={SEARCH_6}&filter=free-ebooks&key={API_KEY}&maxResults=30")
    print(book_data.raise_for_status())

    book_data = book_data.json()
    books = book_data['items']

    some_random_book = [random.choice(books) for i in range(1, 9)]

    data_1 = some_random_book[0]["volumeInfo"]["title"]
    data_2 = some_random_book[1]["volumeInfo"]["title"]
    data_3 = some_random_book[2]["volumeInfo"]["title"]
    data_4 = some_random_book[3]["volumeInfo"]["title"]
    data_5 = some_random_book[4]["volumeInfo"]["title"]

    image_1 = some_random_book[0]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_2 = some_random_book[1]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_3 = some_random_book[2]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_4 = some_random_book[3]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_5 = some_random_book[4]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_6 = some_random_book[5]["volumeInfo"]["imageLinks"]["thumbnail"]

    images = [image_1, image_2, image_3, image_4, image_5, image_6]
    titles = [data_1, data_2, data_3, data_4, data_5]
    len_number = len(images)

    quote = get_quotes()[0]
    author = get_quotes()[1]
    category = get_quotes()[2]

    return render_template('home.html'
                           , images=images, titles=titles, len_number=len_number
                           , some_random_book=some_random_book
                           , color_boot_1=color()[0], color_boot_2=color()[1], color_boot_3=color()[2]
                           , quote=quote, author=author, category=category, COPYRIGHT_TIME=COPYRIGHT_TIME)

@app.route('/')
def home():
    book_data = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q={SEARCH_1}&filter=free-ebooks&key={API_KEY}&maxResults=30")
    print(book_data.raise_for_status())

    book_data = book_data.json()
    books = book_data['items']

    some_random_book = [random.choice(books) for i in range(1, 9)]

    data_1 = some_random_book[0]["volumeInfo"]["title"]
    data_2 = some_random_book[1]["volumeInfo"]["title"]
    data_3 = some_random_book[2]["volumeInfo"]["title"]
    data_4 = some_random_book[3]["volumeInfo"]["title"]
    data_5 = some_random_book[4]["volumeInfo"]["title"]

    image_1 = some_random_book[0]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_2 = some_random_book[1]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_3 = some_random_book[2]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_4 = some_random_book[3]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_5 = some_random_book[4]["volumeInfo"]["imageLinks"]["thumbnail"]
    image_6 = some_random_book[5]["volumeInfo"]["imageLinks"]["thumbnail"]

    images = [image_1, image_2, image_3, image_4, image_5, image_6]
    titles = [data_1, data_2, data_3, data_4, data_5]
    len_number = len(images)

    quote = get_quotes()[0]
    author = get_quotes()[1]
    category = get_quotes()[2]

    return render_template('home.html'
                           , images=images, titles=titles, len_number=len_number
                           , some_random_book=some_random_book
                           , color_boot_1=color()[0], color_boot_2=color()[1], color_boot_3=color()[2]
                           , quote=quote, author=author, category=category, COPYRIGHT_TIME=COPYRIGHT_TIME)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        session.permanent = True
        user_name = request.form['user_name']
        session['user_name'] = user_name

        new_data = {
            user_name: {
                "email": email,
                "password": password,
            }
        }

        if len(user_name) == 0 or len(password) == 0 or len(email) == 0:
            flash("Oops, Please make sure you haven't left any fields empty,", "error")
        else:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                flash("no data it will be created.", "error")
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                if user_name in session:
                    if password == data[user_name]["password"] and email == data[user_name]["email"]:
                        flash("You are already registered.", "success")
                        return redirect(url_for('user_page'))
                    else:
                        flash("Incorrect password, or email.", "error")
                else:
                    flash("You are not registered yet.", "error")
                    return redirect(url_for('user_page'))
            finally:
                flash('please if you have any issues contact the developer.')

    return render_template('login.html', COPYRIGHT_TIME=COPYRIGHT_TIME)


@app.route('/user', methods=["GET", "POST"])
def user_page():
    if "user_name" in session:
        user_name = session['user_name']
        flash("You are logged in, but your user name updated after 4 weeks !", "success")
        book_data = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q=bussnis&filter=free-ebooks&key={API_KEY}&maxResults=30")
        print(book_data.raise_for_status())

        book_data = book_data.json()
        books = book_data['items']

        some_random_book = [random.choice(books) for i in range(1, 9)]

        data_1 = some_random_book[0]["volumeInfo"]["title"]
        data_2 = some_random_book[1]["volumeInfo"]["title"]
        data_3 = some_random_book[2]["volumeInfo"]["title"]
        data_4 = some_random_book[3]["volumeInfo"]["title"]
        data_5 = some_random_book[4]["volumeInfo"]["title"]

        image_1 = some_random_book[0]["volumeInfo"]["imageLinks"]["thumbnail"]
        image_2 = some_random_book[1]["volumeInfo"]["imageLinks"]["thumbnail"]
        image_3 = some_random_book[2]["volumeInfo"]["imageLinks"]["thumbnail"]
        image_4 = some_random_book[3]["volumeInfo"]["imageLinks"]["thumbnail"]
        image_5 = some_random_book[4]["volumeInfo"]["imageLinks"]["thumbnail"]

        images = [image_1, image_2, image_3, image_4, image_5]
        titles = [data_1, data_2, data_3, data_4, data_5]

        len_number = len(images)

        return render_template('index.html',
                               user_name=user_name, images=images, titles=titles, len_number=len_number,
                               COPYRIGHT_TIME=COPYRIGHT_TIME)
    else:
        return redirect(url_for('login'))


@app.route('/search', methods=["GET", "POST"])
def search():
    search = request.form["search"]
    search_data = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={search}&key={API_KEY}&maxResults=30")
    print(search_data.raise_for_status())
    data = search_data.json()

    len_images = [data["items"][x]["volumeInfo"]["imageLinks"]["thumbnail"] for x in range(len(data["items"]))]

    len_number = range(len(data["items"]))

    data_title_1 = data["items"][0]["volumeInfo"]["title"]
    image_1 = data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]

    bootstrap_colors = ["primary", "success", "danger", "warning", "info", "secondary"]
    color_boot_1 = random.choice(bootstrap_colors)
    color_boot_2 = random.choice(bootstrap_colors)
    if color_boot_2 == color_boot_1:
        color_boot_2 = random.choice(bootstrap_colors)
    color_boot_3 = random.choice(bootstrap_colors)
    if color_boot_3 == color_boot_2:
        color_boot_3 = random.choice(bootstrap_colors)

    return render_template('search.html', search=search, data=data, len_number=len_number
                           , color_boot_1=color_boot_1, color_boot_2=color_boot_2, color_boot_3=color_boot_3
                           , COPYRIGHT_TIME=COPYRIGHT_TIME)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_name = request.form['username']
        email = request.form['email']
        password = request.form['password-i']
        confirm = request.form['password-ii']

        # book_data = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={search_for_book}'
        #                          f'&filter=free-ebooks&key={API_KEY}')

        new_data = {
            user_name: {
                "email": email,
                "password": password,
            }
        }

        if len(user_name) == 0 or len(password) == 0 and password != confirm:
            flash("Oops, Please make sure you haven't left any fields empty,"
                  " or passwords must be same.", "error")
        else:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                if user_name in data:
                    flash("You are already registered you can login now.", )
                    return redirect(url_for('login'))
                else:
                    data.update(new_data)
                    # Updating old data with new data

                    with open("data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)
                        flash("you have account now please sign in again. 1 more", "success")
                        return redirect(url_for('login'))
            finally:
                flash('please if you have any issues contact the developer.')

    return render_template("signup.html", COPYRIGHT_TIME=COPYRIGHT_TIME)
# Password.save(password=password, email=email, user_name=user_name)
# return redirect(url_for('login'))


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.pop('user_name', None)
    return redirect(url_for('login'))

# @app.route('/download', methods=['GET', 'POST'])
# def download():
#     # url = 'https://getbootstrap.com/docs/5.3/examples/'
#     # response = requests.get(url)
#     # soup = BeautifulSoup(response.text, 'html.parser')
#     # links = soup.find_all('a')
#     # print(links)
#     #
#     # link = links[0].get('href')
#     if request.method == "POST":
#         name1 = request.form['name1']
#         name2 = request.form['name2']
#
#     return render_template("download.html", name1=name1.filename, name2=name2.filename)


if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/user', methods=["GET", "POST"])
# def user_page():
#     return render_template('index.html')
