
import requests
import random

API_KEY = "AIzaSyBc5pWMjZJcE_ZS3yc6WYHy2KxWNffzjt0"
#
# iteam = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# name = random.choice(item)
# # books = [iteam.choice(item) for item in range(1, 10)]
#
# print(books)

# import random
#
# mylist = [2, 1, 0]
#
# randommm = [random.choice(mylist) for i in range(3, 9)]
# print(randommm)


# book_data = requests.get(
#     f"https://www.googleapis.com/books/v1/volumes?q=flowers&filter=free-ebooks&key={API_KEY}&maxResults=30")
# print(book_data.raise_for_status())
#
# book_data = book_data.json()
# books = book_data['items']
#
# some_random_book = [random.choice(books) for i in range(1, 9)]
#
# data_1 = some_random_book[0]["volumeInfo"]["title"]
# data_2 = some_random_book[1]["volumeInfo"]["title"]
# data_3 = some_random_book[2]["volumeInfo"]["title"]
# data_4 = some_random_book[3]["volumeInfo"]["title"]
# data_5 = some_random_book[4]["volumeInfo"]["title"]
#
# print(data_1, data_2, data_3, data_4, data_5)

# x = range(1, 6),
# for x in range(1, 6),
# name_image = f"image_{x}", name_title = f"data_{x}"
# number = [1, 2, 3]
# for x in range(len(number)):
#     name_image = f"image_{x}"
#     name_title = f"data_{x}"
#     print(name_image)
#     print(name_title)

# import random
#
# book_data = requests.get(
#     f"https://www.googleapis.com/books/v1/volumes?q=bussnis&filter=free-ebooks&key={API_KEY}&maxResults=30")
# print(book_data.raise_for_status())
#
# book_data = book_data.json()
# books = book_data['items']
#
# some_random_book = [random.choice(books) for i in range(1, 9)]
#
# data_1 = some_random_book[0]["volumeInfo"]["title"]
# data_2 = some_random_book[1]["volumeInfo"]["title"]
# data_3 = some_random_book[2]["volumeInfo"]["title"]
# data_4 = some_random_book[3]["volumeInfo"]["title"]
# data_5 = some_random_book[4]["volumeInfo"]["title"]
#
# image_1 = some_random_book[0]["volumeInfo"]["imageLinks"]["thumbnail"]
# image_2 = some_random_book[1]["volumeInfo"]["imageLinks"]["thumbnail"]
# image_3 = some_random_book[2]["volumeInfo"]["imageLinks"]["thumbnail"]
# image_4 = some_random_book[3]["volumeInfo"]["imageLinks"]["thumbnail"]
# image_5 = some_random_book[4]["volumeInfo"]["imageLinks"]["thumbnail"]
#
# images = [image_1, image_2, image_3, image_4, image_5]
# for image in range(len(images)):
#     print(images[image]+" thts number"+str(image))\
# from bs4 import BeautifulSoup
# def download():
#     with open("templates/home.html", "r") as f:
#         soup = BeautifulSoup(f, "html.parser")
#     links = soup.find_all('a')[0]
#     print(links.find_all('p'))
#
#     # return render_template("download.html", name_book_choice=name_book_choice)
# download()

# search_data = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=java&key={API_KEY}&maxResults=30")
# print(search_data.raise_for_status())
# data = search_data.json()
#
# images = []
# number = 0
# len_images = [data["items"][x]["volumeInfo"]["imageLinks"]["thumbnail"] for x in range(len(data["items"]))]
# print(len(data["items"]))
#
# print(len_images)

# def color():
#     bootstrap_colors = ["primary", "success", "danger", "warning", "info", "secondary"]
#     color_boot_1 = random.choice(bootstrap_colors)
#     color_boot_2 = random.choice(bootstrap_colors)
#     if color_boot_2 == color_boot_1:
#         color_boot_2 = random.choice(bootstrap_colors)
#         print("worked 2")
#     color_boot_3 = random.choice(bootstrap_colors)
#     if color_boot_3 == color_boot_2:
#         color_boot_3 = random.choice(bootstrap_colors)
#         print("worked 3")
#     return color_boot_3, color_boot_2, color_boot_1
#
# print(color())
# print(color()[0])

# def get_quotes():
#     API_KEY_2 = "7eK6Za7uBE3G6LoJ52dPrQ==kP8Vi0rHpbpPl2LH"
#     category = 'dreams'
#     api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
#     response = requests.get(api_url, headers={'X-Api-Key': f'{API_KEY_2}'})
#     if response.status_code == requests.codes.ok:
#         list1 = response.json()
#         quote = list1[0]["quote"]
#         author = list1[0]["author"]
#         category = list1[0]["category"]
#         return quote, author, category
#     else:
#         print("Error:", response.status_code, response.text)
#
#
# print(get_quotes()[0])
# import datetime
# time_now = datetime.datetime.now()
# print(time_now.year)

# def kill_char(string, n): # n = position of which character you want to remove
#     begin = string[:n]    # from beginning to n (n not included)
#     end = string[n+1:]    # n+1 through end of string
#     return begin + end
#
# string = input("Enter a string: ")
# print (kill_char(string, 3)) # "M" removed


