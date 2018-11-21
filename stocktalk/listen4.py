from scripts import settings, streaming

# Query keys categorize tweets
# Each key or category corresponds to an array of keywords
#queries = {'XBOX': ['XBOX', 'XBOX','XBOX One', 'XBOX 360'],
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
#           'JETS': ['JETS', 'NY Jets','New York Jets']
#           }

queries = {'COWBOYS': ['COWBOYS', 'Dallas Cowboys'],             
           'NFL': ['NFL', 'NFL','National Football','National Football League'],
           'GIANTS': ['GIANTS', 'NY Giants','New York Giants'],
           'JETS': ['JETS', 'NY Jets','New York Jets']
           }

# Aggregate volume and sentiment every 15 minutes
#refresh = 15*60
refresh = 1*60

streaming.streamer(settings.credentials, 
                   queries, 
                   refresh, 
                   sentiment=True, 
                   debug=True)
