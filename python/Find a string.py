def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        count += 1
        string = string[string.index(sub_string)+1 :]
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count