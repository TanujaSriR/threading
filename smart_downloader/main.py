import threading
from downloader import download_file
from file_logger import setup_logger
from checksum import calculate_checksum
import os

DOWNLOAD_DIR = "downloads"
CHECKSUM_ALGO = "md5"

logger = setup_logger()

def worker(url):
    file_path = download_file(url, DOWNLOAD_DIR, logger)
    if file_path:
        checksum = calculate_checksum(file_path, CHECKSUM_ALGO)
        logger.info(f"Checksum ({CHECKSUM_ALGO}) for {file_path}: {checksum}")

def main():
    with open("download_list.txt") as f:
        urls = [line.strip() for line in f if line.strip()]

    threads = []
    for url in urls:
        t = threading.Thread(target=worker, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("All downloads completed.")

if __name__ == "__main__":
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    main()
