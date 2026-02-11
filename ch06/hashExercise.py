key = "Emma"
h = hash(key)
print("Hash value:", h)

N = 8
index = h % N
print("Table size:", N)
print("Bucket index:", index)
print("Hash value:", h)

table = [None] * N
table[index] = "834-2019"   
print("Table:", table)


