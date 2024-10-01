from utils import readFavourites, readRatings
from request import request


def recommend():
    fav = readFavourites()
    rat = readRatings()
    sim_weights = {}
    common_rating = {}

    for r in rat:
        if (r[0], r[1]) in fav:
            common_rating[(r[0], r[1])] = int(r[2])

    for f in fav:
        res = request(typeof="get", params=f"{f[1]}/{f[0]}/similar", queryparams="")
        similar = res["results"]
        name = ""
        if f[1] == "tv":
            name = "name"
        elif f[1] == "movie":
            name = "title"

        if similar:
            for s in similar:
                key = (str(f[0]), f[1])
                if key in sim_weights:
                    sim_weights[(s[name], s["id"], f[1])] += 1
                else:
                    if key in list(common_rating.keys()):
                        sim_weights[(s[name], s["id"], f[1])] = common_rating[key]
                    else:
                        sim_weights[(s[name], s["id"], f[1])] = 0
    recs = [
        (content_name, item_id, category, weight)
        for (content_name, item_id, category), weight in sim_weights.items()
    ]
    recs.sort(key=lambda r: r[2], reverse=True)
    return recs
