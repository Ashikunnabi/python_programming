# continue works as SKIPPING

for i in range(1, 100):
    if i % 2 == 0:
        continue
    else:
        print(i, end=" ")
