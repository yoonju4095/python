# 문자열 만들기

name = "Kildong"
dept = "IT"

# str concatenation(+)
print("I am " + name + ". I belong to " + dept + " department.")

# %-formatting (%)
print("I am %s. I belong to %s department." %(name,dept))

# str.format()
print("I am {}. I belong to {} department.".format(name,dept))

# f-strings
print(f"I am {name}. I belong to {dept} department.")