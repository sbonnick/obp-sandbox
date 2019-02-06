# NOTICE

This repository and all code in it is intended for development or exploratory purposes only of the OpenBankProject service. This should never be used as is in any production environment. Many of the ideas, code and examples are derivatives of work by the OpenBankProject group on GitHub: https://github.com/OpenBankProject

# Quick start
To use vagrant, run the following command to launch:
```
vagrant up
```

To use docker on your local system instead, use this command to launch (refer to vagrant file for requirements):
```
docker-compose up -d
pip3 install -r requirements.txt
python3 import-data.py
```

These commands will start the services and populate it with some default data. Services will now be accessible at the following URLs using your computer name as the domain:
```
API: http://<domain>:8080
API Explorer: http://<domain>:8082
Social Banking: http://<domain>:8081
```

For here, you can either log into the API Explorer using the following credentials (or another form the `example_import.json` file) or get a auth token for this user to use the API directly:
```
 user_name: robert.xuk.x@example.com
 password:  5232e7
```

## NOTES

- When manually logging into the API Explorer, the OAuth does not always redirect you back to the API Explorer after logging in. If it does not, replace `<localhost>` in the browser URL bar with your correct set domain.

# Advanced Setup

## Custom configs
Create a `.env` and add the following. If you do not create one manually, one will be created for you with the following settings. by default, your computer name is used for the domain.
```
domain=localhost
TZ=America/Toronto
loglevel=info
datafile=example_import.json
```

## Changing default data
By default, the example_import.json is loaded into the service for hosting. Data in here cna be changed, or a separate data set cna be used by adjusting the .env `datafile` entry.

## Querying transactions

TODO: add curl example to query all transactions under robert