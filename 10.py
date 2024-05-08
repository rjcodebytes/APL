from bing_image_downloader import downloader



# Define the search query

query_string = "one piece"



# Download images from Bing

downloader.download(query_string, limit=6, output_dir='dataset', adult_filter_off=True,  force_replace=False, timeout=60, verbose=True)

