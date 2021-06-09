
from urllib.request import urlopen

import urllib.error as urlError

from socket import gaierror

try:
    
    response = urlopen('http://www.debianxyz.org')

    print(response)

    print(response.readline().decode())

    print('Status ', response.status)

    print(response.read(50).decode())
    
except(urlError.URLError, gaierror ):
    
    print('deu merda')

    print('status')

try:

    urlopen('http://www.ietf.org/rfc/rfc0.txt')

except urlError.HTTPError as e:
    
    print('Error ', e.code, e.reason)
    
    print('url', e.url)

