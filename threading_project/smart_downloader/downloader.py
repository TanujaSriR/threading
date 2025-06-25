import requests
import os
from tqdm import tqdm

def download_file(url, output_dir, logger):
    local_filename = os.path.join(output_dir, url.split('/')[-1])
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total = int(r.headers.get('content-length', 0))
            with open(local_filename, 'wb') as f, tqdm(
                desc=local_filename,
                total=total,
                unit='B',
                unit_scale=True
            ) as bar:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        bar.update(len(chunk))

        logger.info(f"Downloaded: {local_filename}")
        return local_filename
    except Exception as e:
        logger.error(f"Failed to download {url}: {e}")
        return None
