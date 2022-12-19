from typing import Union
from ..base.fetch import request
from ..base.constant import Api

Jikan = Api()


class Jikan4SNEK(object):
    """Jikan4SNEK Constructor

    You may want to running your own instance [jikan-me/jikan](https://github.com/jikan-me/jikan) or [jikan-me/jikan-rest](https://github.com/jikan-me/jikan-rest)
    Jikan4SNEK apply customizable: `api_url`, `user-agent`, and `base expiration cache`.

    Parameters
    ----------
    ua : dict
        Your custom user agent. Default is `jikan4snek/v{__version__}`
    api : str
        Custom jikan api url. Default is https://api.jikan.moe/v4
    sqlite_backend : str
        SQLite cache name. Default is `jikan4snek_cache/jikan4snek.sqlite`
    expire_cache : int
        Purge the whole cache after x minutes. Default is 60 minutes.
        PS: Your cache will never purged if you dont have any process running.
    debug : bool
        Enable to debug ratelimit hit. Default is False.
    """

    def __init__(
        self,
        ua: dict = Jikan.headers,
        api: str = Jikan.api,
        sqlite_backend: str = Jikan.sqlite_backend,
        expire_cache: int = Jikan.expire_cache,
        debug: bool = False,
    ):

        self.ua = ua
        self.api = api
        self.sqlite_backend = sqlite_backend
        self.expire_cache = expire_cache
        self.debug = debug

    @staticmethod
    async def fetch_aiosequel(
        self, path: str, entry: str = "", eps: str = ""
    ) -> Union[dict, None]:
        """Check table if the data is cached, if not, fetch the data from the API.

        Parameters
        ----------
        path : str
            The path to the API.
        entry : str
            The entry path after "/".
        eps : str
            The episode number (if the entry is "episodes")

        Returns
        -------
        Union[dict, None]
            The response cache or api
        """
        raw_data = await request(
            api=self.api,
            sqlite_backend=self.sqlite_backend,
            expire_cache=self.expire_cache,
            debug=self.debug,
            ua=self.user_agent,
            someid=self.id,
            path=path,
            entry=entry,
            eps=eps,
        )
        return raw_data

    def get(
        self, some_id: int, entry: str = "", eps: str = ""
    ) -> "JikanResponseFromId":
        ##print(some_id, entry, eps)
        ##print(self.ua)
        """
        Returns the JikanResponseFromId object.

        Parameters
        ----------
        some_id : int
            The id what you want to get.

        entry : str
            The entry path, default is empty which means "/".

        eps : str
            The episode number (only consume if the entry is "episodes").

        """
        return JikanResponseFromId(self, some_id, entry, eps)

    def search(
        self, query: str, limit: int = 25, page: int = 1
    ) -> "JikanResponseFromSearch":
        """Returns the JikanResponseFromSearch object.

        Parameters
        ----------
        query : str
            The query what you want to search.

        limit : int
            The limit of the search result. Default is 25.

        page : int
            The page of the search result. Default is 1.
        """
        return JikanResponseFromSearch(self, query, limit, page)


class JikanResponseFromId:
    ## object utama
    def __init__(self, raw_, id_, entry_: str = "", eps_: str = ""):
        self.id = id_
        self.entry = entry_
        self.eps = eps_
        self.raw = raw_
        self.api = raw_.api
        self.user_agent = raw_.ua
        self.sqlite_backend = raw_.sqlite_backend
        self.expire_cache = raw_.expire_cache
        self.debug = raw_.debug
        ##print(self.id, self.raw)

    async def anime(self):
        """Returns the anime data. https://docs.api.jikan.moe/#tag/anime

        get entries:
        ["full", "characters", "staff", "episodes", "news", "forum", "videos", "videos_episodes",
        "pictures", "statistics", "moreinfo", "recommendations", "userupdates", "reviews", "relations",
        "themes", "external", "streaming"]

        Returns
        -------
        Union[dict, None]
            The response from the API.
        """
        ##return self
        ## 'entry': 'episodes'

        if self.entry and self.entry not in Jikan.anime_valid_entries:
            raise ValueError(f"Invalid entry {Jikan.anime_valid_entries}")
        elif self.entry == "episodes":
            return await Jikan4SNEK.fetch_aiosequel(self, "anime", self.entry, self.eps)
        elif self.entry == "videos_episodes":
            return await Jikan4SNEK.fetch_aiosequel(self, "anime", "videos", "episodes")

        return await Jikan4SNEK.fetch_aiosequel(self, "anime", self.entry)

    async def manga(self):
        """
        Returns the manga data. https://docs.api.jikan.moe/#tag/manga

        get entries: 
        ["full", "characters", "news", "forum", "pictures", "statistics", "moreinfo", 
        "recommendations", "userupdates", "reviews", "relations", "external"]

        Returns
        -------
        Union[dict, None]
            The response from the API.
        """
        if self.entry and self.entry not in Jikan.manga_valid_entries:
            raise ValueError(f"Invalid entry {Jikan.manga_valid_entries}")

        return await Jikan4SNEK.fetch_aiosequel(self, "manga", self.entry)

    async def characters(self):
        """
        Returns the character data. https://docs.api.jikan.moe/#tag/characters

        get entries:
        ["full", "anime", "manga", "voices", "pictures"]

        Returns
        -------
        Union[dict, None]
            The response from the API.
        """
        if self.entry and self.entry not in Jikan.character_valid_entries:
            raise ValueError(f"Invalid entry {Jikan.character_valid_entries}")

        return await Jikan4SNEK.fetch_aiosequel(self, "characters", self.entry)

    async def clubs(self):
        """
        Returns the club data. https://docs.api.jikan.moe/#tag/clubs

        get entries:
        ["members", "staff", "relations"]

        Returns
        -------
        Union[dict, None]
            The response from the API.
        """
        if self.entry and self.entry not in Jikan.club_valid_entries:
            raise ValueError(f"Invalid entry {Jikan.club_valid_entries}")

        return await Jikan4SNEK.fetch_aiosequel(self, "clubs", self.entry)

    async def people(self):
        """
        Returns the people data. https://docs.api.jikan.moe/#tag/people

        get entries:
        ["full", "anime", "voices", "manga", "pictures"]

        Returns
        -------
        Union[dict, None]
            The response from the API.
        """
        if self.entry and self.entry not in Jikan.people_valid_entries:
            raise ValueError(f"Invalid entry {Jikan.people_valid_entries}")

        return await Jikan4SNEK.fetch_aiosequel(self, "people", self.entry)

    async def producers(self):
        """
        Returns the producer data. https://docs.api.jikan.moe/#tag/producers

        get entries:
        ["full", "external"]

        Returns
        -------
        Union[dict, None]
            The response from the API.
        """
        if self.entry and self.entry not in Jikan.producer_valid_entries:
            raise ValueError(f"Invalid entry {Jikan.producer_valid_entries}")

        return await Jikan4SNEK.fetch_aiosequel(self, "producers", self.entry)

    async def random(self):
        """
        Returns the random data. https://docs.api.jikan.moe/#tag/random

        get entries:
        ["anime", "manga", "characters", "people", "users"]

        Returns
        -------
        Union[dict, None]
            The response from the API.
        """
        if self.entry not in Jikan.random_valid_entries:
            raise ValueError(f"Invalid entry {Jikan.random_valid_entries}")

        self.id = ""
        return await Jikan4SNEK.fetch_aiosequel(self, "random", self.entry)

    async def users(self):
        """
        Returns the user data. https://docs.api.jikan.moe/#tag/users

        get entries:
        ["full", "statistics", "favorites", "userupdates", "about", "history", 
        "friends", "reviews", "recommendations", "clubs", "external"]

        Returns
        -------
        Union[dict, None]
            The response from the API.
        """
        if self.entry and self.entry not in Jikan.user_valid_entries:
            raise ValueError(f"Invalid entry {Jikan.user_valid_entries}")

        return await Jikan4SNEK.fetch_aiosequel(self, "users", self.entry)


