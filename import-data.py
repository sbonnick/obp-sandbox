import requests
import os, sys, json
from dotenv import load_dotenv

load_dotenv()

USERNAME      = 'admin'
PASSWORD      = 'Obp#1234567890'
CONSUMER_KEY  = 'zmpkpwsa5mpuovsp0ms00c5agwzofwixlypolpet'
BASE_URL      = "http://" + os.getenv("domain") + ":8080"
API_VERSION   = "v3.1.0"

CONTENT_JSON  = { 'content-type'  : 'application/json' }

login_url     = '{0}/my/logins/direct'.format(BASE_URL)
login_header  = { 'Authorization' : 'DirectLogin username="%s",password="%s",consumer_key="%s"' % (USERNAME, PASSWORD, CONSUMER_KEY)}


print('Login as {0} to {1}'.format(login_header, login_url))
r = requests.post(login_url, headers=login_header)
if (r.status_code != 201):
    print("error: could not login", file=sys.stderr)
    print("text: " + r.text, file=sys.stderr)
    exit(100)
t = r.json()['token']
print("Received token: {0}".format(t))

DL_TOKEN = { 'Authorization' : 'DirectLogin token=%s' % t}

with open(os.getenv('datafile')) as json_file:  
    IMPORT_DATA = json.load(json_file)

response = requests.post(u"{0}/obp/{1}/sandbox/data-import".format(BASE_URL, API_VERSION), json=IMPORT_DATA, headers={**DL_TOKEN, **CONTENT_JSON})
print("code=" + str(response.status_code) + " text=" + response.text)
if (r.status_code != 201):
    print("code=" + str(response.status_code) + " text=" + response.text, file=sys.stderr)
    exit(100)