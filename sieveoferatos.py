## Sieve of Eratosthenes
## Find prime numbers till the upper limit

primes = [1,2]
upper = int(input("Enter the upper limit: "))
nxtprime = 3
while nxtprime <= upper: 
    primeFound = True
    for n in primes[1:]: 
        remainder = nxtprime % n
        if remainder == 0: 
            primeFound = False
            break
    if primeFound == True:
        primes.append(nxtprime)
    nxtprime += 1
else:
    print("Prime numbers till {} are: {}".format(upper,primes))