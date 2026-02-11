# if we don't choose a good key, we can overwrite values
library = {}
print("Library using title only as key:")
library["The Sorting Hat"] = "A book about sorting students"
library["Algorithms"] = "An introduction to algorithms"
library["Hash it out"] = "Arguing? No, math"
library["The Pivot Paradox"] = "An algorithmic mystery"
library["Algorithms"] = "Let's get serious about algorithms"
library["Time and Space"] = "The entire universe... of algorithms"

print(library)
print(library["Algorithms"])

# combine the title and author to get better keys (more likely to be unique)
library = {}

print("\nLibrary using title, author tuple as key:")
library[("The Sorting Hat", "Prof. Dumbledata")] = "A book about sorting students"
library[("Algorithms", "Ada Logic")] = "An introduction to algorithms"
library[("Hash it Out", "Pat Tern")] = "Arguing? No, math"
library[("The Pivot Paradox", "Quinn Sorter")] = "An algorithmic mystery"
library[("Algorithms", "Nora Recursia")] = "Let's get serious about algorithms"
library[("Time and Space", "Colin Plexity")] = "The entire universe... of algorithms"

print(library)
print(library[("Algorithms", "Ada Logic")])

# use ISBN to guarantee uniqueness

