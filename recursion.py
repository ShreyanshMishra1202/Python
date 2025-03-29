# RECURSION
'''
def python():
    print("Python")
    python()
python()
'''
import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
n=0
def python():
    global n        # global help us to change outer variable from inner variable
                    # without global, outer will apply in inner, but change inner will not change outer
    n+=1
    print("Python",n)
    python()
python()