
name = "abhi-coder"

#🔤 Case Conversion
print(name.lower())       # 'abhi-coder '
print(name.upper())       # 'ABHI-CODER '
print(name.title())       # 'Abhi-Coder '
print(name.capitalize())  # 'Abhi-coder '
print(name.swapcase())    # 'ABHI-CODER '



#🧹 Whitespace and Padding

print(name.strip())       # 'abhi-coder'         ← Removes trailing space
print(name.lstrip())      # 'abhi-coder '        ← (no change here)
print(name.rstrip())      # 'abhi-coder'         ← Removes trailing space
print(name.zfill(15))     # '000abhi-coder '     ← Pads with zeros
print(name.center(20))    # '    abhi-coder     '← Centers in 20-width


#🔍 Searching & Checking

print(name.find('coder'))      # 5
print(name.rfind('c'))         # 5
print(name.startswith('abhi')) # True
print(name.endswith(' '))      # True
print('hi' in name)            # True
print(name.index('b'))         # 1


#🔧 Modification and Formatting

print(name.replace('-', ' '))     # 'abhi coder '
print(name.split('-'))            # ['abhi', 'coder ']
print('_'.join(name.split('-')))  # 'abhi_coder '
print("Hello, {}".format(name))   # 'Hello, abhi-coder '
print(name.count('a'))            # 1



#🧪 Character Type Checks



print(name.isalpha())     # False (contains '-' and space)
print(name.isdigit())     # False
print(name.isalnum())     # False (contains '-' and space)
print(name.isspace())     # False
print(name.islower())     # True
print(name.isupper())     # False
print(name.istitle())     # False