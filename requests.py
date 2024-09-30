import requests
def vienkarss_get(url):
    requests.get('https://api.github.com')
    r = requests.get('https://api.github.com')
    r.status_code
    if r.status_code == 200:
        print("success!")
        print("statusa kods: ()".format(r.status_code))
        #biblioteku papild resurs