from cryptography.fernet import Fernet 

'''''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key() '''

def load_key():
    file = open("key.key", "rb")
    key = file.read()

    file.close()
    return key

main_password = input("What is your main password: ")

key = load_key() 
fer = Fernet(key)

def retrieve():

    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            account, password = data.split("|")

           
            print("The password for " + account + " is " + fer.decrypt(password.encode()).decode())
            
def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")



while True:
    mode = input("Do you want to (1) Add a new password or (2) Retrieve a password? Type add or retreive and press q to quit: ")   

    if mode == "q":
       break

    if mode == "add":
       add()
    elif mode == "retreive":
       retrieve()
    else:
      print("Invalid mode")
      quit

    