text = "   welcome to PYTHON programming 101!   "

print(text.strip())
print(text.strip().capitalize())
print(text.strip().upper())
print(text.strip().lower())
print(text.strip().title())
print(text.strip().swapcase())
print(text.strip().center(50, '-'))
print(text.strip().count("o"))
print(text.strip().replace("PYTHON", "Java"))
words = text.strip().split()
print(words)
print("|".join(words))

print(text.strip().startswith("welcome"))
print(text.strip().endswith("101!"))
print(text.strip().isalnum())
print(text.strip().isalpha())
print(text.strip().islower())
print(text.strip().isupper())
print(text.strip().isspace())

print("cat" == "cat")
print("cat" != "Cat")
print("cat" < "caterpillar")
print("dog" > "Dog")
print("10" == 10)
print("10" != 10)

animals = ["dog", "cat", "zebra", "ant"]
print(sorted(animals))
animals.sort()
print(animals)

num = 123
print(str(num))
s = "456"
print(int(s))
f = "78.9"
print(float(f))
