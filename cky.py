def cky(grammar, str):
    pass
 
def main():

    grammarsToAnalyze = int(input()) # Number of grammars to be analized

    for _ in range(grammarsToAnalyze):

        line = input() # Number of NT and number of strings to analyze
        numNT, numSTR = [int(i) for i in line.split()] # Line gets split in 2 variables: num of NT and num of STRs 
        grammar = {} # Dictionary for the grammar
       
        for _ in range (numNT):
            rule = input().split() # Input that contains the rule, split() divides it by spaces
            NTsymbol = rule[0] 
            productions = rule[1:] 
            grammar[NTsymbol] = productions # Grammar instantiation 
        
        for _  in range(numSTR):
            str = input() # String to analyze
            result = cky(grammar,str)

            if result == True: 
                print('yes')
            else:
                print('no')


