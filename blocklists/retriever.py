import csv
import datetime
import os
import requests
# from config import Config
from config.config import Config
# def download_blocklist():
#     # Create the blocklist directory if it doesn't exist
#     os.makedirs(Config.BLOCKLIST_DIR, exist_ok=True)

#     # Build the blocklist file path
#     now = datetime.datetime.now().strftime('%Y-%m-%d')
#     filename = f'{now}.csv'
#     filepath = os.path.join(Config.BLOCKLIST_DIR, filename)

#     # If the blocklist file already exists, don't download it again
#     if os.path.exists(filepath):
#         print(f'{filename} already exists, skipping download')
#         return

#     # Download the blocklist from the specified URL
#     response = requests.get(Config.BLOCKLIST_URL)
#     response.raise_for_status()

#     # Save the blocklist to the file
#     with open(filepath, 'w', newline='') as f:
#         writer = csv.writer(f)
#         for line in response.iter_lines():
#             writer.writerow(line.decode('utf-8').split(','))
    
#     print(f'{filename} downloaded successfully')


# import csv
# from config.config import Config


# class BlocklistRetriever:
#     def __init__(self):
#         self.config = Config()

#     def retrieve_blocklist(self):
#         # Read the CSV file from the local file system
#         blocklist_path = os.path.join(self.config.BLOCKLIST_DIR, '2023-03-16.csv')
#         with open(blocklist_path, 'r') as f:
#             reader = csv.reader(f)
#             blocklist = [row[0] for row in reader]

#         # Return the blocklist
#         return blocklist

#     def add_ip_to_blocklist(self, ip):
#         # Append the IP address to the CSV file
#         blocklist_path = os.path.join(self.config.BLOCKLIST_DIR, '2023-03-16.csv')
#         with open(blocklist_path, 'a') as f:
#             writer = csv.writer(f)
#             writer.writerow([ip])



# import requests
# import os
# from datetime import datetime, timedelta
# # from config import config
# # from config.config import BLOCKLIST_SOURCE_URL, BLOCKLIST_DIR, BLOCKLIST_RETENTION_DAYS


# def retrieve_latest_blocklist():
#     # Retrieve the latest blocklist from the source URL
#     response = requests.get(Config.BLOCKLIST_SOURCE_URL)

#     # Get the current date and format it as YYYY-MM-DD
#     current_date = datetime.utcnow().strftime("%Y-%m-%d")

#     # If the data/blocklists directory doesn't exist, create it
#     if not os.path.exists(Config.BLOCKLIST_DIR):
#         os.makedirs(Config.BLOCKLIST_DIR)

#     # Save the blocklist to a file in the data/blocklists directory
#     blocklist_filename = os.path.join(Config.BLOCKLIST_DIR, f"{current_date}.csv")
#     with open(blocklist_filename, "wb") as f:
#         f.write(response.content)

#     # Delete blocklists that are older than the retention period
#     retention_period = timedelta(days=Config.BLOCKLIST_RETENTION_DAYS)
#     oldest_allowed_date = datetime.utcnow() - retention_period
#     for filename in os.listdir(Config.BLOCKLIST_DIR):
#         if not filename.endswith(".csv"):
#             continue
#         file_date = datetime.strptime(filename[:-4], "%Y-%m-%d")
#         if file_date < oldest_allowed_date:
#             os.remove(os.path.join(Config.BLOCKLIST_DIR, filename))



import os
from datetime import datetime, timedelta
import csv
import requests
from config.config import Config

class BlocklistRetriever:
    def retrieve_latest_blocklist():
    # Retrieve the latest blocklist from the source URL
        response = requests.get(Config.BLOCKLIST_SOURCE_URL)
        data = response.content.decode('utf-8').splitlines()

    # Get the current date and format it as YYYY-MM-DD
        current_date = datetime.utcnow().strftime("%Y-%m-%d")

    # If the data/blocklists directory doesn't exist, create it
        if not os.path.exists(Config.BLOCKLIST_DIR):
            os.makedirs(Config.BLOCKLIST_DIR)

    # Check if a blocklist file already exists for today's date
        blocklist_filename = os.path.join(Config.BLOCKLIST_DIR, f"{current_date}.csv")
        if os.path.exists(blocklist_filename):
        # If the file already exists, append the new data to it
            with open(blocklist_filename, "a", newline="") as f:
                writer = csv.writer(f)
                for row in csv.reader(data):
                    writer.writerow(row)
        else:
        # If the file doesn't exist, create it and save the new data to it
            with open(blocklist_filename, "w", newline="") as f:
                writer = csv.writer(f)
                for row in csv.reader(data):
                    writer.writerow(row)

    # Delete blocklists that are older than the retention period
        retention_period = timedelta(days=Config.BLOCKLIST_RETENTION_DAYS)
        oldest_allowed_date = datetime.utcnow() - retention_period
        for filename in os.listdir(Config.BLOCKLIST_DIR):
            if not filename.endswith(".csv"):
                continue
            file_date = datetime.strptime(filename[:-4], "%Y-%m-%d")
            if file_date < oldest_allowed_date:
                os.remove(os.path.join(Config.BLOCKLIST_DIR, filename))

