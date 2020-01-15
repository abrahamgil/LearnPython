#First app to test fundamentals. 
#Problem: Given the result provided in the GIF create the app. User continues inputs
#         until user ends with /end. After the sentences are formatted to for a 
#         clean output


def saysomething():
    i = 1
    final_statement = [0,1,2,3,4,5,6,7,8,9]
    while True:
        
        user_input = input("Say something: ")
        if user_input == "\end":
            break
        else:
            final_statement[i] = user_input
            print(final_statement[i])
            i = i + 1
            continue
        
        

        

def statementCleanUp(stuff):
    return stuff

saysomething()