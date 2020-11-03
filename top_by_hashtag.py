from TikTokApi import TikTokApi
import pandas as pd

api = TikTokApi()

def simple_dict(tiktok_dict):
    to_return = {}
    to_return['user_id'] = tiktok_dict['author']['id']
    to_return['user_name'] = tiktok_dict['author']['uniqueId']
    to_return['user_id'] = tiktok_dict['author']['id']
    to_return['user_signature'] = tiktok_dict['author']['signature']
    to_return['user_verified'] = tiktok_dict['author']['verified']
    to_return['video_id'] = tiktok_dict['id']
    to_return['video_desc'] = tiktok_dict['desc']
    to_return['video_time'] = tiktok_dict['createTime']
    to_return['privateItem'] = tiktok_dict['privateItem']
    to_return['duetEnabled'] = tiktok_dict['duetEnabled']
    to_return['stitchEnabled'] = tiktok_dict['stitchEnabled']
    to_return['shareEnabled'] = tiktok_dict['shareEnabled']
    to_return['isAd'] = tiktok_dict['isAd']
    to_return['video_length'] = tiktok_dict['video']['duration']
    to_return['video_link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['user_name'], to_return['video_id'])       
    to_return['challenges_id'] = tiktok_dict['challenges'][0]['id']
    to_return['challenges_title'] = tiktok_dict['challenges'][0]['title']
    to_return['challenges_desc'] = tiktok_dict['challenges'][0]['desc']
    to_return['textExtra_awemeId'] = tiktok_dict['textExtra'][0]['awemeId']
    to_return['textExtra_userId'] = tiktok_dict['textExtra'][0]['userId']
    to_return['textExtra_userUniqueId'] = tiktok_dict['textExtra'][0]['userUniqueId']
    to_return['stats_likes'] = tiktok_dict['stats']['diggCount']
    to_return['stats_shares'] = tiktok_dict['stats']['shareCount']
    to_return['stats_comments'] = tiktok_dict['stats']['commentCount']
    to_return['stats_plays'] = tiktok_dict['stats']['playCount'] 
    to_return['authorstats_following'] = tiktok_dict['authorStats']['followingCount']
    to_return['authorstats_followers'] = tiktok_dict['authorStats']['followerCount']
    to_return['authorstats_heart'] = tiktok_dict['authorStats']['heartCount']
    to_return['authorstats_videos'] = tiktok_dict['authorStats']['videoCount']
    to_return['authorstats_diggs'] = tiktok_dict['authorStats']['diggCount']
    to_return['authorstats_hearts'] = tiktok_dict['authorStats']['heart']
    to_return['hashtags'] = tiktok_dict['challenges']
    to_return['extras'] = tiktok_dict['textExtra']
    to_return['raw'] = tiktok_dict
    to_return['music'] = tiktok_dict['music']
    
    
    return to_return


# posted by user
n_videos = 2000

hashtag = 'policelivesmatter'

videos_by_hashtag = api.byHashtag(hashtag, count=n_videos)
videos_by_hashtag = [simple_dict(v) for v in videos_by_hashtag]
videos_by_hashtag_df = pd.DataFrame(videos_by_hashtag)
videos_by_hashtag_df.to_csv('{}_videos.csv'.format(hashtag),index=False)
