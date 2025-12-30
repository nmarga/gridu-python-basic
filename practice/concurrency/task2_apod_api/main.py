import os
from typing import List
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY", "")
APOD_ENDPOINT = os.getenv("APOD_ENDPOINT")
OUTPUT_IMAGES = os.getenv("OUTPUT_IMAGES")

def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> List:
    return []


def download_apod_images(metadata: list) -> None:
    pass


def main() -> None:
    print(API_KEY)
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    download_apod_images(metadata=metadata)


if __name__ == '__main__':
    main()
