## extracting zip with password
import zipfile
import itertools

while True:
    digits = list(range(0, 10))
    file_name = 'test.zip'
    for permutation in itertools.product(digits, repeat=4):
        passwrd= str(permutation)
        with zipfile.ZipFile(file_name) as file:
            try:
                file.extractall(passwrd = bytes(passwrd, 'utf-8'))
            except:
                print("fuuuuuuuuuck")
            
  

