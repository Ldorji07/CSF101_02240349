import requests

url = "https://csf101-server-cap1.onrender.com/get/input/349"  
response = requests.get(url)

with open("downloaded_file.txt", "w") as file: 
    file.write(response.text)

print("File Downloaded Successfuly")