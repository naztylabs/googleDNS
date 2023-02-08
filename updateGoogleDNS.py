# Update Google DNS records automagically using Python Requests
import requests
import os
import logging
from datetime import datetime

timeNow = str(datetime.now())

START = ' [START] '
END = ' [END] '
INFO = ' [INFO] '
ERROR = ' [ERROR] '

domain1 = '' # input the domain name (i.e. if full route is home.myserver.com, put in home)
domain2 = '' # If using a second domain, uncomment and fill in lines 53-56

# Spin up a logger program within the current directory
def initializeLogger():
    responseLog = './response.log'
    if os.path.exists(responseLog):
        logging.basicConfig(filename=responseLog,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%m-%d-%Y-%H:%M:%S',
                            level=logging.DEBUG)
    else:
        with open(responseLog, 'x') as f:
            f.write('Initial Log Creation')
    
    # Silence urllib's debugger unless there is a warning message
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    
    logging.info(timeNow + START + 'Updating DNS Records')

# External IP
def getExternalIP():
    response = requests.get('http://myexternalip.com/raw')
    if response.status_code == 200:
        externalIP = response.text
        return externalIP
    else:
        logging.error(timeNow + ERROR + 'Unable to fetch external IP. Returned status code: ' + response.status_code)
        exit(response.status_code)

# Update Google Domain's Dynamic DNS Page
def updateGoogleDNS(domain):
    # Currently accepts one domain.
    if domain == domain1:
        logging.info(timeNow + INFO + 'Updating ' + domain)
        username = '' # input username from google dynamic dns
        password = '' # input password from google dynamic dns
    # To specify a second domain, uncomment below lines
    # elif domain == domain2:
        # logging.info(timeNow + INFO + 'Updating ' + domain)
        # username = '' # input username from google dynamic dns
        # password = '' # input password from google dynamic dns
    else:
        logging.error(timeNow + ERROR + 'Unable to parse domain')
        exit(1)
    
    domain = domain + '' # Insert the rest of your domain here (i.e. if full route is home.myserver.com you'd put in myserver.com)

    try:
        updateURL = 'https://{}:{}@domains.google.com/nic/update?hostname={}&myip={}'.format(username, password, domain, getExternalIP())
    
        updateResponse = requests.post(updateURL)
        logging.info(timeNow + END + 'Updated for domain: ' + domain + '. Response: ' + updateResponse.text)
    except:
        logging.error(timeNow + ERROR + 'Failed to update for domain: ' + domain + '. Response: ' + updateResponse.text)

def main():
    initializeLogger()
    updateGoogleDNS(domain1)
if __name__ == '__main__':
    main()