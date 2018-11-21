from scripts import settings, streaming

# Query keys categorize tweets
# Each key or category corresponds to an array of keywords
queries = {'ETH': ['ETH', 'Ethereum'],
           'LTC': ['LTC', 'Litecoin'],
           'BTC': ['BTC', 'Bitcoin'],
           'XRP': ['XRP', 'Ripple'],
           'XLM': ['XLM', 'Stellar'],
           'FORD': ['FORD', 'Ford Motors'],
           'AAPL': ['AAPL', 'Apple Computers'],
           'GOOGL': ['GOOGL', 'Google'],
           'TWTR': ['TWTR', 'Twitter'],           
           'TSLA': ['TSLA', 'Tesla'],
           'NFL': ['NFL', 'National Football League']
           }

# Aggregate volume and sentiment every 15 minutes
#refresh = 15*60
refresh = 1*60

streaming.streamer(settings.credentials, 
                   queries, 
                   refresh, 
                   sentiment=True, 
                   debug=True)
