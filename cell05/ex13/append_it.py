import sys

args = sys.argv[1:]
output = []
for arg in args:
    if not arg.endswith("ism"):
        output.append(arg + "ism")
    if not output:
        print("none")
    else:
        for item in output:
            print(item)