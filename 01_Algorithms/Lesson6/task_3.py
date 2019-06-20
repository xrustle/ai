import sys
import ctypes
import struct

a = 42000
b = a
c = b
print(id(a))
print(sys.getsizeof(a))
print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack('LLLLLLl', ctypes.string_at(id(a), sys.getsizeof(a))))
print(id(int))

print('*' * 50)
f = 'Hello world!'
print(id(f))
print(sys.getsizeof(f))
print(ctypes.string_at(id(f), sys.getsizeof(f)))
print(struct.unpack('LLLLLLLLLLli' + 'c' * 13, ctypes.string_at(id(f), sys.getsizeof(f))))
print(id(str))
