from scripts import settings, streaming

# Query keys categorize tweets
# Each key or category corresponds to an array of keywords
queries = {'DAYZ': ['DAYZ', 'DayZ','DayZ Standalone', 'DayZ SA'],
           'PLAYSTATION': ['PLAYSTATION', 'Playstation','Sony Playstation'],
           'TIKTOK': ['TIKTOK', 'Tik Tok','TikTok'],
           'WF': ['WF', 'Wierd Flex'],
           'ADAMLZ': ['ADAMLZ', 'Adam LZ','AdamLZ'],
           'YTUBE': ['YTUBE', 'YouTube','You Tube'],
           'DOTNETCORE': ['DOTNETCORE', '.NET Core','Dot Net Core','.NET Core 2.1', '.NET Core 2.2', '.Net Core 3']
           }

# Aggregate volume and sentiment every 15 minutes
#refresh = 15*60
refresh = 1*60

streaming.streamer(settings.credentials, 
                   queries, 
                   refresh, 
                   sentiment=True, 
                   debug=True)
