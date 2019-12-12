count = 0

for x, y in zip(s1, s2):
        if x != y:
            count += 1

print(count)