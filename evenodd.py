## Examples for Python List comprehension

limit = int(input("Enter the upper limit: ")) + 1
evens = [n for n in range(1, limit) if n%2 == 0]
odds = [n for n in range(1, limit) if n%2 == 1]
print("Even numbers till {} are: {}".format((limit-1),evens))
print("Odd numbers till {} are: {}".format((limit-1),odds))