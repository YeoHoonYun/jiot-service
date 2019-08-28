import homeassistant.remote as remote

api = remote.API('172.30.1.39', 'password')
print(remote.validate_api(api))