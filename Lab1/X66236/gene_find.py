import sys
def gene_find(s):
    n=len(s)
    i=0
    while i+2 <= n:
        if s[i:i+3]== "ATG":
            j=i+3
            while j+2 <= n:
                if s[j:j+3] in {"TTA","TAG","TGA"}:
                    return s[i:j+3]
                j=j+3
        i=i+1
    return ""

s = sys . stdin . readline (). strip ()

print ( gene_find ( s ))
