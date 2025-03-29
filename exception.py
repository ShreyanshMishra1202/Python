try:
    a,b=2,0
    print(a/b)
except ZeroDivisionError:
    print("There is ZeroDivisionError")
finally:
    print("Continue with the following code.")

# the finally part runs irrespective of whether try works or not