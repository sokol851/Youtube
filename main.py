import os
from utils import get_youtube_data, create_database, save_data_to_database
from config import config


def main():
    api_key = os.getenv('YT_API_KEY')
    channel_ids = [
        'UCf31Gf5nCU8J6eUlr7QSU0w',  # Marmok
        'UC746FHtnsAzDgF1diWwf-6A',  # Lekarok
    ]
    params = config()

    data = get_youtube_data(api_key, channel_ids)
    create_database('youtube', params)
    save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()
