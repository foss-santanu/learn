def fibonacci(till=10): 
    fibos = [1, 1]
    while True: 
        nxtFibo = fibos[-1] + fibos[-2]
        if nxtFibo <= till: 
            fibos.append(nxtFibo)
        else:
            break
    return fibos

print(f"Fibonacci sequence till 1 is: {fibonacci(1)}")
print(f"Fibonacci sequence till 2 is: {fibonacci(2)}")
print(f"Fibonacci sequence till 10 is: {fibonacci()}")
print(f"Fibonacci sequence till 8 is: {fibonacci(8)}")
print(f"Fibonacci sequence till 26 is: {fibonacci(26)}")