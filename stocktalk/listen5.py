from scripts import settings, streaming

# Query keys categorize tweets
# Each key or category corresponds to an array of keywords
queries = { 'DESPACITO': ['DESPACITO', 'Despacito','Despacito 2', 'Despacito2'],
            'MINECRAFT': ['MINECRAFT', 'MineCraft','Mine Craft'],
            'THANKSGIVING': ['THANKSGIVING', 'Thanks Giving','Thanksgiving'],
            'WIERDFLEX': ['WIERDFLEX', 'Wierd Flex','Wierd Flex but ok','Wierd Flex, but ok'],
            'COWBOYS': ['COWBOYS', 'Dallas Cowboys'],
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