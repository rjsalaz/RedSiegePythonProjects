import requests

def getIpInfo(ipAddress):

    # Your key goes here
    apiKey: str = "" 
    apiUrl: str = "https://api.ipgeolocation.io/ipgeo"

    payload= {"apiKey":apiKey, "ip":ipAddress}
    response = requests.get(apiUrl, params=payload)
    
    return response.json()
