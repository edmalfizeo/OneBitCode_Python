def uppercase_e_lowercase(string):
    uppercase = 0
    lowercase = 0
    for i in string:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
    return uppercase, lowercase


print(uppercase_e_lowercase("Teste do DUDU"))
