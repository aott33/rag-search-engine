import json


def load_search_print(filepath, search_query):
    movie_data = load_movie_data(filepath)

    if not bool(movie_data):
        print("No movie data.")

    movies_found = search_movie_titles(movie_data, search_query)

    if len(movies_found) == 0:
        print("No match found.")

    print_movie_titles(movies_found)


def print_movie_titles(movies_found):
    max_len = 5
    movies_len = len(movies_found)

    if movies_len < max_len:
        max_len = movies_len

    for i in range(max_len):
        print(f"{i+1}. {movies_found[i]["title"]}")


def load_movie_data(filepath) -> dict:
    movie_data = {}
    try:
        with open(filepath, 'r') as f:
            movie_data = json.load(f)
        return movie_data
    except json.JSONDecodeError as e:
        print(f"JSON Load Error: {e}")
        return {}


def search_movie_titles(movie_data, search_query) -> list[dict]:
    movies_found = []

    for movie in movie_data["movies"]:
        movie_title = movie["title"].lower()
        if search_query in movie_title:
            movies_found.append(movie)

    movies_found_sorted = sorted(movies_found, key=lambda movie: movie["id"])

    return movies_found_sorted
