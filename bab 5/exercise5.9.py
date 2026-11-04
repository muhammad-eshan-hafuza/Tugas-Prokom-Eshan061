# Kita buat list kosong untuk menguji kasus tidak ada user
usernames = []

# Cek apakah list ada isinya
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")