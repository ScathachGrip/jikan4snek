<div align="center">
<a href="https://scathachgrip.github.io/jikan4snek"><img width="600" src="https://cdn.discordapp.com/attachments/1046495201176334467/1053659151869415444/jikan4snek.png" alt="jikan4snek"></a>

<h4 align="center">Python client for Jikan.moe, simplified with amplified in mind.</h4>
<p align="center">
	<a href="https://github.com/ScathachGrip/jikan4snek/actions/workflows/get_test.yml"><img src="https://github.com/ScathachGrip/jikan4snek/workflows/Test%20get/badge.svg"></a>
  	<a href="https://github.com/ScathachGrip/jikan4snek/actions/workflows/search_test.yml"><img src="https://github.com/ScathachGrip/jikan4snek/workflows/Test%20search/badge.svg"></a>
	<a href="https://codeclimate.com/github/ScathachGrip/jikan4snek/maintainability"><img src="https://api.codeclimate.com/v1/badges/1318c78a4b9911edf844/maintainability" /></a>
</p>

 
The motivation is simplified the api call, customizable behaviour, and user should have no worries with ratelimit.  
Jikan4snek simulating requests with cache and apply coroutine delay if ratelimit was hit or it's expired.

<a href="https://github.com/ScathachGrip/jikan4snek/blob/master/CONTRIBUTING.md">Contributing</a> •
<a href="https://scathachgrip.github.io/jikan4snek">Documentation</a> •
<a href="https://github.com/ScathachGrip/jikan4snek/issues/new/choose">Report Issues</a>
</div>

---

<a href="https://scathachgrip.github.io/jikan4snek"><img align="right" src="https://cdn.discordapp.com/attachments/1046495201176334467/1053659152360157264/snekwaifu.png" width="430"></a>

