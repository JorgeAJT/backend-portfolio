def DNA_strand(dna_chain):
    dna = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return "".join(map(lambda c: dna[c], dna_chain))

print(DNA_strand("ATTC"))