#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options, developerKey):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=developerKey)

    # container for all the results
    search_results = []
    # the remaining results to fetch
    num_results_to_fetch = options['max_results']
    # the num of results we will fetch on this next query
    current_fetch_size = min(num_results_to_fetch, 50);

    # run the first query
    search_response = youtube.search().list(
        order=options['order'],
        videoCategoryId=options['video_category_id'],
        type="video",
        part="id,snippet",
        maxResults=current_fetch_size,
    ).execute()

    # update how many results we have left to fetch
    num_results_to_fetch = num_results_to_fetch - current_fetch_size
    # save the results to the main results container
    search_results = search_results + search_response.get("items", [])

    # run the query repeatedly until we fetch all that we wanted or
    # there are no more results
    while "nextPageToken" in search_response and num_results_to_fetch > 0:
        current_fetch_size = min(num_results_to_fetch, 50);
        search_response = youtube.search().list(
            pageToken=search_response.get("nextPageToken"),
            order=options['order'],
            videoCategoryId=options['video_category_id'],
            type="video",
            q=options['q'],
            part="id,snippet",
            maxResults=current_fetch_size,
        ).execute()
        num_results_to_fetch = num_results_to_fetch - current_fetch_size
        search_results = search_results + search_response.get("items", [])

    video_ids = []
    # Aggregate the video ids
    for search_result in search_results:
        if search_result["id"]["kind"] == "youtube#video":
            video_ids.append(search_result["id"]["videoId"])

    # now fetch the detailed results for each video_id
    detailed_results = []
    start = 0
    end = len(video_ids)
    while start < end:
        current_ids = video_ids[start:start + 50]
        start = start + len(current_ids)
        detailed_results = detailed_results + fetch_video_details(youtube, current_ids)
   
    return detailed_results


def fetch_video_details(youtube, video_ids):
    result = []
    video_response = youtube.videos().list(
        id=",".join(video_ids),
        part="id,snippet,statistics,contentDetails",
    ).execute()

    for video_result in video_response.get("items", []):
        result.append({
            'id': video_result["id"],
            'title': video_result["snippet"]["title"],
            'published': video_result["snippet"]["publishedAt"],
            'description': video_result["snippet"]["description"],
            'viewCount': video_result["statistics"]["viewCount"],
            'likeCount': video_result["statistics"]["likeCount"],
            'dislikeCount': video_result["statistics"]["dislikeCount"],
            'favoriteCount': video_result["statistics"]["favoriteCount"],
            'commentCount': video_result["statistics"]["commentCount"],
            'duration': video_result["contentDetails"]["duration"],
        })


    return result

def quick_add(x, y):
    return x + y
