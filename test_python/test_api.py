from requests import post, get
url = 'https://graph.api.smartthings.com/api/smartapps/endpoints'
headers = {
        'Authorization': 'Bearer a9803523-9688-4773-a088-a43898088a80'
    }
print(get(url, headers=headers).text)

x = 1
while(True):
    print("---------------------------------------------------------------------------------")
    url = 'https://graph-na04-useast2.api.smartthings.com/api/smartapps/installations/' + str(x) + '/devices'
    print(url)
    headers = {
            'Authorization': 'Bearer a9803523-9688-4773-a088-a43898088a80'
        }
    print(get(url, headers=headers).text)
    x += 1
    print("---------------------------------------------------------------------------------")