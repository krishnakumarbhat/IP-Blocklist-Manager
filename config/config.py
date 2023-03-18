# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# class Config:
#     BLOCKLIST_URL = 'https://example.com/blocklist.csv'
#     BLOCKLIST_DIR = os.path.join(BASE_DIR, '..', 'data', 'blocklists')



import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# class Config:
#     BLOCKLIST_SOURCES = {
#         'example': 'https://example.com/blocklist.csv',
#         'another': 'https://another.com/blocklist.csv'
#     }
#     BLOCKLIST_DIR = os.path.join(BASE_DIR, '..', 'data', 'blocklists')
#     BLOCKLIST_FILENAME = 'blocklist.csv'
#     BLOCKLIST_SOURCE = 'example'  # Default source

#     @classmethod
#     def get_blocklist_url(cls):
#         source = cls.BLOCKLIST_SOURCES.get(cls.BLOCKLIST_SOURCE)
#         if source:
#             return source
#         else:
#             raise ValueError(f"Blocklist source '{cls.BLOCKLIST_SOURCE}' is not valid.")

class Config:
    BLOCKLIST_SOURCE_URL = "https://mcfp.felk.cvut.cz/publicDatasets/CTU-AIPP-BlackList/Latest/AIP-Alpha-latest.csv"
    BLOCKLIST_DIR = "data/blocklists"
    BLOCKLIST_RETENTION_DAYS = 30


# config = Config()
