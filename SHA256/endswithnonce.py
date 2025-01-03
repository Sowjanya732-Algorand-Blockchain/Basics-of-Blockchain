import hashlib
import time
# pip install hashlib

# Example input string
block = input("Enter Block Number: ")
nonce = 0
data = input("Enter Block Data: ")
input_data = f"{block}{nonce}{data}"

# Convert input data to bytes
input_bytes = input_data.encode('utf-8')

# Hash the data using SHA256
sha256_hash = hashlib.sha256(input_bytes)

# Get the hexadecimal representation of the hash
hex_hash = sha256_hash.hexdigest()

print("SHA256 Hash: ", hex_hash)

target_zeros = "000000"
start_time = time.time()
while True:
    test_string = f"{block}{nonce}{data}"
    test_hash = hashlib.sha256(test_string.encode('utf-8')).hexdigest()
    if test_hash.endswith(target_zeros):
        print(f"Found Nonce: {nonce} => {test_hash}")
        print(f"Time Taken: {time.time() - start_time}")
        break
    nonce += 1