import helloJSON as hJ

def main():
	api_key = input("Please enter API key: ")
	data = hJ.getJSON(api_key)

	selectedRooms = ["Hörsal","Övningssal","Break-Out område"]

	for eachRoom in data['rooms']:
		if eachRoom['typeName'] in selectedRooms:
			print(eachRoom['placeName'])

if __name__ == '__main__':
	main()