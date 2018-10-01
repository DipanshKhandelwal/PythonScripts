from pyshorteners import Shortener
url = input()
api_key = 'AIzaSyCvh--mrya0GvQSo5LEXdme8dCMdTBXNfU'
shortener = Shortener('Google', api_key=api_key)
print("You are ready to go : " + format(shortener.short(url)))
