import json
from datetime import datetime
from mongoengine import connect, DoesNotExist
from models import Author, Quote


# Flag indicating whether to clear the table before inserting new data
CLEAR_TABLE_BEFORE_INSERT = True

connect(
    host="mongodb+srv://user:Example12345@cluster8.w3d66gu.mongodb.net/hw9?retryWrites=true&w=majority&appName=Cluster8"
)


def read_json_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON file {file_path}.")
        return []


def insert_authors_to_bd(authors_data):
    if CLEAR_TABLE_BEFORE_INSERT:
        Author.objects().delete()

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
            print(f"Error inserting author: {e}")


def insert_quotes_to_bd(quotes_data):
    if CLEAR_TABLE_BEFORE_INSERT:
        Quote.objects().delete()

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
            print(f"Author with name {quote_info['author']} not found.")
        except (ValueError, KeyError) as e:
            print(f"Error saving quote: {e}")


if __name__ == '__main__':

    authors_data = read_json_data('authors.json')
    quotes_data = read_json_data('quotes.json')

    insert_authors_to_bd(authors_data)
    insert_quotes_to_bd(quotes_data)
