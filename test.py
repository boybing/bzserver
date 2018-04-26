from urllib import request
from urllib.parse import quote
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
str="http://127.0.0.1:8000"
req = request.Request(quote(str, safe='/:?='))
req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
with request.urlopen(req) as response:
    print(response.read().decode("utf-8"))