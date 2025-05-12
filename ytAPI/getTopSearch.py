from ytAPI.youtube_client import build_youtube_client

def search_top_video( query : str ):

    youtube = build_youtube_client()

    try:

        request = youtube.search().list(
            q=query,
            part="snippet",
            type="video",
            maxResults=10
        )

        response = request.execute()

        if not response.get("items") : raise Exception( f"No results found for {query}" )

        top_result = response["items"][0]
        return top_result["id"]["videoId"]

    except Exception as e:

        raise Exception( f"An error occurred while searching for {query}: {e}" )