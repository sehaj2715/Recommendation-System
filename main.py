from request import request
from card import trendingCard, movieCard, tvCard, seasonInfo, episodeInfo
from utils import (
    saveToWatchList,
    readWatchList,
    clearWatchList,
    saveToFavourites,
    clearFavourites,
    saveRatings,
    editRatings,
)
from algo import recommend
import os

while True:
    print(
        "\n------ Commands ------\ntr --- show trending\ndet --- show details\nser --- search content\nwat --- add to watchlist\ndelwl --- delete watchlist\nwl --- read watchlist\nfav --- add to favourites\ndelfav --- delete favourites\nrate --- rate movies\neditrate --- edit rating\nrec --- get recommendations"
    )
    cmd = input("Enter the command: ").lower()
    if cmd == "tr":
        contentType = input("movie, tv, all: ")
        duration = input("day, week: ")
        results = request(typeof="get", params=f"trending/{contentType}/{duration}")[
            "results"
        ]
        print("\n\n ------Results------\n")
        for result in results:
            trendingCard(result)
    elif cmd == "det":
        mediaType = input("tv, movie: ")
        mediaId = input("id: ")
        result = request(typeof="get", params=f"{mediaType}/{mediaId}")
        if mediaType == "movie":
            movieCard(result)
        elif mediaType == "tv":
            tvCard(result)

            requireSeasonInfo = input(
                "do you want to see description of episodes in a season?(Yes/No): "
            )
            if requireSeasonInfo.lower() == "yes":
                seasonNumber = str(input("Enter season number: "))
            else:
                pass
            seasonInfoResult = request(
                typeof="get", params=f"{mediaType}/{mediaId}/season/{seasonNumber}"
            )
            if requireSeasonInfo.lower() == "yes":
                seasonInfo(seasonInfoResult)

            requireEpisodeInfo = input(
                "do you want to see detailed discription of a particular episode in this season?(Yes/No)"
            )
            if requireEpisodeInfo.lower() == "yes":
                episodeNumber = str(input("Enter episode number: "))
            else:
                pass
            episodeInfoResult = request(
                typeof="get",
                params=f"{mediaType}/{mediaId}/season/{seasonNumber}/episode/{episodeNumber}",
            )
            episodeInfo(episodeInfoResult)
    elif cmd == "ser":
        term = input("What are you looking for: ")

        movieResult = request(
            typeof="get", params="search/movie", queryparams=f"&query={term}"
        )["results"]
        tvResult = request(
            typeof="get", params="search/tv", queryparams=f"&query={term}"
        )["results"]

        if len(movieResult) > 0:
            print("---- Movie Results ----")
            for movie in movieResult:
                trendingCard(movie)
        else:
            print("No movies found")

        if len(tvResult) > 0:
            print("---- Tv Results ----")
            for tv in tvResult:
                trendingCard(tv)
        else:
            print("No show found")
    elif cmd == "wat":
        id = int(input("Enter id: "))
        type = str(input("Enter type: "))
        saveToWatchList(id, type)

    elif cmd == "wl":
        print(readWatchList())

    elif cmd == "fav":
        id = int(input("Enter id: "))
        type = str(input("Enter type: "))
        saveToFavourites(id, type)

    elif cmd == "delfav":
        delete = input(f"do you want to delete all favourites?(Yes/No)")
        if delete.lower() == "yes":
            os.remove("favourites.txt")
        else:
            id = input(f"Enter the ID: ")
            type = input(f"Enter the type: ")
            clearFavourites(id=id, type=type)

    elif cmd == "rate":
        id = int(input("Enter id: "))
        type = str(input("Enter type: "))
        rating = int(input("Enter rating (0-5): "))
        if int(rating) <= 5:
            saveRatings(id, type, rating)
        else:
            print("Invalid rating")

    elif cmd == "editrate":
        search = input(f"which movie do you want to re-rate?")
        replace = input(f"what's the new rating you want to give?")
        editRatings(search=search, replace=replace)

    elif cmd == "rec":
        recs = recommend()
        print("Recommendations -- ")
        for x in recs:
            print(x[0])

    else:
        print("Invalid Command")
