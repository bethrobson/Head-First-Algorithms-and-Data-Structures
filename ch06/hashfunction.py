def my_hash(s: str) -> int:
    return ord(s[0]) % 10

table = dict()

hash = my_hash("Dallas");      table[hash] = ("Dallas", "75001")
hash = my_hash("Austin");      table[hash] = ("Austin", "73301")
hash = my_hash("Houston");     table[hash] = ("Houston", "77002")
hash = my_hash("San Antonio"); table[hash] = ("San Antonio", "78205")
hash = my_hash("Phoenix");     table[hash] = ("Phoenix", "85004")
hash = my_hash("Los Angeles"); table[hash] = ("Los Angeles", "90012")
hash = my_hash("Savannah");    table[hash] = ("Savannah", "31401")
hash = my_hash("Charlotte");   table[hash] = ("Charlotte", "28201")
hash = my_hash("New Haven");   table[hash] = ("New Haven", "06510")

# collisions overwrite
for key, value in table.items():
    print(key, value)

