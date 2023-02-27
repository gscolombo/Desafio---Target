known_num = {
    0: 0,
    1: 1
}

def fibonacci(n):
    if n in known_num:
        return known_num[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known_num[n] = res
    return res

def checkFibonacci(n):
    k = 0
    while fibonacci(k) <= n:
        res = fibonacci(k)
        if res == n:
            print(f"{n} belongs to Fibonacci's sequence.")
            return
        k += 1
    print(f"{n} does not belongs to Fibonacci's sequence.")


print("Function to check if a given number belongs to Fibonacci's sequence. \nBelow is the test for numbers in the interval [0, 200):")
for n in range(200):
    checkFibonacci(n)

print("\n Custom test: (accept only integers inputs)")
print("(Give an empty input to exit the program)")
while True:
    n = input()
    if n == "":
        break
    checkFibonacci(int(n))
    
