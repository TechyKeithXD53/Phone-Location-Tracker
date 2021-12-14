txt = "This Is The Link Of {}, Here The Link: {}"
txtlist = ["https://www.w3schools.com/python/"]
txtfake = ("https://www.w3schools.com/python/python_strings_methods.asp",
           "https://www.w3schools.com/python/python_casting.asp", "https://www.w3schools.com/python/python_variables.asp", "https://www.w3schools.com/python/python_numbers.asp")
txtlist.extend(txtfake)
afake = "String Methods"
bfake = "https://www.w3schools.com/python/python_strings_methods.asp"
a2fake = "Python Casting"
b2fake = "https://www.w3schools.com/python/python_casting.asp"
a3fake = "Python Variables"
b3fake = "https://www.w3schools.com/python/python_variables.asp"
a4fake = "Python Numbers"
b4fake = "https://www.w3schools.com/python/python_numbers.asp"
print(txt.format(afake, bfake))
print(txt.format(a2fake, b2fake))
print(txt.format(a3fake, b3fake))
print(txt.format(a4fake, b4fake))
print(txtlist)