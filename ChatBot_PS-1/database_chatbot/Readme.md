# Database

## Responsibilities

* Stores responses based on intent and entities
* Has features to populate and edit the DB content

## Team 

* Chirag Singhal
* Anirudh

## How to setup?

Make sure you have **pip** and mysql is installed. Change the database details in `settings.py` Open up the terminal and type -

    git clone https://github.com/chirag-singhal/ChatBot_PS-1.git
    cd ChatBot_PS-1
    pip install virtualenv
    virtualenv chatbot
    source chatbot/bin/activate
    pip install -r requirements.txt
    cd databse_chatbot
    python3 manage.py createsuperuser
    python3 manage.py makemigrations
    python3 manage.py migrate --run-syncdb
    python3 manage.py runserver
    
# nlp_chatbot

## Team 

* Ashrya Agrawal 
* Shubh Shah
* Sanjeet Kapadia

To install dependencies, execute the following command
```
pip install -r requirements.txt
```

Now you need to use the nlp module once to get the 400Mb BERT model downloaded

Open python interactive console and execute following lines in that interactive session:
```
from nlp_module import nlp_module
nlp = nlp_module()
```

Now you can start the django server. There's no further need of configuring/setting-up NLP engine.
