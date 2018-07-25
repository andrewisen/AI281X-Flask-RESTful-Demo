import urllib.request, urllib, json

# List all rooms for a the building "U-huset" or "Undervisningshuset at KTH.
# 		Based on: 						https://www.kth.se/places
# 		The public API is avaible here: 	https://www.kth.se/api/places/swagger/

# NOTE:
# 		Building-ID for U-huset: 	f3b6cf22-e7e9-491f-9214-7b79761beba7
# 		URL:						https://www.kth.se/api/places/v3/building/{id}

# SLL Error:
# If you are using "newer versions" of Mac OSX then you might get the error:
# 		[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
#
# This is probably because your version of Python doesn't include certifications.
# Install SLL certifications for newer Python, e.g. I use Python 3.7, by running the following in Terminal:
#		/Applications/Python\ 3.7/Install\ Certificates.command 

def getJSON(api_key):
	headers = {'Accept': 'application/json', 'api_key': api_key}    
	url = 'https://www.kth.se/api/places/v3/building/f3b6cf22-e7e9-491f-9214-7b79761beba7'
	req = urllib.request.Request(url, None, headers)
	response = urllib.request.urlopen(req)

	data = json.loads(response.read().decode())
	return data

def main():
	api_key = input("Please enter API key: ")
	data = getJSON(api_key)
	print(data)

if __name__ == '__main__':
	main()