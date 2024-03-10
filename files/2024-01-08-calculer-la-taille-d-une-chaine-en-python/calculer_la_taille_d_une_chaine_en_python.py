"""
https://www.youtube.com/watch?app=desktop&v=ut74oHojxqo

https://www.youtube.com/watch?v=uTJoJtNYcaQ

"""

import sys


print("# SIZE IN RAM")
print("CODE POINT    SIZE IN RAM  CHAR")
last_size_ram = 0
for ucp in range(sys.maxunicode):
    if last_size_ram == sys.getsizeof(chr(ucp)):
        continue
    last_size_ram = sys.getsizeof(chr(ucp))
    print(f"{ucp:10} {last_size_ram:>14} {chr(ucp):>5}")

print("\n# SIZE IN UTF-8")
print("CODE POINT  SIZE IN UTF-8  CHAR")
last_size_utf8 = 0
badids = []
surrogate_pairs = range(55296, 57343 + 1)
valid_ucps = [_i for _i in range(sys.maxunicode) if _i not in surrogate_pairs]
for ucp in valid_ucps:
    if last_size_utf8 == sys.getsizeof(chr(ucp).encode("utf-8")):
        continue
    last_size_utf8 = sys.getsizeof(chr(ucp).encode("utf-8"))
    print(f"{ucp:10} {last_size_utf8:>14} {chr(ucp):>5}")


hex(163)
print(f"{163:20b}")
print(f"{16993:020b}")
print(f"{16993:20b}")

