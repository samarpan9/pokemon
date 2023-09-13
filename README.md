First create the virtual environment and install all the dependencies using requirements file.

To create a virtual environemnt:
```
python3 -m venv venv
```
now activate it.

once done install all the dependencies:
```
pip install -r requirements.txt
```

i've created a config file for easy database configuration instead of assigning the value into the environment.

Populate the config file with your postgresql database

now that everything is setup.

Use seed.py to fetch all the data from pokeAPI as such:

```
python3 seed.py
```

It will fetch all the data using the api_handler and store all the data into postgresql.

In api handler's fetch_pokemon_data,
I've used the limit to fetch just 10 pokemon data. if it is required to fetch all the pokemons than use the other provided url_link with no limits and also uncomment the while, break and next_url statements of line 11, 16, and 41. uncommenting this will fetch all the pokemon data.

i've used normal sql queries instead of using the ORM because of that not being a requirement and also because i wanted to use raw queries for this oroject.

once the data is fetched and stored.

there is no need to call the api anymore. the data is all stored in a single request.

Now run the main file to provide the api endpoints.

To run the main file:
```
uvicorn main:app --reload   
```

once started:
visit: /api/v1/pokemons


Apart from the basic functionalities, i've also added the feature for pagination to control the number of data.
