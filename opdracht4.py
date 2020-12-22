import hashlib

input = "bgvyzdsv"
i = 1

while True:
    m = hashlib.md5()
    m.update((input + str(i)).encode())
    if m.hexdigest().startswith("00000"):
        print(i)   
    if m.hexdigest().startswith("000000"):
        print(i)
        break
    i += 1