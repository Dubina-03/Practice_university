from factorial.factorials import *
from exp_root.root import *
from exp_root.exponentiation import *
from logarithm.logarithm import *


functions = [ln, lg, factorial, root2, root3, exp2, exp3]
def main():
    def result():
        print('This value is incorrect')
        results = main()
        return results


    function = input('Please, choose the function(log, ln, lg, factorial, root2, root3, exp2, exp3): ')
    x=0
    for func in functions:
        if func.__name__ == function:
            x+=1
    if x!=1:
        print('This function is not available')
        main()

    if function == 'exp2' or function == 'exp3' or function == 'root3':
        n=input('Enter the number ')
        try:
            g=float(n)
        except:
            results=result()
            return results
        n=float(n)
    elif function=='ln' or function=='lg' or function=='root2':
        n=input('Enter the number (the num>0) ')
        try:
            g=float(n)
            if 0>=g:
                results = result()
                return results
        except:
            results = result()
            return results
        n=float(n)
    elif function == 'factorial':
        n=input('Enter the number (the num is natural) ')
        try:
            g=int(n)
            if 0 > g:
                results = result()
                return results
        except:
            results = result()
            return results
        n=int(n)
    elif function == 'log':
        a = input('Enter the base of the logarithm (the num>0 and !=1) ')
        b = input('Enter the number (the num>0) ')
        try:
            g = float(a)
            f = float(b)
            if 0 >=g or 0>=f or f==1:
                results = result()
                return results
        except:
            results = result()
            return results
        a=float(a)
        b=float(b)

    if function!='log':
        for func in functions:
            if func.__name__==function:
                print('Your result is', func(n))
                return func(n)
    else:
        print('Your result is', log(a, b))
        return log(a, b)


if __name__ == '__main__':
    main()