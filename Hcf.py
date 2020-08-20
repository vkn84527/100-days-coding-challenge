# Python program to find HCF of two 
#// numbers iteratively. 
def hcf(a, b):
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a 
    return a 
	
a = 60
b = 96
print(hcf(a, b)) 
