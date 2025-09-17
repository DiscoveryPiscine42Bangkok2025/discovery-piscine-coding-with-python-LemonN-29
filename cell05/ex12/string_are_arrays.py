import sys

if len(sys.argv) != 2:
    print("none")

s = sys.argv[1]
count = s.count('z')
if count == 0:
    print("none")
else:
    print("z" * count)

