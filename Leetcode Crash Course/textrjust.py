def justify(width, s):
    def rjust(string, int, fillchar=' '):
        if len(string) >= width:
            return string
        padding_required = width - len(string)
  
        return fillchar * padding_required + string
        
    currentLine = []    
    line_length = 0
    words = s.split()
    justified_text = []

    for word in words:
        if len(word) + len(currentLine) + line_length > width:
            justified_text.append(' '.join(currentLine).rjust(width))
            currentLine = []
            line_length = 0

        currentLine.append(word)
        line_length += len(word)

    if currentLine:
        justified_text.append(' '.join(currentLine).rjust(width))
   
    return '\n'.join(justified_text)

# Write tests
paragraph = "Write a function that takes in the parameters width, and a string that would right justify a given paragraph."
width = 10
result = justify(width, paragraph)
print(result)