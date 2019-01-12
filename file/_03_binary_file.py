# Write a binary data to a file
with open('03.binary_file', 'wb') as file:
    file.write(b'Life is awesome')

# Read a binary data from file
with open('03.binary_file', 'rb') as file:
    read_as_binary = file.read()
    print(read_as_binary)
    # output: b'Life is awesome'
    print(read_as_binary.decode('utf-8'))
    # output: Life is awesome
