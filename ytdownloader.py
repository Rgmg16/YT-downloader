from pytube import YouTube

def download_video(url, path):
    try:
        # Create YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Print video details
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")
        print(f"Duration: {yt.length} seconds")

        # Download video
        stream.download(output_path=path)
        print(f"Downloaded '{yt.title}' successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get user input for video URL and download path
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (leave empty for current directory): ")

    # Set default path if empty
    if not download_path:
        download_path = "."

    # Download the video
    download_video(video_url, download_path)
