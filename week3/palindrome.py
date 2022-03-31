phrase = ["race car", "bazinga", "Rat, Dad, Tar"] # phrases and words being tested
specialchars = "!@#$%^&*()~`<>,./?':;}{][\| "
inverse = ""
# all special characters - !@#$%^&*()`~-_+=[{]}\|;:"',<.>/?'"]
def palindrome():
  for phrases in phrase:
    print("Original Phrase:", phrases)
    
    for chars in specialchars:
      phrases = phrases.replace(chars, "") # replaces special characters and spaces
      phrases = phrases.lower() # makes everything lowercase
      inverse = phrases[::-1] # reverses word
    print("New Phrase:", inverse)  
    
    if (phrases == inverse):
      print("Wow! That's a palindrome!")
      print(" ")
    else:
      print("Unfortunately, that is not a palindrome.")
      print(" ")
