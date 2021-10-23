import requests

def getIpInfo(ipAddress):

    apiKey: str = "807a4e07686e4e848904720eafab7430" 
    apiUrl: str = "https://api.ipgeolocation.io/ipgeo"

    payload= {"apiKey":apiKey, "ip":ipAddress}
    response = requests.get(apiUrl, params=payload)
    
    return response.json()
