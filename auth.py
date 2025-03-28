def login(username, password):
if username == "admin" and password == "password":
return "Login Successful"
else:
return "Invalid Credentials"
print(login("admin", "password"))

ok