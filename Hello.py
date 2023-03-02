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
# name = name.strip()  #==> Removes Whitespace from str
# name = name.capitalize() #==> Capitalizes The firs word str
# name = name.title() #==> Capitalizes Every Word in str
name = name.strip().title() #==> Removes Whitespace from str and Capitalizes Every Word in str
print(f"Hello, {name}")

#split Users name into first name and last name
first_name, last_name = name.split(" ")
print(f"firstname : {first_name}, last name: {last_name}")
