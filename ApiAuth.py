user_database = []

print("---- Register ----")

new_username = input("Masukkan Username Baru: ")
new_password = input("Masukkan Password Baru: ")

new_user = {
    "username": new_username,
    "password": new_password
}

user_database.append(new_user)
print(user_database)



print("---- Login ----")

new_username = input("Masukkan Username:")
new_password = input("Masukkan Password:")

status_login = False
for user in user_database:
    if user["username"] == new_username and user["password"] == new_password:
        status_login = True
        break

if status_login:
    print("Login Berhasil")
else:
    print("Login Gagal")

