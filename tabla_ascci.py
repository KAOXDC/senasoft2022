print("programa para ver la tabla del codigo ascii")

for i in range(32, 127):
    print(i, chr(i), end="\t")
    if i % 10 == 0:
        print()