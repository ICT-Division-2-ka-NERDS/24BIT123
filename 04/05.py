# 24bit123

# Que-5

for a in range(1, 31):
    for b in range(1, 31):
        for c in range(1, 31):
            if a**2 + b**2 == c**2:
                print(a, b, c, sep=", ")
