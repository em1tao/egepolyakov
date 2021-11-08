variants = []

for a in range(2):
	for b in range(2):
		for c in range(2):
			for d in range(2):
				a = bool(a)
				b = bool(b)
				c = bool(c)
				d = bool(d)
				func = (not a or b) and not (b == c) and (not d or a)
				variants.append((a,b,c,d,func))
print("A   B   C   D   F")
variants = list(filter(lambda x: x[4], variants))
print(*variants,sep="\n")

