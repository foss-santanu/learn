## Fibonacci sequence generator
def fiboNumbers(): 
    x, y = 0, 1
    while True:
        yield x 
        z = x
        x += y 
        y = z 
    
## Function to return a list of Fibonacci numbers of a given size
def fibonaccis(iterCount=1):
    fibos = []
    for nxtFibo in fiboNumbers(): 
        fibos.append(nxtFibo)
        iterCount -= 1
        if iterCount == 0: 
            break          
    return fibos

print(f"Fibonacci sequence with one member: {fibonaccis()}")
print(f"Fibonacci sequence with two members: {fibonaccis(2)}")
print(f"Fibonacci sequence with three members: {fibonaccis(3)}")
print(f"Fibonacci sequence with 8 members: {fibonaccis(8)}")
print(f"Fibonacci sequence with 26 members: {fibonaccis(26)}")