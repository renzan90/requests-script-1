import requests

r = requests.get('https://imgs.xkcd.com/comics/python.png')

print(r.headers)

#print(r.status_code)

#returns all the headers such as name of the server (nginx in this case), content type etc. 
#'headers' might refer to the crucial information about the given link/resource
#status 200: it's working
#status 300: redirect
#status 400: http error