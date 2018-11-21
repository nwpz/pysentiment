from scripts import settings, streaming

# Query keys categorize tweets
# Each key or category corresponds to an array of keywords
queries = {'ELON': ['ELON', 'Elon Musk'],
           'VW': ['VW', 'Volkswagen'],
           'SP500': ['SP500', 'S&P 500','SPX'],
           'DAX': ['DAX', 'DAX'],
           'ORCL': ['ORCL', 'Oracle'],
           'ANDROID': ['ANDROID', 'Android'],
           'IOS': ['IOS', 'iOS','Apple iOS'],
           'PYTHON': ['PYTHON', 'Python','Python 3.7'],
           }

# Aggregate volume and sentiment every 15 minutes
#refresh = 15*60
refresh = 1*60

streaming.streamer(settings.credentials, 
                   queries, 
                   refresh, 
                   sentiment=True, 
                   debug=True)
