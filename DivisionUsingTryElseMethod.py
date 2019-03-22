def smart_division():
    try:
        num1 = int(input('enter first number '))
        num2 = int(input('enter second number '))
        result = num1/num2
        print(result)
    except ZeroDivisionError:
        print('division by 0 is not possible')
    except:
        print('wrong input ' )
    else:
        print('no exceptions')
    finally:
        print('The end of program')
        
        
smart_division()
