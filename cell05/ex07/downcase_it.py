import sys

print(sys.argv)
if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].lower())