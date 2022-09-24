import sys
from sort_case import sort_case

def main():
    
    text = "HeLLo, World!"        
    upper_case, lower_case = sort_case(text)
    print(upper_case, lower_case)
        
if __name__ == "__main__":
    main()