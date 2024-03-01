import os
import subprocess


project_path = os.path.abspath('hw9')
current_dir = os.path.dirname(os.path.realpath(__file__))


def run_spider(spider_name, output_file):
    full_output_path = os.path.join(current_dir, output_file)

    if os.path.exists(full_output_path):
        os.remove(full_output_path)

    command = [
        'scrapy',
        'crawl',
        spider_name,
        '-o',
        full_output_path
    ]
    subprocess.run(command, cwd=project_path, check=True)


if __name__ == '__main__':
    print('Starting the scraping process...')
    try:
        run_spider("quotes", "quotes.json")
        run_spider("authors", "authors.json")
        print('Scraping completed successfully.')
    except Exception as e:
        print(f"An error occurred: {e}")
