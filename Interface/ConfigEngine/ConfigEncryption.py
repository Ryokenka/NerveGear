from cryptography.fernet import Fernet

# Generate a key
# key = Fernet.generate_key()
key = b'0TJVCP3wtoexfWyLermEVcv8TlnvRVikFkTVbL41-hA='

# Create a Fernet cipher object with the key
cipher = Fernet(key)

config_path = "config.txt"

def encrypt_string(string):
    return cipher.encrypt(string.encode())

def decrypt_string(encrypted_string):
    return cipher.decrypt(encrypted_string).decode()


# TEST
# code = encrypt_string("Hello, world!")
# print(code)
# print(decrypt_string(code)) 

def config_to_string(config_path):
    try:
        # Open the file in read mode
        with open(config_path, 'r') as file:
            # Read the entire content of the file into a string
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print("File not found.")
        return None
    
def string_to_config(config_path, content):
    try:
        # Open the file in write mode
        with open(config_path, 'w') as file:
            # Write the string content to the file
            file.write(content)
        print("String successfully written to file:", config_path)
    except IOError:
        print("Error writing to file.")