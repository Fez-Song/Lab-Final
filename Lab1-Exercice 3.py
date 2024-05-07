phonebook = {
    "John": "18712936268",
    "Fez": "17627796683",
    "Jack": "15900328682",
}


def lookup_number(name):
    return phonebook[name]


name = input("Enter a name(John, Fez, Jack): ")
print(lookup_number(name))