import requests


def search_unsplash_image(query):
    endpoint = "https://api.unsplash.com/photos/random"
    params = {"query": query, "client_id": "q5VDnibIsRvn6A6iRG73gfvidSdNysXm4dEQD8KhzgI"}
    response = requests.get(endpoint, params=params)
    data = response.json()
    if "urls" in data:
        image_url = data["urls"]["regular"]
        return image_url
    else:
        return None

# Replace 'YOUR_ACCESS_KEY' with your actual Unsplash API access key
# access_key = 'q5VDnibIsRvn6A6iRG73gfvidSdNysXm4dEQD8KhzgI'
# word_to_search = 'Athens'

# image_url = search_unsplash_image(word_to_search)

# if image_url:
# print(f"Image URL for '{word_to_search}': {image_url}")
# else:
# print(f"No image found for '{word_to_search}'")
