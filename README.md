
# RAG-CHAT

## Retrieval-Augmented Generation demo

A simple demo to store your own data locally and use OpenAI:s API to answer questions with that data as context.
I made it to learn more about RAG and used sample data I had written myself to be able to see if the answers are correct or hallucinations. 


# Prerequisites
- Python 3.12 (not tested on earlier versions)
- An OpenAI API key
- Your data in a single text file

# Data storage
Your data is stored in a Chroma vector database on your file system (location controlled by environment variable in settings.py)

# Setup
- Create a virtual environment and install dependencies from requirements.txt  
- Add your OpenAI API key as an environment variable. `export OPENAI_API_KEY=YOUR_API_KEY` (or `set`instead of `export`on Windows.) The OpenAI API key is the only required environment variable, everything else has default values.
- Prepare your data into a single text file and run `python src/load_vector_db.py <file_name>`
- If you use the sample data, the command is: `python src/load_vector_db.py sample_data/sample_data.txt` A directory is created where the database is stored
- Check `src/settings.py` and set environment variables if you don't want the default values.

# Tests
` python -m unittest tests/`

# Run the program
`python main.py`
the number of previous queries that are included is controlled by environment variables

# Sample data
Texts from https://wordpress.com/view/interrailinfosvenska.wordpress.com are found in a file in the /sample_data directory. 
If you use this data you can ask questions about train travel with Interrail, but you'll get answers in Swedish.

# Formatting & linting
`ruff format` and `ruff check`is used.

# Output
Q & A-logs are saved to files in a `chat_logs` directory which is created automatically. 
In addition to questions and answers, some more data is saved (model, temperature etc)

# Limitations 
- Local only, no API
- If you have a lot of data to ingest into the vector database, a single file might be too big. 
- No rotation of the chat history file 

# Reset
Stop the program and delete the database folder and its contents. 
load data into a new databse, as described in setup.

# License
MIT License, see the file `LICENSE`


# Credits & inspiration
https://github.com/tolo
https://github.com/AllAboutAI-YT/easy-local-rag










