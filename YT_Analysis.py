# import libraries
import os
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from googleapiclient.discovery import build
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment variable
API_KEY = os.getenv('API_KEY')

# Initialize API client
youtube = build("youtube", "v3", developerKey = API_KEY)

# Retrieve YT channels
def search_channels(youtube, query, max_results =1000):
    request = youtube.search().list(
        part='snippet',
        type='channel',
        q=query,
        regionCode='KE',
        maxResults=max_results
    )
    response = request.execute()
    channels = []
    for item in response['items']:
        data = {
            'channel_id': item['snippet']['channelId'],
            'channel_title': item['snippet']['title'],
            'description': item['snippet']['description']
        }
        channels.append(data)
    return pd.DataFrame(channels)


query = ('Kenya')
df_channels = search_channels(youtube, query)
df_channels.head()

# Get the channel statistics
def get_channel_stats(youtube, channel_ids):
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=','.join(channel_ids)
    )
    response = request.execute()    
    channels = []
    for item in response['items']:
        data = {
            'channel_id': item['id'],
            'channel_title': item['snippet']['title'],
            'subscribers': int(item['statistics'].get('subscriberCount', 0)),
            'views': int(item['statistics'].get('viewCount', 0)),
            'total_videos': int(item['statistics'].get('videoCount', 0)),
            'playlist_id': item['contentDetails']['relatedPlaylists']['uploads']
        }
        channels.append(data)
    return pd.DataFrame(channels)

# Get channel statistics for the channels retrieved from the search
channel_ids = df_channels['channel_id'].tolist()
df_channel_stats = get_channel_stats(youtube, channel_ids)
df_channel_stats.head()

# Search for channels in Kenya with the keyword 'education'
query = 'Kenya'
df_channels = search_channels(youtube, query)

# Retrieve statistics for the channels found
channel_ids = df_channels['channel_id'].tolist()
df_channel_stats = get_channel_stats(youtube, channel_ids)

# Display the combined data
df_combined = pd.merge(df_channels, df_channel_stats, on='channel_id')
df_combined.head()

# display info on the merged data
df_combined.info()

# Check for null values in our data frame
df_combined.isnull().sum()

# Analyze video count distribution
plt.Figure(figsize= (10, 6))
sns.histplot(df_channel_stats['total_videos'], bins = 30, kde = True)
plt.title("Distribution of Video Counts")
plt.xlabel('Total Videos')
plt.ylabel('Number of Channels')
plt.show()

# Analyzing subscriber trends
plt.figure(figsize= (10,6))
sns.scatterplot(x= 'subscribers', y= 'total_videos', data= df_combined)
plt.title('Subscriber Count VS Total Videos')
plt.xlabel('Subscriber')
plt.ylabel('Total Videos')
plt.show()

# Analysing engagement metrics
df_channel_stats['Avg_Views_Per_Video'] = df_combined['views'] / df_channel_stats['total_videos']

# plot the engagement metrics
plt.figure(figsize=(10, 6))
sns.scatterplot(x='subscribers', y='Avg_Views_Per_Video', data= df_channel_stats)
plt.title('Subscribers vs Average Views per Video')
plt.xlabel('Subscribers')
plt.ylabel('Average Views per Video')
plt.show()
