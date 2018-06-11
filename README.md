# lego.py
`lego.py` is an experimental server emulator for the now-defunct MMORPG, Lego Universe, written in Python 3.6.5. Please note that the server is still a constant work in progress and will not always be stable. Please check the releases page for the most stable distributions of the program.

## Getting started
Once the repository has been cloned in your environment, run `pip3 install -r requirements.txt` before starting the server. Next, be sure to download and install the latest release of the MongoDB community server from [here](https://www.mongodb.com/download-center?jmp=nav#community). Once installed, open a bash terminal and execute the following commands: `mkdir resources/data/db`, `mongod --dbpath resources/data` (or replace the dbpath argument with your own specified location where you'd like to store the database-related files).
