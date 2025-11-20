
##### Template for Chapter 5.14, Exercises 1 - 4 ######


# print("********** Ch 6 Exercise 1 **********")

def b(z):
    print(f"b z={z}")
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    print(f"a x={x} y={y}")
    x = x + 1
    return x * y

def c(x, y, z):
    print(f"c x={x} y={y} z={z}")
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))



# print("********** Ch 6 Exercise 2 **********")


def acc(m,n):
    if m == 0:
        return n+1
    
    elif m>0 and n==0:
        return acc(m-1, 1)

    elif m>0 and n>0:
        return acc(m-1, acc(m,n-1))

m=2
n=3
result = acc(m,n)
print(f"acc({m},{n}) = {result}")

# print("********** Ch 6 Exercise 3 **********")

# Exercise 3 should be worked in a new file called palindrome.py



# print("********** Ch 6 Exercise 4 **********")

# Do your work for Exercise 4 here.

# print("Ch 6 Exercise 4: Not implemented") # Delete this line when you write your code!



# print("********** Ch 6 Exercise 5 **********")

# Do your work for Exercise 5 here.







