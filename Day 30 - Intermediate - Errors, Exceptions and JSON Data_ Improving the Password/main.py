# try:
# 	file = open('a_file.txt')
# 	a_dictionary = {'key': 'value'}
# 	print(a_dictionary['no_key'])
# # except: # allows KeyError to pass
# except FileNotFoundError:  # passes only FileNotFoundError and not KeyError
# 	file = open('a_file.txt', 'w')
# 	file.write('something')
#
# # Stacking exceptions
# # except KeyError:
# # 	print("That key doesn't exist.")
#
# # Holding the error message
# except KeyError as error_message:
# 	print(f"The key {error_message} doesn't exist.")
#
# # Else (happens when there are no exceptions)
# else:
# 	content = file.read()
# 	print(content)

# Finally (runs no matter what)
# finally:
# 	file.close()
# 	print('File was closed')

# Raising my own errors

# finally:
# 	raise TypeError('This is a made up error.')

height = float(input('Height: '))
weight = int(input('Weight: '))
if height > 3:
	raise ValueError('Human height should not be over 3 meters')
bmi = weight / height ** 2
print(bmi)
