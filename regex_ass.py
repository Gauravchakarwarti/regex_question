#1.) Regex Query Tool - A tool that allows the user to enter a text string and then in a separate control enter a regex pattern. 
#It will run the regular expression against the source text and return any matches or flag errors in the regular expression.


import re

def regex_query_tool():
    print("Regex Query Tool")
    print("----------------")
    
    # Get user input for text string and regex pattern
    text = input("Enter the text string: ")
    pattern = input("Enter the regex pattern: ")
    
    try:
        # Compile the regex pattern
        compiled_pattern = re.compile(pattern)
        
        # Search for matches in the text
        matches = compiled_pattern.findall(text)
        
        if matches:
            print("\nMatches found:")
            for match in matches:
                print(match)
        else:
            print("\nNo matches found.")
            
    except re.error:
        print("\nInvalid regex pattern. Please check the pattern syntax.")

if __name__ == "__main__":
    regex_query_tool()
