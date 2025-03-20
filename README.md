
## Make and Enter a Python Virtual Environment (venv)
```
# Creating a base virtual environment
python -m venv venv
# Entering the virtual environment
source venv/bin/activate
# Installing the python dependencies into the virtual environment
python -m pip install -r requirements.txt
```

## How to exit a Virtual Environment
```
deactivate
```

## Example files
`example.py -> querying a database`
`test.py -> testing the query function in example.py`


## How to run a Docker Container with 'Docker Compose`
There is a mysql container defined in `docker-compose.yaml`
This can be run with the following command:
```
docker compose up
```
And stopped with `Ctrl-C`
