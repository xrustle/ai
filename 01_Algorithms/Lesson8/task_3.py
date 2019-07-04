import hashlib

s = 'Hello, вау world!'

print(hash(s))
print(hash(s))
print(hash(s))
# -3732018269567937720

print(hashlib.sha1(s.encode('utf-8')).hexdigest())
print(hashlib.sha256(s.encode('utf-8')).hexdigest())
print(hashlib.sha512(s.encode('utf-8')).hexdigest())


