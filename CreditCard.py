cc = '1337-1767-4239-4862'
 #defining the functions 
def hideccno(ccno):
    strng = '' #empty string
    if len(cc) > 4:
        strng += '*' *(len(cc) - 4)+cc[-4:] #here we are slicing the strings to just blur the first digits
    else:
        return cc
    return strng
print(hideccno(cc))
