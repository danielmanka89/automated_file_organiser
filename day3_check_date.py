import os
import datetime

filename = "photo_old.jpg"

timestamp = os.path.getmtime(filename)
print(f"Raw timestamp: {timestamp}")

readable_date = datetime.datetime.fromtimestamp(timestamp)
print(f"Readable date: {readable_date}")

date_folder = readable_date.strftime("%Y-%m-%d")
print(f"Folder name to use: {date_folder}")