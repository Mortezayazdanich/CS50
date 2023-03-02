#1st Code "Hello World"
print("Hello, World!")

#2nd Code "Passing Variable to print()"
name = input("What's Your name? ")
print("Hello,", name)

#3rd Code "String Concatination"
print("Hello, " + name)

#4th Code "Named Parameters"
# Print doc ==> print(*objects, sep=' ', end='\n', file = sys.stdout, flush = False)
print("Hello,", end= ' ')
print(name)
# sep
print("Hello", name, sep="|||")

#5th Code "Formatted String"
print(f"Hello, {name}")
