import datetime
import os


def runtimeConvert(runtime: int):
    if runtime <= 60:
        print(f"Runtime ---- {runtime} minutes")
    else:
        print(f"Runtime ---- {runtime//60} hours {runtime%60} minutes")


def dateConvert(date: str):
    formattedDate = datetime.datetime.strptime(date, "%Y-%m-%d")
    day = formattedDate.strftime("%d").lstrip("0")
    month = formattedDate.strftime("%m").lstrip("0")
    year = formattedDate.strftime("%y")
    print(f"Release Date ---- {day}-{month}-{year}")


def currencyConvert(budget: int):
    if budget >= 1000000000:
        return f"{budget/1000000000:.1f} Billion Dollars"
    elif budget >= 1000000:
        return f"{budget/1000000:.1f} Million Dollars"
    elif budget >= 1000:
        return f"{budget/1000:.1f} Thousand Dollars"
    else:
        return f"{budget} Dollars"


def saveToWatchList(id: int, type: str):
    with open("watchlist.txt", "at") as f:
        f.write(f"{id},{type}\n")


def readWatchList():
    with open("watchlist.txt", "r") as f:
        data = f.readlines()
        wt = []
        for item in data:
            item = item.strip()
            item = tuple(item.split(","))
            wt.append(item)
        return wt


def clearWatchList():
    os.remove("watchlist.txt")


def saveToFavourites(id: int, type: str):
    with open("favourites.txt", "at") as f:
        f.write(f"{id},{type}\n")


def readFavourites():
    with open("favourites.txt", "r") as f:
        data = f.readlines()
        ft = []
        for item in data:
            item = item.strip()
            item = tuple(item.split(","))
            ft.append(item)
        return ft


def clearFavourites(id: str, type: str):
    ft = readFavourites()
    for x, item in enumerate(ft):
        if item[0] == id:
            if item[1] == type:
                ft.pop[x]
                break
    os.remove("favourites.txt")
    with open("favourites.txt", "w") as f:
        for item in ft:
            f.write(f"{item[0]},{item[1]}\n")


def saveRatings(id: int, type: str, rating: int):
    with open("ratings.txt", "at") as f:
        f.write(f"{id},{type},{rating}\n")


def readRatings():
    with open("ratings.txt", "r") as f:
        data = f.readlines()
        rt = []
        for item in data:
            item = item.strip()
            item = tuple(item.split(","))
            rt.append(item)
        return rt


def editRatings(id: str, type: str, rating: str):
    ft = []
    with open("ratings.txt", "r+") as f:
        data = f.readlines()
        for item in data:
            item = item.strip()
            item = tuple(item.split(","))
            ft.append(item)

        for x, item in enumerate(ft):
            if item[0] == id:
                if item[1] == type:
                    ft.pop(x)
                    ft.insert(x, (id, type, rating))
                    break
    os.remove("ratings.txt")
    with open("ratings.txt", "w") as f:
        for item in ft:
            f.write(f"{item[0]},{item[1]},{item[2]}\n")
