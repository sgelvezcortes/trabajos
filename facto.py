def fact(n):
    if n > 0 :
        fact = 1
        i = 1
        while i <= n :
            fact *= i
            i = i + 1
        return fact
    elif n < 0 :
        return 0
    else :
        return 1
filas = 10
for n in range(filas):
    for r in range(n + 1) :
        print(f"({n}, {r}) = { fact(n) // (fact(r) * fact(n - r)) }  ", end="")
    print("")
    
print("gatico")