num1 = 0.0
num2 = 0.0
operation = ''

def perform_operation(num1,num2,operation):
    match operation:
        case 'add':
            return num1+num2
        
        case 'subtract':
            return num1-num2
        
        case 'multiply':
            return num1*num2
        
        case 'divide':
            try:
                answer = num1/num2
            except ZeroDivisionError as e:
                return e
            return answer
