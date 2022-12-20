import time
import logging
import asyncio
from aiohttp_client_cache import CachedSession, SQLiteBackend
from typing import Union
from .constant import Api, rm_slash, fetch_hit

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

    # if someid has "?q=" then it's a search
    if "?q=" in str(path):
        endpoint = f"{path}"

    else:
        endpoint = f"{path}/{someid}/{entry}/{eps}"

    start_fetch = time.time()
    async with CachedSession(cache=sequel_cfg) as session:
        async with session.get(f"{api}/{rm_slash(endpoint)}", headers=ua) as resp:
            time_took = time.time() - start_fetch
            time_took = round(time_took, 3)
            if resp.from_cache:
                if debug:
                    logging.info(f"Not hitting API, cache is available")
                    logging.info(
                        f"is_cache:{resp.from_cache} | status_code:{resp.status} | url:{resp.url} | took:{time_took} seconds")

                return await resp.json()

            else:
                if len(api_hit) == 0:
                    api_hit.append(1)
                    if debug:
                        logging.info(
                            f"First conditions of request, API hit {len(api_hit)}")
                        logging.info(
                            f"is_cache:{resp.from_cache} | status_code:{resp.status} | url:{resp.url} | took:{time_took} seconds")

                    return await resp.json()

                elif len(api_hit) <= 1:
                    api_hit.append(1)
                    if debug:
                        logging.info(
                            f"Second conditions of request, API hit {len(api_hit)}")

                    api = await fetch_hit(
                        cache=sequel_cfg,
                        endpoint=f"{api}/{rm_slash(endpoint)}",
                        headers=ua,
                    )

                    if debug:
                        logging.info(
                            f"is_cache:{api['cache']} | status_code:{api['status']} | url:{api['url']} | took:{api['took']} seconds")
                    return api["reparse"]

                else:
                    api_hit.clear()
                    if debug:
                        logging.info(
                            f"Third conditions of request, apply sleep for {Jikan.constant_hit} seconds..")
                    await asyncio.sleep(Jikan.constant_hit)
                    api_hit.append(1)
                    if debug:
                        logging.info(
                            f"Third should back to first condtions, API hit {len(api_hit)}")

                    api = await fetch_hit(
                        cache=sequel_cfg,
                        endpoint=f"{api}/{rm_slash(endpoint)}",
                        headers=ua,
                    )
                    if debug:
                        logging.info(
                            f"is_cache:{api['cache']} | status_code:{api['status']} | url:{api['url']} | took:{api['took']} seconds")

                    return api["reparse"]
