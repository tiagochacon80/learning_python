import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.google.com")
except:
    print("Erreur")
else:
    print("Tout va bien")