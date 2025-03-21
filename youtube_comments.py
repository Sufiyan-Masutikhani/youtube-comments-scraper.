import googleapiclient.discovery
import pandas as pd

def get_youtube_comments(video_id, api_key):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    comments = []
    
    response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=100
    ).execute()

    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            published_at = item['snippet']['topLevelComment']['snippet']['publishedAt']
            comments.append([author, comment, published_at])

        if 'nextPageToken' in response:
            response = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=response['nextPageToken'],
                textFormat="plainText",
                maxResults=100
            ).execute()
        else:
            break

    return comments

def save_comments_to_csv(comments, filename="youtube_comments.csv"):
    df = pd.DataFrame(comments, columns=["Author", "Comment", "Published At"])
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Saved {len(comments)} comments to {filename}")

if __name__ == "__main__":
    video_id = "GGJOC1FNqn8"  # Replace with your YouTube video ID
    api_key = "AIzaSyAZdL9RUIMrHuvGHwNgmYp2EgeiVGAdkoU"  # Replace with your YouTube API key

    comments = get_youtube_comments(video_id, api_key)
    save_comments_to_csv(comments)