class JikanResponseFromSearch:
    def __init__(self, raw_, query, limit_, page_):
        self.id = query
        self.limit = limit_
        self.page = page_
        self.raw = raw_
        self.api = raw_.api
        self.user_agent = raw_.ua
        self.sqlite_backend = raw_.sqlite_backend
        self.expire_cache = raw_.expire_cache
        self.debug = raw_.debug

        ##print(self.__dict__)

    async def anime(self):
        """Search the anime data. https://docs.api.jikan.moe/#tag/anime/operation/getAnimeSearch

        Returns
        -------
        Union[dict, None]
            The response search from the API.
        """
        return await Jikan4SNEK.fetch_aiosequel(
            self, f"anime?q={self.id}&limit={self.limit}&page={self.page}"
        )

    async def manga(self):
        """Search the manga data. https://docs.api.jikan.moe/#tag/manga/operation/getMangaSearch

        Returns
        -------
        Union[dict, None]
            The response search from the API.
        """
        return await Jikan4SNEK.fetch_aiosequel(
            self, f"manga?q={self.id}&limit={self.limit}&page={self.page}"
        )

    async def characters(self):
        """Search the characters data. https://docs.api.jikan.moe/#tag/characters/operation/getCharactersSearch

        Returns
        -------
        Union[dict, None]
            The response search from the API.
        """
        return await Jikan4SNEK.fetch_aiosequel(
            self, f"characters?q={self.id}&limit={self.limit}&page={self.page}"
        )

    async def clubs(self):
        """Search the clubs data. https://docs.api.jikan.moe/#tag/clubs/operation/getClubsSearch

        Returns
        -------
        Union[dict, None]
            The response search from the API.
        """
        return await Jikan4SNEK.fetch_aiosequel(
            self, f"clubs?q={self.id}&limit={self.limit}&page={self.page}"
        )

    async def people(self):
        """Search the people data. https://docs.api.jikan.moe/#tag/people/operation/getPeopleSearch

        Returns
        -------
        Union[dict, None]
            The response search from the API.
        """
        return await Jikan4SNEK.fetch_aiosequel(
            self, f"people?q={self.id}&limit={self.limit}&page={self.page}"
        )

    async def producers(self):
        """Search the producers data. https://docs.api.jikan.moe/#tag/producers/operation/getProducers

        Returns
        -------
        Union[dict, None]
            The response search from the API.
        """
        return await Jikan4SNEK.fetch_aiosequel(
            self, f"producers?q={self.id}&limit={self.limit}&page={self.page}"
        )

    async def magazines(self):
        """Search the magazines data. https://docs.api.jikan.moe/#tag/magazines/operation/getMagazines

        Returns
        -------
        Union[dict, None]
            The response search from the API.
        """
        return await Jikan4SNEK.fetch_aiosequel(
            self, f"magazines?q={self.id}&limit={self.limit}&page={self.page}"
        )

    async def users(self):
        """Search the users data. https://docs.api.jikan.moe/#tag/users/operation/getUsersSearch

        Returns
        -------
        Union[dict, None]
            The response search from the API.
        """
        return await Jikan4SNEK.fetch_aiosequel(
            self, f"users?q={self.id}&limit={self.limit}&page={self.page}"
        )
