import asyncio
import jikan4snek
import argparse
import time


class Client(object):
    def __init__(self):
        self.dump = jikan4snek.dump
        self.some_bunch_of_anime = [
            44511,
            50602,
            50172,
            49918,
            49596,
            41467,
            48316,
            49709,
            42962,
            47917,
            49891,
            50425,
            50710,
            49784,
            51098,
            49979,
            52046,
            52193,
            51128,
            48542,
            49828,
            51403,
            50205,
            50528,
            50590,
            51212,
            30455,
            50923,
            50348,
            51680,
        ]


Base = Client()
Jikan = jikan4snek.Jikan4SNEK(debug=True)

async def fetch():
    start = time.time()
    for i in Base.some_bunch_of_anime:
        res = await Jikan.get(i).anime()
        print(f"{res['data']['mal_id']}: {res['data']['title']}")

    print(
        f"GET {len(Base.some_bunch_of_anime)} request sequentially without cache, took: {(time.time() - start) / 60:.2f} minutes"
    )

async def anime():

    anime = await Jikan.get(18679).anime()
    print("anime", Base.dump(anime))

    anime_picture = await Jikan.get(18679, entry="characters").anime()
    print("anime_picture", Base.dump(anime_picture))

    anime_characters = await Jikan.get(18679, entry="characters").anime()
    print("anime_characters", Base.dump(anime_characters))

async def manga():
    
    manga = await Jikan.get(116778).manga()
    print("manga", Base.dump(manga))
    
    manga_characters = await Jikan.get(116778, entry="characters").manga()
    print("manga_characters", Base.dump(manga_characters))

async def characters():
        
    characters = await Jikan.get(170734).characters()
    print("characters", Base.dump(characters))

    characters_voice = await Jikan.get(170734, entry="voices").characters()
    print("characters_voice", Base.dump(characters_voice))

async def clubs():
        
    clubs = await Jikan.get(14230).clubs()
    print("clubs", Base.dump(clubs))

    clubs_members = await Jikan.get(14230, entry="members").clubs()
    print("clubs_members", Base.dump(clubs_members))

async def people():

    people = await Jikan.get(60).people()
    print("people", Base.dump(people))

    people_pictures = await Jikan.get(60, entry="pictures").people()
    print("people_pictures", Base.dump(people_pictures))

async def producers():

    producers = await Jikan.get(1).producers()
    print("producers", Base.dump(producers))

    producers_external = await Jikan.get(1, entry="external").producers()
    print("producers_external", Base.dump(producers_external))

async def random():

    anime = await Jikan.get(False, entry="anime").random()
    print("random_anime", Base.dump(anime))

    manga = await Jikan.get(False, entry="manga").random()
    print("random_manga", Base.dump(manga))

async def users():

    user = await Jikan.get("sinkaroid").users()
    print("user", Base.dump(user))

    user_history = await Jikan.get("sinkaroid", entry="history").users()
    print("user_history", Base.dump(user_history))


async def search_anime():
    search = await Jikan.search("naruto").anime()
    print("search_anime", Base.dump(search))

async def search_manga():
    search = await Jikan.search("black clover").manga()
    print("search_manga", Base.dump(search))

async def search_characters():
    search = await Jikan.search("uchiha").characters()
    print("search_characters", Base.dump(search))

async def search_clubs():
    search = await Jikan.search("naruto").clubs()
    print("search_club", Base.dump(search))

async def search_people():
    search = await Jikan.search("tanaka rie").people()
    print("search_people", Base.dump(search))

async def search_producers():
    search = await Jikan.search("madhouse").producers()
    print("search_producers", Base.dump(search))

async def search_magazines():
    search = await Jikan.search("shonen jump").magazines()
    print("search_magazines", Base.dump(search))

async def search_users():
    search = await Jikan.search("sin").users()
    print("search_users", Base.dump(search))


parse = argparse.ArgumentParser(description="J4snek")
parse.add_argument("-sequentially", action="store_true")
parse.add_argument("-get_anime", action="store_true")
parse.add_argument("-get_manga", action="store_true")
parse.add_argument("-get_clubs", action="store_true")
parse.add_argument("-get_characters", action="store_true")
parse.add_argument("-get_people", action="store_true")
parse.add_argument("-get_producers", action="store_true")
parse.add_argument("-get_random", action="store_true")
parse.add_argument("-get_users", action="store_true")

parse.add_argument("-search_anime", action="store_true")
parse.add_argument("-search_manga", action="store_true")
parse.add_argument("-search_characters", action="store_true")
parse.add_argument("-search_clubs", action="store_true")
parse.add_argument("-search_people", action="store_true")
parse.add_argument("-search_producers", action="store_true")
parse.add_argument("-search_magazines", action="store_true")
parse.add_argument("-search_users", action="store_true")

args = parse.parse_args()


async def main():
    if args.sequentially:
        return await fetch()

    elif args.get_anime:
        return await anime()

    elif args.get_manga:
        return await manga()

    elif args.get_clubs:
        return await clubs()

    elif args.get_characters:
        return await characters()

    elif args.get_people:
        return await people()

    elif args.get_producers:
        return await producers()

    elif args.get_random:
        return await random()

    elif args.get_users:
        return await users()

    elif args.search_anime:
        return await search_anime()

    elif args.search_manga:
        return await search_manga()

    elif args.search_characters:
        return await search_characters()

    elif args.search_clubs:
        return await search_clubs()

    elif args.search_people:
        return await search_people()

    elif args.search_producers:
        return await search_producers()

    elif args.search_magazines:
        return await search_magazines()

    elif args.search_users:
        return await search_users()

    else:
        print("No arguments given")


if __name__ == "__main__":
    asyncio.run(main())