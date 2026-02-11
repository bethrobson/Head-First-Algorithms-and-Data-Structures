phone_book = dict()

phone_book["Emma Johnson"] = "834-2019"
phone_book["Liam Smith"]   = "658-2934"
phone_book["Olivia Brown"] = "903-1748"
phone_book["Noah Davis"]   = "273-4816"

emma_number = phone_book.get("Emma Johnson")
noah_number = phone_book.get("Noah Davis", "not found")
ava_number  = phone_book.get("Ava Miller", "not found")

print(emma_number) 
print(noah_number)
print(ava_number)  

for key, value in phone_book.items():
    print(key, value)

