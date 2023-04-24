"""
Implement a Python function collatz(n) that does the following. It takes a given integer 𝑛 and if
𝑛 is even, it divides 𝑛 by 2. Otherwise, it multiplies 𝑛 by 3 and adds one to it. Then, this number
is added to a list 𝑙. The new number is called 𝑛 and this procedure is repeated until 𝑛 is equal to 1.
At the end the function returns the list 𝑙.
"""

print('Enter a positive non-zero number')
n = int(input('n = '))
lstNumber = [n]

def collatz(n):
        if (n % 2 == 0):
            return n // 2
        elif (n % 2 == 1):
            return n * 3 + 1
        else:
            print('Error')
        
while (n != 1):
    n = collatz(n)
    lstNumber.append(n)

print(lstNumber)

"""
Krutarth Trivedi
2130962
"""