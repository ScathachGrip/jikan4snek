import time
import logging
from asyncio import sleep
from aiohttp_client_cache import CachedSession, SQLiteBackend
from typing import Union
from .constant import Api, rm_slash

Jikan = Api()
api_hit = []


async def request(
    path: str,
    someid: int,
    entry: str,
    eps: str = "",
    api: str = Jikan.api,
    ua: dict = Jikan.headers,
    sqlite_backend: str = Jikan.sqlite_backend,
    expire_cache: int = Jikan.expire_cache,
    debug: bool = Jikan.debug,
) -> Union[dict, None]:
    """Request to the API or fetch from cache.

    Parameters
    ----------
    api : str
        The base url of the API.
    path : str
        The path to the API.
    someid : int
        The id of the anime or manga.
    entry : str
        The entry path after "/"
    ua : dict
        The user agent.
    sqlite_backend : str
        The sqlite backend.
    expire_cache : int
        Expire cache in minutes.

    Returns
    -------
    Union[dict, None]
        The response from the API.
    """

    sequel_cfg = SQLiteBackend(
        cache_name=sqlite_backend,
        expire_after=expire_cache * 60,
        allowed_codes=(200, 304),
        allowed_methods=["GET"],
        timeout=2.5,
        urls_expire_after={"*/random": 0},
    )

    ## if someid has "?q=" then it's a search
    if "?q=" in str(path):
        endpoint = f"{path}"

    else:
        endpoint = f"{path}/{someid}/{entry}/{eps}"

    start_fetch = time.time()
    async with CachedSession(cache=sequel_cfg) as session:
        async with session.get(f"{api}/{rm_slash(endpoint)}", headers=ua) as resp:
            simulate_time = time.time() - start_fetch
            simulate_time = round(simulate_time, 2)

            if debug:
                logging.info(
                    f"Cache:{resp.from_cache} | Status:{resp.status} | {resp.url}"
                )
                logging.info(
                    f"Add delay hit depends on your internet, took {simulate_time} sec."
                )

            try:
                if Jikan.strict_delay:
                    if resp.from_cache:
                        res = await resp.json()
                        return res
                    else:
                        res = await resp.json()
                        await sleep(Jikan.constant_hit)
                        return res

                else:
                    if resp.from_cache:
                        if debug:
                            logging.info(f"Not hitting the API, using cache")
                        res = await resp.json()
                        return res

                    elif resp.from_cache is False and len(api_hit) < 3:
                        if debug:
                            logging.info(f"API hit {len(api_hit) + 1}")
                        api_hit.append(1)
                        res = await resp.json()
                        await sleep(Jikan.simulate_hit)
                        ## print(f"ratelimit hit 1: {len(api_hit)}")
                        return res

                    else:
                        if debug:
                            logging.info(
                                f"API hit exceeded 3, Reseting hit to 1 and add delay"
                            )
                        api_hit.clear()
                        api_hit.append(1)
                        res = await resp.json()
                        await sleep(1)
                        ## print(f"ratelimit hit 2: {len(api_hit)}")
                        return res

            except Exception as e:
                raise Exception(
                    f"Failed to get data from: {path} with: {someid} due to: {e}"
                )
