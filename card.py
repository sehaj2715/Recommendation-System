from request import genres
from utils import runtimeConvert, dateConvert, currencyConvert


def trendingCard(data):
    print(f"Id ---- {data["id"]}")
    if "media_type" in data:
        print(f"Type ---- {data["media_type"]}")
    if "name" in data:
        print(f"Name ---- {data["name"]}")
    elif "title" in data:
        print(f"Name ---- {data["title"]}")

    print(f"Overview ---- {data["overview"]}")
    genresList = ""
    for genre_id in data["genre_ids"]:
        genresList += f"{genres[str(genre_id)]} "
    print(f"Genres ---- {genresList}")
    if "release_date" in data:
        print(f"Release Year ---- {data["release_date"][:4]}")
    elif "first_air_date" in data:
        print(f"Release Year ---- {data["first_air_date"][:4]}")
    print("\n")

def movieCard(data):
    print(f"Id ---- {data["id"]}")
    print(f"Title ---- {data["original_title"]}")
    genresList = ""
    for genre in data["genres"]:
        genresList += f"{genre["name"]} "
    print(f"Genres ---- {genresList}")
    print(f"Overview ---- {data["overview"]}")
    runtimeConvert(int(data["runtime"]))
    dateConvert(data["release_date"])
    print(f"Budget ---- {currencyConvert(data["budget"])}")
    print(f"Revenue ---- {currencyConvert(data["revenue"])}")
    companiesName = []
    for com in data["production_companies"]:
        companiesName.append(com["name"])
    companies = ", ".join(companiesName)
    print(f"Production Companies ---- {companies}")
    print(f"Vote Average ---- {data["vote_average"]:.2f}")
    print(f"Vote Count ---- {data["vote_count"]}")
    print(f"IMDB Url ---- https://www.imdb.com/title/{data["imdb_id"]}")

def tvCard(data):
    print(f"Id ---- {data["id"]}")
    if len(data["created_by"]) == 0:
        pass
    else:
        for x in data["created_by"]:
            print(f"Name of Creator ---- {x["name"]}")

    if len(data["episode_run_time"]) == 0:
        pass
    else:
        print(f"Episode Run Time ---- {data["episode_run_time"]}")
    print(f"First Air Date ---- {data["first_air_date"]}")
    genreList=[]
    for x in data["genres"]:
        genreList.append(x["name"])
    print(f"Genres ---- {genreList}")
    print(f"Last Air Date ---- {data["last_air_date"]}")
    print(f"Name ---- {data["name"]}")
    networksList = []
    for x in data["networks"]:
        networksList.append(x["name"])
    print(f"Networks ---- {networksList}")
    productionCompanies = []
    for x in data["production_companies"]:
        productionCompanies.append(x["name"])
    print(f"Production Companies ---- {productionCompanies}")

def seasonInfo(data):
    nameList = []
    for x in data["episodes"]:
        nameList.append(x["name"])
    print(nameList)


def episodeInfo(data):
    nameList = []
    for x in data["crew"]:
        nameList.append(x["name"])
    print(nameList)
