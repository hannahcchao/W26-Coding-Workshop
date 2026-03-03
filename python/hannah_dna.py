def main():
    dna = "ATCTGATTACCGGGAC"
    a = []
    t = []
    c = []
    g = []
    for letter in dna:
        if(letter == "a"):
            a.append(letter)
        elif(letter == "t"):
            a.append(letter)
        elif(letter == "c"):
            a.append(letter)
        elif(letter == "g"):
            a.append(letter)
    freq = {"A": a.len(), "T": t.len(), "C": c.len(), "G": g.len()}
    return freq