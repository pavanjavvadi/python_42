import urllib.request

site_link = input("Enter copied link: ")

getcode = urllib.request.urlopen(site_link).getcode()
print("status:",getcode)
