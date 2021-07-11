import time
import hashlib
from urllib.request import urlopen, Request

url = Request('https://www.promiedos.com.ar/',
              headers={'User-Agent': 'Mozilla/5.0'})
# load the website
response = urlopen(url).read()

# standard and first hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        # load the website
        response = urlopen(url).read()

        # hash  the website
        currentHash = hashlib.sha224(response).hexdigest()

        # wait to perform the check
        time.sleep(30)

        # load the website
        response = urlopen(url).read()

        # new hash to the website
        newHash = hashlib.sha224(response).hexdigest()

        # check the new hash with the previous one
        if newHash == currentHash:
            continue

        # changes to the hash
        else:
            # print on console
            print("something changed")

            # again read the website
            response = urlopen(url).read()

            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()

            # wait
            time.sleep(30)
            continue

    # errors
    except Exception as e:
        print("error")
