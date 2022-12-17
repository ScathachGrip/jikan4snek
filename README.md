<div align="center">
<a href="https://scathachgrip.github.io/jikan4snek4snek"><img width="600" src="https://cdn.discordapp.com/attachments/1046495201176334467/1053659151869415444/jikan4snek.png" alt="jikan4snek"></a>

<h4 align="center">Python client for Jikan.moe, simplified with amplified in mind.</h4>
<p align="center">
	<a href="https://github.com/ScathachGrip/jikan4snek/actions/workflows/request_sequentially.yml"><img src="https://github.com/ScathachGrip/jikan4snek/workflows/Request%20Sequentially/badge.svg"></a>
	<a href="https://codeclimate.com/github/ScathachGrip/jikan4snek/maintainability"><img src="https://api.codeclimate.com/v1/badges/1318c78a4b9911edf844/maintainability" /></a>
</p>

 
The motivation is simplified the api call, customizable behaviour, and user should have no worries with ratelimit.  
Jikan4snek simulating the requests with saved cache and apply coroutine delay if cache was expired.

<a href="https://github.com/ScathachGrip/jikan4snek/blob/master/CONTRIBUTING.md">Contributing</a> •
<a href="https://github.com/ScathachGrip/jikan4snek/wiki/Routing">Documentation</a> •
<a href="https://github.com/ScathachGrip/jikan4snek/issues/new/choose">Report Issues</a>
</div>

---

<a href="https://scathachgrip.github.io/jikan4snek4snek"><img align="right" src="https://cdn.discordapp.com/attachments/1046495201176334467/1053659152360157264/snekwaifu.png" width="430"></a>

- [Jikan4snek](#features)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Usage](#usage)
      - [Get](#get)
      - [Search](#search)
    - [Constructors](#constructors)
    - [Running tests](#running-tests)
    - [Jikan4snek.dump](#jikan4snekdump)
  - [Documentation](#documentation)
    - [Jikan4snek](https://scathachgrip.github.io/jikan4snek4snek)
    - [Jikan.moe documentation](https://docs.api.jikan.moe/)
  - [Acknowledgments](#acknowledgments)
  - [Pronunciation](#Pronunciation)
  - [MyAnimeList TOS](https://myanimelist.net/membership/terms_of_use)
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
You can apply your own instance of [Jikan](https://github.com/jikan-me/jikan-rest), user-agent, sqlite backend, and cache expiration time on the constructor.

The default:
```py
import asyncio
from jikan4snek import Jikan4SNEK

async def main():
    jikan = Jikan4SNEK(
        api="https://api.jikan.moe/v4",
        ua={
            "User-Agent": f"jikan4snek/{__version__}",
            "From": "hey@scathach.id",
        },
        sqlite_backend="jikan4snek_cache/jikan4snek",
        expire_cache=60, ## 1 hour
    )
    anime = await jikan.search("naruto").anime()
    print(anime)

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

### Running tests
Check workflows and the whole `/test` folder.

### Jikan4snek.dump
Short hand of [json.dump()](https://docs.python.org/3/library/json.html#json.dumps) If you are phobia with arbitrary bad indentation of json, use `Jikan4snek.dump()` to dump them, It's definitely str, not dictionaries, just in case for reading object to save your time.

## Documentation
https://scathachgrip.github.io/jikan4snek4snek

## Acknowledgements
I hope you have found this project useful. All the major credit really goes to the [Jikan](https://jikan.moe) and [MyAnimeList](https://myanimelist.net) itself.

## Pronunciation
Jikan is jikan.moe. then Snek is snek you know exactly what it's mean.

## Legal
This tool can be freely copied, modified, altered, distributed without any attribution whatsoever. However, if you feel like this tool deserves an attribution, mention it. It won't hurt anybody.
> Licence: WTF.