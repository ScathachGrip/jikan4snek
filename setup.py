import re
from setuptools import setup

version = ""
with open("jikan4snek/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)


requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()


if not version:
    raise RuntimeError("version is not set")

readme = ""
with open("README.md", encoding="utf8") as f:
    readme = f.read()

setup(
    name="jikan4snek",
    author="sinkaroid",
    author_email="anakmancasan@gmail.com",
    version=version,
    long_description=readme,
    long_description_content_type = "text/markdown",
    url="https://github.com/ScathachGrip/jikan4snek",
    project_urls={
        "CI": "https://github.com/ScathachGrip/jikan4snek/actions",
        "Funding": "https://github.com/sponsors/sinkaroid",
        "Issue tracker": "https://github.com/ScathachGrip/jikan4snek/issues/new/choose",
        "Documentation": "https://ScathachGrip.github.io/jikan4snek",
    },
    packages=["jikan4snek", "jikan4snek.client", "jikan4snek.base"],
    license="MIT",
    classifiers=[
        "Framework :: AsyncIO",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Games/Entertainment",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries"
    ],
    description="Python client for Jikan.moe, MyAnimeList's unofficial API",
    include_package_data=True,
    keywords=[
        "jikan",
        "myanimelist",
        "mal"
    ],
    install_requires=requirements,
)