- [Jikan4snek](#features)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Usage](#usage)
      - [Get](#get)
      - [Search](#search)
      - [Bulk-request](#bulk-request)
    - [Constructors](#constructors)
    - [Running tests](#running-tests)
  - [Debug](#debug)
    - [Jikan4snek.dump](#jikan4snekdump)
  - [Documentation](#documentation)
    - [Jikan4snek](https://scathachgrip.github.io/jikan4snek)
    - [Jikan.moe documentation](https://docs.api.jikan.moe/)
  - [Acknowledgments](#acknowledgments)
  - [Pronunciation](#Pronunciation)
  - [Legal](#legal)


## Features
Jikan4snek combines in-disk cache and ratelimit hit to simulate the requests.

- Has own ratelimit flow
- Customizable behaviour
- Simplified, nested method call
- Covers 80% of the v4 Jikan endpoints
- Easy to use, check your intelisense

## Installation
`pip install jikan4snek` 

Or build from source:
> clone this repo and run `python setup.py install`

### Prerequisites
<table>
	<td><b>NOTE:</b> Python 3.7 or above</td>
</table>

### Usage
Should be run in async context, also follow the nested call after **get** or **search** method.

```py
import asyncio
from jikan4snek import Jikan4SNEK, dump

async def main():
    jikan = Jikan4SNEK()
    anime = await jikan.get(18679).anime()
    print(anime) ## this is <class 'dict'>
    print(dump(anime)) ## this is <class 'str'>

asyncio.run(main())
```

### Constructors
You can apply your own instance of [Jikan](https://github.com/jikan-me/jikan-rest), user-agent, sqlite backend, cache expiration, and debug.

The default:
```py
import asyncio
from jikan4snek import Jikan4SNEK

async def main():
    jikan = Jikan4SNEK(
        api="https://api.jikan.moe/v4",
        ua={
            "User-Agent": "jikan4snek/current_version",
            "From": "hey@scathach.id",
        },
        sqlite_backend="jikan4snek_cache/jikan4snek",
        expire_cache=60, ## 1 hour
        debug=False ## debug mode, default is False
    )
    some_anime = await jikan.search("naruto").anime()
    ## do with some_anime

asyncio.run(main())
```

### Get
[`jikan.get()`](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.Jikan4SNEK.get) used from based on id.

```py
await jikan.get(18679, entry="characters").anime()
await jikan.get(18679, entry="pictures").anime()
```

<details> 
<summary>See more</summary>

#### Anime
> [jikan4snek.client.jikan.JikanResponseFromId.anime](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromId.anime)

```py
await jikan.get(18679, entry="characters").anime()
await jikan.get(18679, entry="pictures").anime()
```

#### Manga
> [jikan4snek.client.jikan.JikanResponseFromId.manga](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromId.manga)

```py
await jikan.get(58391).manga()
await jikan.get(58391, entry="characters").manga()
```

#### Characters
> [jikan4snek.client.jikan.JikanResponseFromId.characters](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromId.characters)

```py 
await jikan.get(83799).characters()
await jikan.get(83799, entry="voices").characters()
```

#### Clubs
> [jikan4snek.client.jikan.JikanResponseFromId.clubs](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromId.clubs)

```py
await jikan.get(1).clubs()
await jikan.get(1, entry="members").clubs()
```

#### People
> [jikan4snek.client.jikan.JikanResponseFromId.people](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromId.people)

```py
await jikan.get(1).people()
await jikan.get(1, entry="pictures").people()
```

#### Producers
> [jikan4snek.client.jikan.JikanResponseFromId.producers](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromId.producers)

```py
await jikan.get(1).producers()
await jikan.get(1, entry="external").producers()
```

#### Random
> [jikan4snek.client.jikan.JikanResponseFromId.random](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromId.random)

```py
await jikan.get(False, entry="anime").random()
await jikan.get(False, entry="manga").random()
```
#### Users
> [jikan4snek.client.jikan.JikanResponseFromId.users](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromId.users)

```py
await jikan.get("sinkaroid").users()
await jikan.get("sinkaroid", entry="history").users()
```
</details>

### Search
[`jikan.search()`](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.Jikan4SNEK.search) used from based on query search.

```py
await jikan.search("naruto").anime()
await jikan.search("naruto", limit=10, page=2).anime()
```

<details>
<summary>See more</summary>

#### Anime
> [jikan4snek.client.jikan.JikanResponseFromSearch.anime](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromSearch.anime)

```py
await jikan.search("naruto").anime()
await jikan.search("naruto", limit=10, page=2).anime()
```

#### Manga
> [jikan4snek.client.jikan.JikanResponseFromSearch.manga](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromSearch.manga)

```py
await jikan.search("naruto").manga()
await jikan.search("naruto", limit=10, page=2).manga()
```

#### Characters
> [jikan4snek.client.jikan.JikanResponseFromSearch.characters](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromSearch.characters)

```py
await jikan.search("uchiha").characters()
await jikan.search("uchiha", limit=10, page=1).characters()
```

#### Clubs
> [jikan4snek.client.jikan.JikanResponseFromSearch.clubs](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromSearch.clubs)

```py
await jikan.search("naruto").clubs()
await jikan.search("naruto", limit=10, page=1).clubs()
```

#### People
> [jikan4snek.client.jikan.JikanResponseFromSearch.people](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromSearch.people)

```py
await jikan.search("tanaka rie").people()
await jikan.search("tanaka", limit=10, page=1).people()
```

#### Producers
> [jikan4snek.client.jikan.JikanResponseFromSearch.producers](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromSearch.producers)

```py
await jikan.search("madhouse").producers()
await jikan.search("japan", limit=10, page=1).producers()
```

#### Magazines
> [jikan4snek.client.jikan.JikanResponseFromSearch.magazines](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromSearch.magazines)

```py
await jikan.search("jump").magazines()
await jikan.search("jump", limit=10, page=1).magazines()
```

#### Users
> [jikan4snek.client.jikan.JikanResponseFromSearch.users](https://scathachgrip.github.io/jikan4snek/client/jikan.html#jikan4snek.client.jikan.JikanResponseFromSearch.users)

```py
await jikan.search("sinkaroid").users()
await jikan.search("sin", limit=10, page=1).users()
```
</details>

### Bulk request
If you using `asyncio.gather(*[jikan.get("..").anime()])` sadly, It will broke the base api hit, Just do it like usual, enable debug, and snek will handle the ratelimit for you. For example:

```py
import asyncio
import jikan4snek

some_bunch_of_anime = [
    44511, 50602, 50172, 49918, 49596, 41467, 
    48316, 49709, 42962, 47917, 49891, 50425, 
    50710, 49784, 51098, 49979, 52046, 52193, 
    51128, 48542, 49828, 51403, 50205, 50528, 
    50590, 51212, 30455, 50923, 50348, 51680]

async def main():
    Jikan = jikan4snek.Jikan4SNEK(debug=True)
    for i in some_bunch_of_anime:
        res = await Jikan.get(i).anime()
        print("Anime:", res['data']['title'])

asyncio.run(main())
```

### Running tests
Check workflows and the whole `/test` folder.

## Debug
Enable debug. Default is False. Use this if jikan4snek request is not working as expected.  
```py
jikan = Jikan4SNEK(debug=True)
```

```
2022-12-20 21:02:06,435 | INFO | request:fetch | Not hitting API, cache is available
2022-12-20 21:02:06,435 | INFO | request:fetch | is_cache:True | status_code:200 | url:https://api.jikan.moe/v4/anime/44511 | took:0.02 seconds
2022-12-20 21:02:06,435 | INFO | main:memek | Anime: Chainsaw Man
2022-12-20 21:02:06,435 | INFO | request:fetch | Not hitting API, cache is available
2022-12-20 21:02:06,435 | INFO | request:fetch | is_cache:True | status_code:200 | url:https://api.jikan.moe/v4/anime/50602 | took:0.0 seconds
2022-12-20 21:02:06,435 | INFO | main:memek | Anime: Spy x Family Part 2
2022-12-20 21:02:06,435 | INFO | request:fetch | Not hitting API, cache is available
2022-12-20 21:02:06,435 | INFO | request:fetch | is_cache:True | status_code:200 | url:https://api.jikan.moe/v4/anime/50172 | took:0.0 seconds
2022-12-20 21:02:06,435 | INFO | main:memek | Anime: Mob Psycho 100 III
2022-12-20 21:02:07,997 | INFO | request:fetch | First conditions of request, API hit 1
2022-12-20 21:02:07,997 | INFO | request:fetch | is_cache:False | status_code:200 | url:https://api.jikan.moe/v4/anime/49918 | took:1.56 seconds
2022-12-20 21:02:07,997 | INFO | main:memek | Anime: Boku no Hero Academia 6th Season
2022-12-20 21:02:09,560 | INFO | request:fetch | Second conditions of request, API hit 2
2022-12-20 21:02:09,576 | INFO | request:fetch | is_cache:False | status_code:200 | url:https://api.jikan.moe/v4/anime/49596 | took:0.016 seconds
2022-12-20 21:02:09,576 | INFO | main:memek | Anime: Blue Lock
2022-12-20 21:02:11,122 | INFO | request:fetch | Third conditions of request, apply sleep for 1 seconds..
2022-12-20 21:02:12,123 | INFO | request:fetch | Third should back to first condtions, API hit 1
2022-12-20 21:02:12,154 | INFO | request:fetch | is_cache:False | status_code:200 | url:https://api.jikan.moe/v4/anime/41467 | took:0.031 seconds
2022-12-20 21:02:12,154 | INFO | main:memek | Anime: Bleach: Sennen Kessen-hen
2022-12-20 21:02:13,716 | INFO | request:fetch | Second conditions of request, API hit 2
2022-12-20 21:02:13,732 | INFO | request:fetch | is_cache:False | status_code:200 | url:https://api.jikan.moe/v4/anime/48316 | took:0.016 seconds
2022-12-20 21:02:13,732 | INFO | main:memek | Anime: Kage no Jitsuryokusha ni Naritakute!
2022-12-20 21:02:15,247 | INFO | request:fetch | Third conditions of request, apply sleep for 1 seconds..
2022-12-20 21:02:16,247 | INFO | request:fetch | Third should back to first condtions, API hit 1
```

### Jikan4snek.dump
Short hand of [json.dump()](https://docs.python.org/3/library/json.html#json.dumps) If you are phobia with arbitrary bad indentation of json. Use `Jikan4snek.dump()` to dump them, It's definitely str, not dictionaries, just in case for reading object to save your time.

## Documentation
https://scathachgrip.github.io/jikan4snek

## Acknowledgements
I hope you have found this project useful. All the major credit really goes to the [Jikan](https://jikan.moe) and [MyAnimeList](https://myanimelist.net) itself.

## Pronunciation
Jikan is jikan.moe. then Snek is snek you know exactly what it's mean.

## Legal
This tool can be freely copied, modified, altered, distributed without any attribution whatsoever. However, if you feel like this tool deserves an attribution, mention it. It won't hurt anybody.
> Licence: WTF.