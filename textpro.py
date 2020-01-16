#First app to test fundamentals. 
#Problem: Given the result provided in the GIF create the app. User continues inputs
#         until user ends with /end. After the sentences are formatted to for a 
#         clean output


def saysomething():
    i = 0
    final_statement = [None]*100
    while True:
        
        user_input = input("Say something: ")
        if user_input == "\end":
            statementCleanUp(final_statement)
            return final_statement
            break
        else:
            final_statement[i] = user_input
            print(final_statement[i])
            i = i + 1
            continue
        
        
      

def statementCleanUp(stuff):
    
    return stuff

print(saysomething())