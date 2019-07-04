import hashlib


def rabin_karp(s, subs):
    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            return i

    return None


print(rabin_karp('Hello, world!', 'world'))
