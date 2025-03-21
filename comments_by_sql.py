import sqlite3
import googleapiclient.discovery

# Function to get YouTube comments
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
            comments.append((author, comment, published_at))

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

# Function to save comments in SQLite database
def save_comments_to_db(comments, db_name="youtube_comments.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS comments (
                      author TEXT, 
                      comment TEXT, 
                      published_at TEXT)''')

    # Insert comments into the table
    cursor.executemany("INSERT INTO comments VALUES (?, ?, ?)", comments)

    conn.commit()
    conn.close()
    print(f"✅ Saved {len(comments)} comments to {db_name}")

if __name__ == "__main__":
    video_id = "GGJOC1FNqn8"  # Replace with the YouTube Video ID
    api_key = "AIzaSyAZdL9RUIMrHuvGHwNgmYp2EgeiVGAdkoU"  # Replace with your API Key

    comments = get_youtube_comments(video_id, api_key)
    save_comments_to_db(comments)
