test_string = "My name is Seongjae Moon."
print(test_string.split()) # ['My', 'name', 'is', 'Seongjae', 'Moon.']

for i in test_string.split():
    print(i, end = ' ') # My name is Seongjae Moon.

replace = test_string.replace('Seongjae Moon.', 'Super Moon!')
for i in replace:
    print(i, end = '') # My name is Super Moon! 