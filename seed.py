import json
from datetime import datetime
from mongoengine import connect, DoesNotExist
from models import Author, Quote

# Підключення до бази даних
connect(
    host="mongodb+srv://user:Example12345@cluster8.w3d66gu.mongodb.net/hw9?retryWrites=true&w=majority&appName=Cluster8"
)

# Функція для зчитування даних з JSON файлу
def read_json_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return []
    except json.JSONDecodeError:
        print(f"Помилка при декодуванні JSON файлу {file_path}.")
        return []

# # Видалення всіх документів з колекції авторів
# Author.objects().delete()
# # Видалення всіх документів з колекції цитат
# Quote.objects().delete()

# Зчитування даних з файлів
authors_data = read_json_data('authors.json')
quotes_data = read_json_data('quotes.json')

# Завантаження даних у базу даних
for author_info in authors_data:
    try:
        born_date = datetime.strptime(author_info['born_date'], '%B %d, %Y')
        author = Author(
            fullname=author_info['fullname'],
            born_date=born_date,
            born_location=author_info['born_location'],
            description=author_info['description']
        )
        author.save()
    except (ValueError, KeyError) as e:
        print(f"Помилка при збереженні автора: {e}")

for quote_info in quotes_data:
    try:
        author = Author.objects.get(fullname=quote_info['author'])
        quote = Quote(
            author=author,
            quote=quote_info['quote'],
            tags=quote_info['tags']
        )
        quote.save()
    except DoesNotExist:
        print(f"Автора з іменем {quote_info['author']} не знайдено.")
    except (ValueError, KeyError) as e:
        print(f"Помилка при збереженні цитати: {e}")

# connect(
#     'mydatabase',
#     host="mongodb+srv://user:Example12345@cluster8.w3d66gu.mongodb.net/hw9?retryWrites=true&w=majority&appName=Cluster8"
# )
#
# with open('authors.json', 'r', encoding='utf-8') as f:
#     authors_data = json.load(f)
#
# with open('quotes.json', 'r', encoding='utf-8') as f:
#     quotes_data = json.load(f)
#
# for author_info in authors_data:
#     born_date = datetime.strptime(author_info['born_date'], '%B %d, %Y')
#     author = Author(
#         fullname=author_info['fullname'],
#         born_date=born_date,
#         born_location=author_info['born_location'],
#         description=author_info['description']
#     )
#     author.save()
#
# for quote_info in quotes_data:
#     author = Author.objects(fullname=quote_info['author']).first()
#     quote = Quote(
#         author=author,
#         quote=quote_info['quote'],
#         tags=quote_info['tags']
#     )
#     quote.save()
