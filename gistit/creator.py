import sys
import time
import json
import requests

if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
    import urllib.error as urlerror
else:
    import urllib2
    import urlparse


class Creator:
    ''' Gist Creator class '''
    def create(self, content, public=True, filename=None):
        ''' Creates a gist with the following content '''
        url = 'https://api.github.com/gists'
        if not filename:
            filename = 'gistit' + time.strftime("_%Y-%m-%d_%H%M")   # "%d/%m/%Y"
        values = {
                'public' : public,
                'description' : 'Created using GistIt - http://is.gd/Gistit',
                'files' : {
                    filename: {
                        'content': content
                        }
                    }
                }
        # Create request
        values = json.dumps(values)
        r = requests.post(url, values)
        jsoon = json.loads(r.content.decode())
        return jsoon

    def temp(self):
        data = urlparse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib2.Request(url, data)
        # Send request
        try:
            response = urllib2.urlopen(req)         #res.geturl(), .url=str, .status=200, .info=200, .msg=OK,
        except urlerror.HTTPError as exep:
            print('The server couldn\'t fulfill the request.',
                  'Error code: ', exep.code)
            raise
        except urlerror.URLError as exep:
            print('We failed to reach a server.')
            print('Reason: ', exep.reason)
            raise
        except:
            raise
        else:
            # everything is fine
            the_page = str(response.read()) # More pythonic than .decode('utf-8')
            # Parse for success or failure
            print(the_page)

