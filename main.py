import os
import requests
import shutil
from urllib.parse import urlparse
from subprocess import call
from concurrent.futures import ThreadPoolExecutor
import random, string
try:
    shutil.rmtree("ts_files")
except Exception:
    pass
# Create a new folder
folder_name = "ts_files"
os.makedirs(folder_name, exist_ok=True)

# Read the file and extract the links
with open("vwvlvZm4", "r") as file:
    lines = file.readlines()
    ts_links = [line.strip() for line in lines if line.startswith("https://")]

total_links = len(ts_links)
fully_downloaded_files = 0


# Function to download a TS file
def download_ts_file(link, index):
    global fully_downloaded_files

    parsed_url = urlparse(link)
    filename = os.path.join(folder_name, f"segment{index + 1}.ts")
    with open(filename, "wb") as file:
        response = requests.get(link)
        file.write(response.content)

    fully_downloaded_files += 1
    percentage = (fully_downloaded_files / total_links) * 100
    print(f"Progress: {fully_downloaded_files}/{total_links} ({percentage:.2f}%)")


# Download TS files using multiple threads
with ThreadPoolExecutor() as executor:
    for index, link in enumerate(ts_links):
        executor.submit(download_ts_file, link, index)

print("Conversion completed successfully!")

print("processing\ncombining all the ts files")
os.chdir(folder_name)
os.system('cat *.ts > all.ts')
print("done with the combining\nnow converting to mp3")
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
output_file = f'output-{random_string}.mp3'
os.system(f'ffmpeg -i all.ts {output_file}')
print("done\ncleaning files")
# Step 6: Delete .ts files
for file in os.listdir('.'):
    if file.endswith('.ts'):
        os.remove(file)
os.rename(output_file, f'../{output_file}')
