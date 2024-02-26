# Automatic Text-To-Speech

This repository contains a text-to-speech pipeline that scrapes text from a webpage, preprocesses it, converts it into speech using OpenAI's text-to-speech API, and subsequently combines the audio files if necessary. It is designed to work with efficiency by distributing tasks across multiple threads for speed.

## Overview of Each Step

**_1_scrape.py**: This takes care of scraping a webpage and saving the content in a '.txt' file *(Optional if you add your own .txt files to the /files directory)*

**_2_prep_text_files.py**: Preprocesses the text files ensuring that they are of the correct format and splits any files larger than 4096 characters.

**_3_TTS.py**: Takes the text in each file and converts it into speech using the OpenAI API. The resulting audio is saved in an '.mp3' format.

**_4_combine.py**: Combines all the split audio files and stores them in '/files/audio/combined'.

It is built using Python and leverages various libraries such as BeautifulSoup for web scraping, os and shutil for file manipulation, and OpenAI's library for text-to-speech conversion. It can be launched through docker compose.

## Setup Instructions

**Requirements: [Docker](https://docs.docker.com/get-docker/), [OpenAI API KEY](https://openai.com/blog/openai-api)**

 1. Clone this repository with `git clone https://github.com/tavindotson/auto-tts.git` then `cd auto-tts`
 2. Create a '.env' file from the provided 'env.template' and update it with your OpenAI API KEY,
		Linux: `cp env.template .env ; nano .env`
 3. Start with docker-compose.
		`docker compose up -d`
 4. Open a shell into the container
		`docker exec -it auto-tts sh`
 6. Run the scripts in order inside the container
		`python _1_scrape.py`
		`python _2_prep_text_files.py`
		`python _3_TTS.py`
		`python _4_combine.py`
 7. The finished MP3s will be in `/files/audio/combined`

## Contributing

TBD

## License

TBD
