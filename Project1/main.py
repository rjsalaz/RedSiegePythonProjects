from sys import argv,exit
from getopt import getopt,GetoptError
from ApiCall import getIpInfo
from Display import displayResponse


def main(argv):

    inputIpAddress: str = ''
    inputFile: str = ''
    apiResponse: str = ''

    try: 
        opts,args = getopt(argv,"ha:f:", ["IpAddress=","inputFile="])
    
    except GetoptError:
        print("main.py -a [ip address]")
        print("EX) main.py -a 8.8.8.8")
        exit(2)
    
    for opt, args in opts:

        if opt == "-a":

            inputIpAddress = args
            apiResponse = getIpInfo(inputIpAddress)
            displayResponse(apiResponse)


        elif opt == "-f":
            print()


        elif opt == "-h":
            print("")
            exit(2)


if __name__ == '__main__': 

    main(argv[1:])