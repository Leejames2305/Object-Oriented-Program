## Practical 1 - Basics

# ===== 1.1 Comment =====
# x = 1 # This is a comment

# ===== 1.2 Data Types =====
# print(type(True))
# print(type(5))
# print(type(3.14))
# print(type("Hello"))

# ===== 1.2.1 Boolean =====
# if 2 > 1:
#     print("True")
# else:
#     print("False")

# ===== 1.2.2 Numbers =====
# x = 3
# x = x + 1

# r = 4
# print(r == x)

# c = 1.-3j
# print(c*c.conjugate())

# print(type(x))
# print(type(r))
# print(type(c))

# ===== 1.2.3 Strings =====
# t = "Hello everyone"
# print(t)
# print(t[0])
# print(t[2])
# print(t[-1])
# print(t[-3])

# text = '''This is a multi-
# line'''
# print(text)

# s = "12345678"
# print(s[:3])
# print(s[3:])
# print(s[2:5])
# print(s[::-1])
# print(s[::2])

# x = s
# # x = x + 1  # This will raise an error
# x = int(s)
# x = x + 1
# print(x)

# w = str(x+1)
# print(w)

# print(s + t + w)

# utarstring = ' u t a r '
# print(utarstring.find('a'))
# print(utarstring.strip())
# print(utarstring.replace(' ', ''))

# ===== 1.3 List =====
# listx = [1, 2, 3]
# print(listx[0])
# print(listx[1:2])
# print(listx[::-1])

# string = ' a, b, c, d '
# news = string.replace(' ', '').split(',')
# print(news)

# for e in string:
#     print(e)

# ==== 1.4 Keyboard Input =====
# userinput = input('Enter something: ')
# print('You entered:', userinput)

# ===== 1.5 String Formatting =====
# a = 'first'
# b = 'second'
# c = 'third'
# d = 'last'
# string = a + ' ' + b
# string = string + ' %s' %c
# string = string + ' {x}'.format(x=d)
# print(string)

# ===== 1.6 Files =====
# with open('Practical_1/A1_input.txt', 'r') as f:
#     data = f.read()
#     print(data)

# ===== 1.7 Debugging =====
''' This is the buggy code '''
'''
print 'This is the start' 
x = 0; y = 0 
x = 3.5 
y = 2*x-4j 
x += 1 
print 'x is', x 
print 'y is %d, y is %d ' %  y  
print 'This is the end'
'''

''' This is the fixed code '''
# print('This is the start')
# x, y = 0, 0
# x = 3.5
# y = 2*x - 4j
# x += 1
# print('x is', x)
# print('y real is %d, y imag is %d' % (y.real, y.imag))
# print('This is the end')

# ===== Excercise =====
with open('Practical_1/A1_input.txt', 'r') as f:
    data = f.readlines()

    # Extract bracketed contents
    results = []
    for line in data:
        line = line.strip()
        searchpos = 0
        while True:
            start = line.find('[', searchpos)
            if start == -1:
                break

            end = line.find(']', start)
            if end == -1:
                break

            contents = line[start+1:end]
            results.append(contents)
            searchpos = end + 1

    # Print results with contents per line
    print('Extracted contents:')
    for item in results:
        print(item)
    
    # Post-processing of contents
    # Take any number (int/str) and turn them into char; e.g. 12, 'y' -> OneTwo,y
    processed_results = []
    for item in results:
        output = ''
        for ch in item:
            if ch.isdigit():
                digit_map = {
                    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three',
                    '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
                    '8': 'Eight', '9': 'Nine'
                }
                output += digit_map[ch]
            else:
                output += ch
        processed_results.append(output)
    
    print('Processed contents:')
    for item in processed_results:
        item = item.replace(' ', '')
        item = item.replace("'", "")
        print(item)


# ===== EOF =====
input('Press Enter to continue...')