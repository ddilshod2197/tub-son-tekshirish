def ekuk(a, b):
    max_val = max(a, b)
    min_val = min(a, b)
    ekuk = 0
    for i in range(1, min_val + 1):
        if a % i == 0 and b % i == 0:
            ekuk = i
    return ekuk

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

print("Eng kichik umumiy karrali:", ekuk(a, b))
