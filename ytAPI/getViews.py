from ytAPI.youtube_client import build_youtube_client

def get_video_views( video_id : str ):

    youtube = build_youtube_client()
    
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    response = request.execute()

    if response.get("items"):

        view_count = int(response["items"][0]["statistics"]["viewCount"])
        return view_count

    else:

        print(f"Video with ID {video_id} not found.")
        return None