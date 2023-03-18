# IP-Blocklist-Manager

## Introduction
This project is a simple tool that allows users to add an IP address to a blocklist. The tool retrieves the latest blocklist from a source URL, saves it to a local file, and allows the user to add an IP address to that file. The blocklists are saved in CSV format, with one IP address per line.

##Directory Structure
The project has the following directory structure:


![image](https://user-images.githubusercontent.com/79183768/226090564-a7b7c019-2c46-40d3-b817-83dd6364a8d2.png)


6 directories, 11 files 


blocklists: This directory contains the retriever.py file, which contains the BlocklistRetriever class responsible for retrieving the latest blocklist from the source URL and saving it to a local file.
config: This directory contains the config.py file, which contains the Config class responsible for storing the configuration parameters used by the tool.
data: This directory contains the saved blocklists in CSV format.
main.py: This is the main entry point of the tool, which prompts the user to add an IP address to the current day's blocklist.
Requirements
The following are the requirements for running the project:

Python 3.9 or higher
requests library

Installation and Usage
To use the tool, follow these steps:

Clone the repository to your local machine using the following command:
git clone https://github.com/krishnakumarbhat/IP-Blocklist-Manager.git

Install the required dependencies using the following command:

###pip install requests
Run the main.py file using the following command:

###python main.py

If you want to add an IP address to the current day's blocklist, enter 1 when prompted and then enter the IP address. Otherwise, just press Enter to exit the tool.
