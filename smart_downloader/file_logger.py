import logging

def setup_logger():
    logging.basicConfig(
        filename='download_log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger('DownloadLogger')
