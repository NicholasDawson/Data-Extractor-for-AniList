# Data Extractor for AniList
## Software Requirements:
- [Python 3](https://www.python.org/downloads/ "Python 3")
	 - **Needed Libraries:**
	- requests
	- bs4
	- selenium
- [geckodriver (Firefox Webdriver)](https://github.com/mozilla/geckodriver/releases "geckodriver")
	- Place geckodriver.exe into your Python parent folder (ex. C:\Python34 )

## Description:
This tool will open the url(s) given using Selenium and geckodriver to scrape and process most of the useful data for any movie, manga, or anime on AniList.co

It could be useful for someone who wants to save the metadata and the cover/banner art for their anime/manga collection.

## Usage:
When running the program, you can choose one of two modes:

**URL Mode:** downloads data for one url at a time that you can copy & paste into the program.

**List Mode:** downloads data for all of the urls listed in a text document.

## Examples:
**URL Mode**
![URL Mode Screenshot Terminal](https://raw.githubusercontent.com/NicholasDawson/Data-Extractor-for-AniList/master/Screenshots/url_mode.png "URL Mode Screenshot Terminal")

**List Mode**
![List Mode Screenshot Terminal](https://raw.githubusercontent.com/NicholasDawson/Data-Extractor-for-AniList/master/Screenshots/list_mode.png "List Mode Screenshot Terminal")

**Folder**
![Folder Screenshot](https://raw.githubusercontent.com/NicholasDawson/Data-Extractor-for-AniList/master/Screenshots/folder.png "Folder Screenshot")

**Files**
![Files Screenshot](https://raw.githubusercontent.com/NicholasDawson/Data-Extractor-for-AniList/master/Screenshots/files.png "Files Screenshot")

**Data JSON**
```json
{
  "Banner Image": "https://s4.anilist.co/file/anilistcdn/media/anime/banner/101921-rDCpn6FK0mHt.jpg",
  "Cover Image": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx101921-qSV6zMacSDm4.png",
  "Title": "Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen",
  "Description": "Kaguya Shinomiya and Miyuki Shirogane are the members of the incredibly prestigious Shuichi'in Academy's student council, asserting their positions as geniuses among geniuses. All the time they spend together has caused the two of them to develop feelings for each other, but their pride will not allow them to be the one to confess and become the submissive one in the relationship! Love is war, and their battle to make the other confess begins now!\n\n(Source: MangaUpdates)",
  "Format": "TV",
  "Episodes": "12",
  "Episode Duration": "24 mins",
  "Status": "Finished",
  "Start Date": "Jan 12, 2019",
  "End Date": "Mar 30, 2019",
  "Season": "Winter 2019",
  "Average Score": "83%",
  "Mean Score": "83%",
  "Popularity": "67784",
  "Favorites": "4096",
  "Studios": [
    "A-1 Pictures"
  ],
  "Producers": [
    "Mainichi Broadcasting",
    "Aniplex of America",
    "Aniplex",
    "Magic Capsule"
  ],
  "Source": "Manga",
  "Hashtag": "#かぐや様",
  "Genres": [
    "Comedy",
    "Romance",
    "Psychological"
  ],
  "Romaji": "Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen",
  "English": "Kaguya-sama: Love is War",
  "Native": "かぐや様は告らせたい～天才たちの恋愛頭脳戦～",
  "Synonyms": [
    "Kaguya Wants to be Confessed To: The Geniuses' War of Love and Brains"
  ],
  "tags": {
    "School": "86%",
    "Tsundere": "85%",
    "School Club": "84%",
    "Parody": "81%",
    "Slapstick": "77%",
    "Episodic": "65%",
    "Ensemble Cast": "56%",
    "Seinen": "40%",
    "Rotoscoping": "33%",
    "Female Protagonist": "20%"
  }
}
```

