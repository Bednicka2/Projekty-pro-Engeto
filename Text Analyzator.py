TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# proměnné
separator = "-" * 40
username_password = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# přihlášení
username = input("username: ")
password = input("password: ")
print(separator)

if username in username_password:
    if password == username_password.get(username):
        print(f"Welcome to the app, {username}. \nWe have 3 texts to be analyzed. \n{separator}")
    else:
        print("Wrong password!")
        quit()
else:
    print("Wrong username!")
    quit()

# Výběr textu na analýzu
choice = input("Enter a number btw. 1 and 3 to select: ")
if choice.isnumeric():
    if choice in ["1", "2", "3"]:
        print(separator)
    else:
        print("Input is out of range!")
        quit()
else:
    print("Input is not a number")
    quit()

# Analýza textu

text = TEXTS[int(choice) - 1].split()
words = []
titlecase, uppercase, lowercase, numeric = [], [], [], []
for word in text:
    words.append(word.strip("!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"))
words = list(filter(None, words))

for word in words:
    if word.istitle():
        titlecase.append(word)
    elif word.isupper():
        uppercase.append(word)
    elif word.islower():
        lowercase.append(word)
    elif word.isnumeric():
        numeric.append(word)

numeric = [int(num) for num in numeric]
suma = sum(numeric)

print(f"""There are {len(words)} words in the selected text.
There are {len(titlecase)} titlecase words.
There are {len(uppercase)} uppercase words.
There are {len(lowercase)} lowercase words.
There are {len(numeric)} numeric strings.
The sum of all the numbers is {suma}.""")

print(separator)
print("LEN | OCCURENCES | NR.")
print(separator)

dic = {}
a = []

for word in words:
    a.append(len(word))

for lengh in a:
    if lengh not in dic:
        dic[lengh] = 1
    else:
        dic[lengh] += 1

max_lengh = max(dic.get(b) for b in dic)
max_number = max(len(str(b)) for b in dic)
for b in sorted(dic):
    x = "*" * dic.get(b)
    print(f"{' ' * (max_number - len(str(b)))}{b}|{x} {' ' * (max_lengh - len(str(x)))}|{dic.get(b)}")
