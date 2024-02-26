# Automatic Text-To-Speech

This repository contains a text-to-speech pipeline that scrapes text from a webpage, preprocesses it, converts it into speech using OpenAI's text-to-speech API, and subsequently combines the audio files if necessary. It is designed to work with efficiency by distributing tasks across multiple threads for speed.

## Consists of four stages:

_1_scrape.py: This takes care of scraping a webpage and saving the content in a '.txt' file. (Optional if you add your own .txt files to the /files directory)

_2_prep_text_files.py: Preprocesses the text files ensuring that they are of the correct format and splits any files larger than 4096 characters.

_3_TTS.py: Takes the text in each file and converts it into speech using the OpenAI API. The resulting audio is saved in an '.mp3' format.

_4_combine.py: Combines all the split audio files and stores them in '/files/audio/combined'.

The pipeline is built using Python and leverages various libraries such as BeautifulSoup for web scraping, os and shutil for file manipulation, and OpenAI's library for text-to-speech conversion. It can be launched through docker-compose using the provided Dockerfile and docker-compose.yml.

## Instructions to Use:

**Requirements: Docker, OpenAI API KEY**

Clone this repository with 'git clone (repository)', followed by 'cd (repository)'.

Create a '.env' file from the provided 'env.template' and update it with your OpenAI API KEY.

Build and start the docker-compose.

Run the individual scripts in order.

The resulting '.mp3' files can be found in the /files/audio/combined directory.

## Contributing

## License
