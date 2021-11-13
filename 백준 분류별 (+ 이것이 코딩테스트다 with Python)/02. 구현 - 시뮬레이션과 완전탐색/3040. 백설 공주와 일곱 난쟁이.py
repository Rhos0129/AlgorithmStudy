from itertools import combinations

dwarfs=sorted([int(input()) for i in range(9)])

# 난쟁이가 아닌 2명을 찾자
diff=sum(dwarfs)-100
for notDwarf1, notDwarf2 in combinations(dwarfs, 2):
    if notDwarf1+notDwarf2==diff:
        dwarfs.remove(notDwarf1)
        dwarfs.remove(notDwarf2)
        break

dwarfs.sort()
for dwarf in dwarfs:
    print(dwarf)

