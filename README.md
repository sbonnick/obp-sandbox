# NOTICE
This repository and all code in it is intended for development or exploratory purposes only of the OpenBankProject service. This should never be used as is in any production environment. Many of the ideas, code and examples are derivatives of work by the OpenBankProject group on GitHub: https://github.com/OpenBankProject


# Quick start
To use vagrant, run the following command to launch:
```
vagrant up
```

These commands will start the services and populate it with some default data. Services will now be accessible at the following URLs using your computer name as the domain:
```
API: http://<domain>:8080
API Explorer: http://<domain>:8082
Social Banking: http://<domain>:8081
```

For here, you can either log into the API Explorer using the following credentials (or another from the `example_import.json` file) or get a auth token for this user to use the API directly:
```
 user_name: robert.xuk.x@example.com
 password:  5232e7
```

## NOTES
- When manually logging into the API Explorer, the OAuth does not always redirect you back to the API Explorer after logging in. If it does not, replace `<localhost>` in the browser URL bar with your correct set domain.


# Advanced Setup

## Using docker native instead of vagrant
To use docker on your local system instead, use this command to launch (refer to vagrant file for requirements):
```
docker-compose up -d
pip3 install -r requirements.txt
python3 import-data.py
```

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

## Querying transactions for a given bank and account
Given a test user `robert.xuk.x@example.com`, using the above mentioned password and the API Explorer consumer key, a token can be retrieved using:
```
curl -X POST \
  http://<DOMAIN>:8080/my/logins/direct \
  -H 'authorization: DirectLogin username=\"robert.xuk.x@example.com\",password=\"5232e7\",consumer_key=\"zmpkpwsa5mpuovsp0ms00c5agwzofwixlypolpet\"' \
  -H 'content-type: application/json' \
```

Taking the token retrieved above and assuming the bank `psd201-bank-x--uk` and account `05237266-b334-4704-a087-5b460a2ecf04`, you can query all transactions using:
```
curl -X GET \
  http://<DOMAIN>:8080/obp/v3.1.0/banks/psd201-bank-x--uk/accounts/05237266-b334-4704-a087-5b460a2ecf04/accountant/transactions \
  -H 'authorization: DirectLogin token=\"<TOKEN FROM PREVIOUS CURL>\"' \
  -H 'content-type: application/json' \
```


# Whats happening under the hood

whats happening... Its networking turtles all the way down!

```
Host (services exposed locally only)
  + - Vagrant VM (port forward 8080 - 8082 to host)
    + - Docker Service (using host networking)
      + - OBP Container
        + - API Service (port 8080)
          + - OAUTH Endpoint ServiceS
        + - API Explorer Service (port 8082)
        + - Social Banking Service (port 8081)
```

Using the hosts domain name is important here when configuring a deployment since the VM will be given the same name. This cheats a little by ensuring all internal and host-internal traffic flows to the correct endpoints.
