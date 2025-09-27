def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1+num2
        
    elif operation == 'subtract':
        return num1-num2
        
    elif operation == 'multiply':
        return num1*num2
        
    elif operation =='divide':
        try:
            answer = num1/num2
        except ZeroDivisionError as e:
            return e
        return answer
