⸻

📥 YouTube Comments Scraper

A simple Python tool to scrape comments from a YouTube video using the YouTube Data API and save them in CSV, JSON, or SQLite database formats.

⸻

✅ Features:

	•	Scrapes top-level comments from a YouTube video.
	•	Save comments in CSV, JSON, or SQLite database.
	•	Easy to customize video IDs and API keys.

⸻

📂 Project Structure:

File	Description

youtube_comments.py	Fetches comments and saves them to a CSV file.
comments_by_json.py	(Optional) Saves comments in a JSON file.
comments_by_sql.py	(Optional) Saves comments in a SQLite database.
requirements.txt	All required Python packages.
.gitignore	Excludes venv/, __pycache__/, .db, .csv, .json files from Git.



⸻

🚀 How to Run

1. Clone the repo:

       git clone <your-repo-url>
       cd <your-project-folder>

2. Create and activate virtual environment:
  
       python3 -m venv venv  
       source venv/bin/activate   # For Linux/Mac  
       venv\Scripts\activate      # For Windows  

3. Install dependencies:

       pip install -r requirements.txt

4. Add your YouTube API Key and video ID in the script you want to run:

       video_id = "YOUR_VIDEO_ID"
       api_key = "YOUR_API_KEY"

5. Run the script:
	•	For CSV export:

       python youtube_comments.py

	•	For JSON export:

        python comments_by_json.py

	•	For SQLite database export:

       python comments_by_sql.py



⸻

📦 Requirements

	•	Python 3.x
	•	google-api-python-client
	•	pandas (for CSV saving)

Install using:

    pip install google-api-python-client pandas



⸻

📜 Notes:

	•	Make sure you have an active YouTube Data API key from Google Cloud Console.
	•	API limits may apply based on your quota.

⸻
