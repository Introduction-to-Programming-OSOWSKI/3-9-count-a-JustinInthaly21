def countA(w):
    t = 0
    for i in range(0, len(w)):
        t = t + i
        if w[i] == "a":
            return t + 1
         

print(countA("macaaa"))
