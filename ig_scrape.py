import requests
import json 

def get_insta_info(username):
    base_url = 'https://www.instagram.com/'
    profile_url = "https://www.instagram.com/api/v1/users/web_profile_info/?username="+ username
    headers = {
        'User-Agent': 'Instagram 219.0.0.12.117 Android'
    }
    response = requests.get(profile_url, headers=headers)
    data = json.loads(response.text)

    if response.status_code == 200:
        edge_followed_by_count = data['data']['user']['edge_followed_by']['count']
        edge_follow_count = data['data']['user']['edge_follow']['count']
        edge_owner_to_timeline_media_count = data['data']['user']['edge_owner_to_timeline_media']['count']

        print("edge_followed_by_count: {}".format(edge_followed_by_count))
        print("edge_follow_count: {}".format(edge_follow_count))
        print("edge_owner_to_timeline_media_count: {}".format(edge_owner_to_timeline_media_count))

    
username = input("enter username: ")

get_insta_info(username)

