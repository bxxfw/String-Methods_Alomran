text = "   welcome to PYTHON programming 101!   "

print("Original text:", repr(text))

stripped = text.strip()
print("\n1) strip():", repr(stripped))

cap = stripped.capitalize()
print("2) capitalize():", repr(cap))

up = stripped.upper()
print("3) upper():", repr(up))

low = stripped.lower()
print("4) lower():", repr(low))

title = stripped.title()
print("5) title():", repr(title))

swap = stripped.swapcase()
print("6) swapcase():", repr(swap))

centered = stripped.center(50, '-')
print("7) center(50, '-'):", repr(centered))

count_o = stripped.count("o")
print("8) count('o'):", count_o)

replaced = stripped.replace("PYTHON", "Java")
print("9) replace('PYTHON','Java'):", repr(replaced))

split_list = stripped.split()
print("10) split():", split_list)

joined = "|".join(split_list)
print("11) join() with '|':", repr(joined))

print("\nBoolean tests on the stripped string:")
print("startswith('welcome'):", stripped.startswith("welcome"))
print("endswith('101!'):", stripped.endswith("101!"))
print("isalnum():", stripped.isalnum())
print("isalpha():", stripped.isalpha())
print("islower():", stripped.islower())
print("isupper():", stripped.isupper())
print("isspace():", stripped.isspace())

print("\nString comparisons:")
print('"cat" == "cat":', "cat" == "cat")
print('"cat" != "Cat":', "cat" != "Cat")
print('"cat" < "caterpillar":', "cat" < "caterpillar")
print('"dog" > "Dog":', "dog" > "Dog") 

print("\nComparisons between string and number:")
print('"10" == 10:', "10" == 10)
print('"10" != 10:', "10" != 10)
try:
    print('"10" > 10:', "10" > 10)
except TypeError as e:
    print('"10" > 10: TypeError ->', e)

words = ["dog", "cat", "zebra", "ant"]
print("\nSorting strings:")
print("Original list:", words)
sorted_list = sorted(words)
print("sorted(words) ->", sorted_list)
print("After sorted(), original list:", words)

words_copy = words.copy()
ret = words_copy.sort()
print("words_copy.sort() returned:", ret)
print("After words_copy.sort(), words_copy:", words_copy)
print("=> sorted() returns a new list; list.sort() sorts in-place and returns None.")

print("\nConverting between strings and numbers:")
num = 123
s_num = str(num)
print("str(123) ->", repr(s_num), "type:", type(s_num))

s = "456"
i = int(s)
print('int("456") ->', i, "type:", type(i))

s2 = "3.14"
f = float(s2)
print('float("3.14") ->', f, "type:", type(f))

try:
    bad = int("hello")
    print('int("hello") ->', bad)
except ValueError as e:
    print('int("hello") -> ValueError ->', e)