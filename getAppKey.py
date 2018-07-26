def main():
	with open('app_key.txt') as file:
		app_key = file.read()
	file.closed

	return app_key

if __name__ == '__main__':
	main()