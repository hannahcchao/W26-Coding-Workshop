def main():
    dna = "ATCTGATTACCGGGAC"
    a = []
    t = []
    c = []
    g = []
    for letter in dna:
        if letter == "A":
            a.append(letter)
        elif letter == "T":
            t.append(letter)
        elif letter == "C":
            c.append(letter)
        elif letter == "G":
            g.append(letter)
            
    freq = {"A": len(a), "T": len(t), "C": len(c), "G": len(g)}
    return (freq)
print(main())