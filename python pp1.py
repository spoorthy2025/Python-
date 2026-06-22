def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci sequence up to 6: {[fibonacci(i) for i in range(7)]}")

def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(f"Sum of [1, 2, 3, 4, 5]: {list_sum([1, 2, 3, 4, 5])}")

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

print(f"Is 'madam' a palindrome? {is_palindrome('madam')}")
print(f"Is 'A man, a plan, a canal: Panama' a palindrome? {is_palindrome('A man, a plan, a canal: Panama')}")
print(f"Is 'hello' a palindrome? {is_palindrome('hello')}")

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

print("\nTower of Hanoi (3 disks):")
tower_of_hanoi(3, 'A', 'B', 'C')