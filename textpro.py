#First app to test fundamentals. 
#Problem: Given the result provided in the GIF create the app. User continues inputs
#         until user ends with /end. After the sentences are formatted to for a 
#         clean output

""" My Original Attempt
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
    for i in stuff:
        print(i)
        isupper.i()
        print(i)

    return stuff

print(saysomething())

"""
def sentence_maker(phrase):
    interrogatives = ("how", "what", "why", "when", "where", "do")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)



results = []
while True:
    user_input = input("Saw something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))