from TikTokApi import TikTokApi
import pandas as pd
import glob, os

api = TikTokApi()


all_videos = pd.read_csv('original_duets.csv')

# which files should I parse?
file_list = []
for file in os.listdir('/Users/andreasipka/Desktop/TikTok/data/sound/'):
    if file.endswith('_sound.csv'):        
        file_list.append(int(file[:-10]))
        
n_videos = 500

music_ids = list(all_videos.music_id.value_counts().index)


for music_id in music_ids:
	if music_id not in file_list:
		print('doing: ', music_id)
		videos_by_sound = api.bySound(music_id, count=n_videos)
		videos_by_sound_raw = pd.DataFrame(videos_by_sound)
		videos_by_sound_raw.to_csv('data/sound/{}_sound.csv'.format(music_id),index=False)

