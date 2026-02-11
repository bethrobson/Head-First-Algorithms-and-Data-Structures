
def find_file(folder, target):
    for name, contents in folder.items():
        for item in contents:
            if item == target:
                return name
            elif isinstance(item, dict):
                found = find_file(item, target)
                if found:
                    return found
    return False

# folder structure
filesystem = {
    "home": [
        "notes.txt",
        {"photos": ["vacation.jpg", "birthday.png"]},
        {"docs": ["resume.pdf", {"projects": ["report.docx", "target.txt"]}]}
    ]
}

print(find_file(filesystem, "target.txt"))   # "projects"
print(find_file(filesystem, "vacation.jpg")) # "photos"
print(find_file(filesystem, "notes.txt"))    # "home"
print(find_file(filesystem, "not_here.txt")) # False




