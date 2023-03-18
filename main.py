# import requests
# import os
# import datetime

# # Set the source URL for the blocklist
# SOURCE_URL = "https://mcfp.felk.cvut.cz/publicDatasets/CTU-AIPP-BlackList/Latest/AIP-Alpha-latest.csv"

# # Set the directory where the blocklists will be saved
# SAVE_DIR = "blocklists"

# # Create the save directory if it doesn't exist
# if not os.path.exists(SAVE_DIR):
#     os.makedirs(SAVE_DIR)

# # Generate a filename based on the current date
# filename = datetime.datetime.now().strftime("%Y-%m-%d.csv")

# # Check if the file already exists
# if os.path.exists(os.path.join(SAVE_DIR, filename)):
#     print("Today's blocklist has already been saved.")
# else:
#     # Download the blocklist from the source URL
#     response = requests.get(SOURCE_URL)

#     # Save the blocklist to a file
#     with open(os.path.join(SAVE_DIR, filename), "wb") as f:
#         f.write(response.content)

#     print(f"Blocklist saved to {os.path.join(SAVE_DIR, filename)}")

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--source-url", default=SOURCE_URL, help="URL of the blocklist source")
# args = parser.parse_args()

# SOURCE_URL = args.source_url



# from blocklist.retriever import download_blocklist
# from config.config import Config

# if __name__ == '__main__':
#     url = Config.BLOCKLIST_URL
#     output_dir = Config.BLOCKLIST_DIR
#     download_blocklist(url, output_dir)

# import argparse
# import csv

# def get_args():
#     parser = argparse.ArgumentParser(description='Block distracting websites')
#     parser.add_argument('-s', '--sites', type=str, help='path to CSV file containing list of websites to block')
#     parser.add_argument('-t', '--time', type=int, default=25, help='time to block websites (in minutes)')
#     return parser.parse_args()

# def block_websites(sites, time):
#     with open(sites, 'r') as f:
#         reader = csv.reader(f)
#         websites = list(reader)
#     print('Blocking websites...')
#     # add code here to block websites
#     print(f'Websites blocked for {time} minutes')

# if __name__ == '__main__':
#     args = get_args()
#     block_websites(args.sites, args.time)


# from blocklists.retriever import download_blocklist

# if __name__ == '__main__':
#     download_blocklist()

# from blocklist.retriever import BlocklistRetriever

# if __name__ == '__main__':
#     retriever = BlocklistRetriever()

#     # Retrieve the blocklist
#     blocklist = retriever.retrieve_blocklist()
#     print(f'Blocklist: {blocklist}')

#     # Add an IP address to the blocklist
#     ip = '192.168.1.1'
#     retriever.add_ip_to_blocklist(ip)
#     print(f'Added {ip} to blocklist')

#     # Retrieve the updated blocklist
#     blocklist = retriever.retrieve_blocklist()
#     print(f'Updated blocklist: {blocklist}')

# import os
# import csv
# from blocklists.retriever import BlocklistRetriever
from config.config import Config

# # Create an instance of the BlocklistRetriever class
# blocklist_retriever = BlocklistRetriever()

# # Retrieve the current blocklist
# current_blocklist = blocklist_retriever.retrieve_blocklist()
# print(f'Current blocklist: {current_blocklist}')

# # Ask the user for an IP address to add to the blocklist
# ip_address = input('Enter IP address to block: ')

# # Add the IP address to the blocklist
# blocklist_retriever.add_ip_to_blocklist(ip_address)
# print(f'{ip_address} added to blocklist')

# # Retrieve the updated blocklist
# updated_blocklist = blocklist_retriever.retrieve_blocklist()
# print(f'Updated blocklist: {updated_blocklist}')


import csv
import os
import shutil
import requests
from datetime import datetime, timedelta
# from blocklists.retriever import BlocklistRetriever
# from config import Config
# from blocklists import BlocklistRetriever


# def main():
#     retriever.retrieve_latest_blocklist()


# if __name__ == "__main__":
#     main()



# from blocklists.retriever import BlocklistRetriever

# def main():
#     retriever = BlocklistRetriever()
#     retriever.retrieve_latest_blocklist()

#     # Prompt user to enter an IP address to block
#     ip_address = input("Enter an IP address to block: ")

#     # Add the IP address to the blocklist file for the current date
#     blocklist_filename = retriever.get_blocklist_filename()
#     with open(blocklist_filename, "a") as f:
#         f.write(ip_address + "\n")

# if __name__ == "__main__":
#     main()

from blocklists.retriever import *
# from blocklists.retriever import BlocklistRetriever.retrieve_latest_blocklist

from config.config import Config

def main():
    BlocklistRetriever.retrieve_latest_blocklist()

    # Prompt user to enter an IP address to block
    ip_address = input("Enter an IP address to block: ")

    # Add the IP address to the blocklist file for the current date
    current_date = datetime.utcnow().strftime("%Y-%m-%d")
    blocklist_filename = os.path.join(Config.BLOCKLIST_DIR, f"{current_date}.csv")
    with open(blocklist_filename, "a") as f:
        f.write(ip_address + "\n")

if __name__ == "__main__":
    main()












































# class BlocklistRetriever:
#     def __init__(self, source_url):
#         self.config = Config()
#         self.source_url = source_url

#     def retrieve_blocklist(self):
#         # Check if a blocklist for today already exists
#         blocklist_path = os.path.join(self.config.BLOCKLIST_DIR, f'{datetime.now():%Y-%m-%d}.csv')
#         if os.path.exists(blocklist_path):
#             print(f"A blocklist for today already exists at {blocklist_path}. Skipping retrieval.")
#             with open(blocklist_path, 'r') as f:
#                 reader = csv.reader(f)
#                 blocklist = [row[0] for row in reader]
#             return blocklist

#         # Otherwise, download the blocklist from the source URL
#         response = requests.get(self.source_url)
#         if response.status_code != 200:
#             raise Exception(f"Failed to retrieve blocklist from {self.source_url}. Status code: {response.status_code}")
#         blocklist_data = response.text.strip().split('\n')

#         # Write the blocklist to a file for today
#         with open(blocklist_path, 'w') as f:
#             writer = csv.writer(f)
#             for row in blocklist_data:
#                 writer.writerow([row])

#         # Return the blocklist
#         return blocklist_data

#     def add_ip_to_blocklist(self, ip):
#         # Append the IP address to today's blocklist file
#         blocklist_path = os.path.join(self.config.BLOCKLIST_DIR, f'{datetime.now():%Y-%m-%d}.csv')
#         with open(blocklist_path, 'a') as f:
#             writer = csv.writer(f)
#             writer.writerow([ip])


# if __name__ == '__main__':
#     source_url = Config.BLOCKLIST_URL

#     # Retrieve the blocklist from the source
#     blocklist_retriever = BlocklistRetriever(source_url)
#     blocklist = blocklist_retriever.retrieve_blocklist()

#     # Add an IP address to the blocklist
#     blocklist_retriever.add_ip_to_blocklist('192.168.0.1')

#     # Copy the blocklist file to yesterday's file, if it exists
#     yesterday = datetime.now() - timedelta(days=1)
#     yesterday_path = os.path.join(Config.BLOCKLIST_DIR, f'{yesterday:%Y-%m-%d}.csv')
#     if os.path.exists(yesterday_path):
#         shutil.copy(yesterday_path, os.path.join(Config.BLOCKLIST_DIR, f'{yesterday:%Y-%m-%d}-backup.csv'))
