if __name__ == '__main__':
    s = input()
    alphanumeric = False
    alphabetical = False
    digits = False
    lowercase = False
    uppercase = False
    for i in s:
        if not alphanumeric and i.isalnum():
            alphanumeric = True
        if not alphabetical and i.isalpha():
            alphabetical = True
        if not digits and i.isdigit():
            digits = True
        if not lowercase and i.islower():
            lowercase = True
        if not uppercase and i.isupper():
            uppercase = True
    
    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)
        
    