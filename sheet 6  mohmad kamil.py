#file io 
#1
with open('example.txt', 'w') as file:
    file.write("Hello from file")

#2
with open('example.txt', 'a') as file:
    file.write("\nYour Name")


#3
with open('example.txt', 'a') as file:
    for num in range(1, 101):
        file.write(f"{num}\n")
 
#4
with open('example.txt', 'r') as file:
    lines = file.readlines()  
    for line in lines[49:60]:  
        print(line.strip())
        

#JSON
#1
import json
users = {
    "users": [
        {"username": "user1", "password": "password1"},
        {"username": "user2", "password": "password2"},
        {"username": "user3", "password": "password3"}
    ]
}
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)
    
#2
import json
with open("users.json", "r") as file:
    data = json.load(file)
first_user = data["users"][0]
print(f"Username: {first_user['username']}, Password: {first_user['password']}")

#3
import json
new_username = input("Enter the new username: ")
new_password = input("Enter the new password: ")
with open("users.json", "r") as file:
    data = json.load(file)
new_user = {"username": new_username, "password": new_password}
data["users"].append(new_user)
with open("users.json", "w") as file:
    json.dump(data, file, indent=4)

print(f"New user '{new_username}' has been added.")

#4
import json
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
with open("users.json", "r") as file:
    data = json.load(file)
user_found = False
for user in data["users"]:
    if user["username"] == username_input and user["password"] == password_input:
        user_found = True
        print("Login successful!")
        break

if not user_found:
    print("Invalid username or password.")


#Math
import math

radius = 4.5

area = math.pi * radius ** 2

print(f"The area of the circle with radius {radius} is {area}")