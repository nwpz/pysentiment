from scripts import settings, streaming

# Query keys categorize tweets
# Each key or category corresponds to an array of keywords
queries = {'ETH': ['ETH', 'Ethereum'],
           'LTC': ['LTC', 'Litecoin'],
           'BTC': ['BTC', 'Bitcoin'],
           'XRP': ['XRP', 'Ripple'],
           'XLM': ['XLM', 'Stellar'],
           'THANKSGIVING': ['THANKSGIVING', '#Thanksgiving', 'turkey','turkeyday','thanksgiving'],
           'Brexit': ['BREXIT', 'Brexit', '#Brexit']
#           'FORD': ['FORD', 'Ford Motors'],
#           'AAPL': ['AAPL', 'Apple Computers'],
#           'GOOGL': ['GOOGL', 'Google'],
#           'TWTR': ['TWTR', 'Twitter'],           
#           'TSLA': ['TSLA', 'Tesla'],
#           'NFL': ['NFL', 'National Football League'],
#           'ELON': ['ELON', 'Elon Musk'],
#           'VW': ['VW', 'Volkswagen'],
#           'SP500': ['SP500', 'S&P 500','SPX'],
#           'DAX': ['DAX', 'DAX'],
#           'ORCL': ['ORCL', 'Oracle'],
#           'ANDROID': ['ANDROID', 'Android'],
#           'IOS': ['IOS', 'iOS','Apple iOS'],
#           'PYTHON': ['PYTHON', 'Python','Python 3.7'],
#           'DAYZ': ['DAYZ', 'DayZ','DayZ Standalone', 'DayZ SA'],
#           'PLAYSTATION': ['PLAYSTATION', 'Playstation','Sony Playstation'],
#           'TIKTOK': ['TIKTOK', 'Tik Tok','TikTok'],
#           'WF': ['WF', 'Wierd Flex'],
#           'ADAMLZ': ['ADAMLZ', 'Adam LZ','AdamLZ'],
#           'YTUBE': ['YTUBE', 'YouTube','You Tube'],
#           'DOTNETCORE': ['DOTNETCORE', '.NET Core','Dot Net Core','.NET Core 2.1', '.NET Core 2.2', '.Net Core 3'],
#           'XBOX': ['XBOX', 'XBOX','XBOX One', 'XBOX 360'],
#           'NINTENDO': ['NINTENDO', 'Nintendo','Wii', 'Nintendo Switch'],
#           'MEME': ['MEME', 'Meme','Dank Meme', 'Meme Review'],
#           'HEDGEFUNDS': ['HEDGEFUNDS', 'Hedge Funds','HedgeFunds'],
#           'MIFID': ['MIFID', 'MiFID II','Mifid','MiFIR','RTS 28','RTS28','APA','ARM'],
#           'CRYPTO': ['CRYPTO', 'Crypto','Crypto Currency'],
#           'BREXIT': ['BREXIT', 'Brexit'],
#           'DONALDTRUMP': ['DONALDTRUMP', 'Donald Trump','Donald Trump President','POTUS'],
#           'NORTHKOREA': ['NORTHKOREA', 'North Korea','Kim Jung Il'],
#           'CAMPFIRE': ['CAMPFIRE', 'Camp Wildfire','Camp Wild Fires','California Wild Fire'],
#           'FACEBOOK': ['FACEBOOK', 'Face Book', 'Facebook'],
#           'DESPACITO': ['DESPACITO', 'Despacito','Despacito 2', 'Despacito2'],
#           'MINECRAFT': ['MINECRAFT', 'MineCraft','Mine Craft'],
#           'THANKSGIVING': ['THANKSGIVING', 'Thanks Giving','Thanksgiving'],
#           'WIERDFLEX': ['WIERDFLEX', 'Wierd Flex','Wierd Flex but ok','Wierd Flex, but ok'],
#           'COWBOYS': ['COWBOYS', 'Dallas Cowboys'],
#           'GIANTS': ['GIANTS', 'NY Giants','New York Giants'],
#           'JETS': ['JETS', 'NY Jets','New York Jets'],


           }

# Aggregate volume and sentiment every 15 minutes
#refresh = 15*60
refresh = 1*60

streaming.streamer(settings.credentials, 
                   queries, 
                   refresh, 
                   sentiment=True, 
                   debug=True)
