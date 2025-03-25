# ......................................... DATA STRUCTURES ...........................................

# there are in-buit data structures in python (list, dictionary, tuple, set) - they are considered non-primitive data structures

# .................mutability and immutability......................
# mutability - can be modified
# immutability - cannot be modified

# ................................ TUPLES .......................
# similar to list but is immutable
# uses () brackets
# data are accessed by indexing - indexes uses a square bracket

letters = ('a','b','d','y','z')
print(letters[0]) # accesses the first letter in the tuple
print(letters[0:]) # prints everyhing from index 0 to the last
print(letters[2:-1]) # prints upto th last index....reason for -1 is because the indexing format always excludes the last index






# .........................DICTIONARY.............................
# ordered colection of items
# stores elements in key value pairs
# key - unique identifier that are associated with each value
# e.g id number that uniquely idntifies you

capital_cities = {
    'KENYA': ['NAIROBI','MOMBASA','KISUMU','NAKURU'],
    'NIGERIA': 'ABUJA',
    'SOUTH AFRICA': 'JOHUNNESBURG'
}
print(capital_cities)
print(capital_cities['SOUTH AFRICA'])









# ...............................SETS..................................
# collection of unque data
# cannot store duplicted elements(cannot have same element repeated inside a set)
# incase {1,4,5,6,3,1} one of the '1' will be excluded on printing
# uses curly braces {}

account_names = {'PRAIZ','PHILIP','TERRY','LARRY','GLORIAN','GRACE','PRINCE'}
print(account_names)
print(account_names.pop()) # prints single items from the tuple randomly
