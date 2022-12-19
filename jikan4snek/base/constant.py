import json
import re
from jikan4snek import __version__
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(funcName)s:%(module)s | %(message)s')


class Api:
    def __init__(
        self,
        BASE_API="https://api.jikan.moe/v4",
        BASE_STRICT_DELAY=False,
        BASE_DEBUG=False,
        BASE_CONSTANT_HIT=2,
        BASE_SIMULATE_HIT=1.3,
        BASE_EXPIRE_CACHE=60,
        BASE_SQLITE_BACKEND="jikan4snek_cache/jikan4snek",
        BASE_headers: dict = {
            "User-Agent": f"jikan4snek/v{__version__} (https://pypi.org/project/jikan4snek);",
            "From": "hey@scathach.id",
        },
        BASE_anime_valid_entries: tuple = (
            "full",
            "characters",
            "staff",
            "episodes",
            "news",
            "forum",
            "videos",
            "videos_episodes",
            "pictures",
            "statistics",
            "moreinfo",
            "recommendations",
            "userupdates",
            "reviews",
            "relations",
            "themes",
            "external",
            "streaming",
        ),
        BASE_manga_valid_entries: tuple = (
            "full",
            "characters",
            "news",
            "forum",
            "pictures",
            "statistics",
            "moreinfo",
            "recommendations",
            "userupdates",
            "reviews",
            "relations",
            "external",
        ),
        BASE_character_valid_entries: tuple = (
            "full",
            "anime",
            "manga",
            "voices",
            "pictures",
        ),
        BASE_club_valid_entries: tuple = ("members", "staff", "relations"),
        BASE_people_valid_entries: tuple = (
            "full",
            "anime",
            "voices",
            "manga",
            "pictures",
        ),
        BASE_producer_valid_entries: tuple = ("full", "external"),
        BASE_random_valid_entries: tuple = (
            "anime",
            "manga",
            "characters",
            "people",
            "users",
        ),
        BASE_user_valid_entries: tuple = (
            "full",
            "statistics",
            "favorites",
            "userupdates",
            "about",
            "history",
            "friends",
            "reviews",
            "recommendations",
            "clubs",
            "external",
        ),
    ):
        self.api = BASE_API
        self.strict_delay = BASE_STRICT_DELAY
        self.debug = BASE_DEBUG
        self.constant_hit = BASE_CONSTANT_HIT
        self.simulate_hit = BASE_SIMULATE_HIT
        self.expire_cache = BASE_EXPIRE_CACHE
        self.sqlite_backend = BASE_SQLITE_BACKEND
        self.headers = BASE_headers
        self.anime_valid_entries = BASE_anime_valid_entries
        self.manga_valid_entries = BASE_manga_valid_entries
        self.character_valid_entries = BASE_character_valid_entries
        self.club_valid_entries = BASE_club_valid_entries
        self.people_valid_entries = BASE_people_valid_entries
        self.producer_valid_entries = BASE_producer_valid_entries
        self.random_valid_entries = BASE_random_valid_entries
        self.user_valid_entries = BASE_user_valid_entries


BASE_URL = Api()


def dump(parser: dict):
    """Converts the json object to a more readable object.

    Parameters
    ----------
    parser : dict

    Returns
    -------
    str
        The new dictionaries with neat keys.
    """
    return json.dumps(parser, sort_keys=True, indent=4, ensure_ascii=False)


def resolve(b_object: dict) -> dict:
    """Resolves the json object.

    Parameters
    ----------
    b_object : dict

    Returns
    -------
    dict
        raw json object
    """
    return json.loads(b_object)

def rm_slash(url: str) -> str:
    return re.sub(r"(?<!:)/{2,}", "/", url)

def logs(info: str) -> None:
    return logging.info(info)

