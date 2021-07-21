qte = int(input())

yes = 0
no = 0

for i in range(qte):
    value = int(input())
    if(value >= 10 and value <= 20):
        yes += 1
    else:
        no += 1

print("%d in" %yes)
print("%d out" %no)
