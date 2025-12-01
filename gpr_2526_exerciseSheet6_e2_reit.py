def ackermann_function(n,m):
    if n == 0:
        return m+1
    elif m == 0 & n != 0:
        return ackermann_function(n-1,1)
    else:
        return ackermann_function(n-1, ackermann_function(n, m-1))

def rewrite_recursive_funktion(n):

    # Recursiv fuction looks like: f(n) = --- 1                 n<=1
    #                                     --- f(n-1) + f(n-3)   otherwise

    if n <= 1:
        return 1

    f = [0] * (n+1) # Index beginnt with 0, so we need n+1 places to store the result of n

    f[0] = 1
    f[1] = 1
    f[2] = 2 #  f(n−1) + f(n−3) otherwise, so we have f[2] = f[1]+f[-1] = 1+1 = 2

    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-3]
    return f[n]


if __name__ == "__main__":
    print(ackermann_function(0,1))
    print(rewrite_recursive_funktion(6))