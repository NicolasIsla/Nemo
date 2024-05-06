import gdown
import zipfile
import os
import shutil
from dotenv import load_dotenv

load_dotenv()

def download_and_extract(url, destination):
    gdown.download(f"https://drive.google.com/uc?id={url}", destination, quiet=False)

    with zipfile.ZipFile(destination, 'r') as zip_ref:
        zip_ref.extractall(os.path.dirname(destination))
    os.remove(destination)

if __name__ == "__main__":
    path = os.getenv('PATH_DATASET')
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        # remove the existing directory
        shutil.rmtree(path)
        os.makedirs(path)

    file_urls = {
        'train': os.getenv("FILE_URL1_ID"),
        'val': os.getenv("FILE_URL2_ID"),
    }

    for dataset_id, url in file_urls.items():
        destination = os.path.join(path, f"file_{dataset_id}.zip")
        download_and_extract(url, destination)
        print(f"Dataset {dataset_id} downloaded and extracted successfully.")

   

