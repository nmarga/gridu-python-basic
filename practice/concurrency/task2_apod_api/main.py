import os
from typing import List
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY", "")
APOD_ENDPOINT = os.getenv("APOD_ENDPOINT", "")
OUTPUT_IMAGES = os.getenv("OUTPUT_IMAGES", "")

def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> List:
    """Fetches list of APOD metadata from NASA API."""
    request_params = {
        "api_key": api_key,
        "start_date": start_date,
        "end_date": end_date
    }
    try:
        response = requests.get(APOD_ENDPOINT, timeout=10, params=request_params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching metadata: {e}")
        return []

def download_apod_images(metadata: list) -> None:
    """Downloads images from the metadata list, skip the other media type."""
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)

    for entry in metadata:
        if entry.get("media_type") != "image":
            print(f"Skip {entry.get('date')} with media type: {entry.get('media_type')}")
            continue

        image_url = entry.get("hdurl") or entry.get("url")
        date = entry.get("date")
        # Determine file extension and name
        extension = image_url.split(".")[-1].split("?")[0]
        file_name = f"{date}.{extension}"
        file_path = os.path.join(OUTPUT_IMAGES, file_name)

        print(f"Downloading {file_name}...")
        try:
            img_data = requests.get(image_url, timeout=10).content
            with open(file_path, 'wb') as handler:
                handler.write(img_data)
        except requests.exceptions.RequestException as e:
            print(f"Could not download {date}: {e}")

def main() -> None:
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    download_apod_images(metadata=metadata)


if __name__ == '__main__':
    main()
