import requests
url= 'https://play.google.com/store/apps/details?id=com.google.android.youtube'
r = requests.get(url)

print (r.text)