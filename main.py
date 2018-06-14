#! /usr/bin/env python

from tube_scraper.scraper import youtube_search

def main():
    search_opts = {
        'order': 'viewCount',
        'max_results': 500,
        'published_Before':'2007-12-31T00:00:00Z',
        'published_After':'2006-12-31T00:00:00Z',
        'video_category_id': 29,
        'region_Code': 'GB',
       
        }
    results = youtube_search(search_opts, open("API_KEY.txt").read())

    # WHEN YOU ADD KEYS TO THE DETAILED FETCH AND WANT THEM
    # ADDED TO THE CSV, ADD THEM HERE
    keys = [
        'id',
        'title',
        'published',
        'viewCount',
        'likeCount',
        'dislikeCount',
        'favoriteCount',
        'commentCount',
        'duration',
    ]

    f = open("results.csv", "w")
    for result in results:
        line = []
        for key in keys:
            line.append(result[key])
        f.write((u'**'.join(line) + u'\n').encode('utf-8'))
    f.close()

if __name__ == '__main__':
    main()
