# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "GroupName": "Tomorrow X Together",   
               "DebutDate": "March 4, 2019",   
               "Members":["Yeonjun","Soobin","Beomgyu ","Taehyun ","Huening Kai"]  
              }) 

InfoDb.append({  
               "GroupName": "Blackpink",   
               "DebutDate": "August 8, 2016",   
               "Members":["Lisa","Jennie","Rose ","Jisoo "]  
              }) 

# Database used for looping functions
InfoDbLoop = []

InfoDbLoop.append({  
               "GroupName": "Tomorrow X Together",   
               "DebutDate": "March 4, 2019",   
               "Members":["Yeonjun","Soobin","Beomgyu ","Taehyun ","Huening Kai"]  
              }) 

InfoDbLoop.append({  
               "GroupName": "Blackpink",   
               "DebutDate": "August 8, 2016",   
               "Members":["Lisa","Jennie","Rose ","Jisoo "]  
              }) 

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDbLoop[n]["GroupName"]) 
    print("\t", "DebutDate: ", end="") 
    print(InfoDbLoop[n]["DebutDate"]) 
# using comma puts space between values
    print("\t", "Members: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDbLoop[n]["Members"]))  # join allows printing a string list with separator
    print()

def for_loop():
  for n in range(len(InfoDbLoop)):
    print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
  while n < len(InfoDbLoop):
      print_data(n)
      n += 1
  return

def recursive_loop(n):
  if n < len(InfoDbLoop):
      print_data(n)
      recursive_loop(n + 1)
  return # exit condition

def __init__(self, n):
  self.n = n

def databases():
  print("Printing the for loop")
  print(" ")
  for_loop()
  print("Printing while_loop")
  print(" ")
  while_loop(0)
  print("Printing recursive_loop")
  print(" ")
  recursive_loop(0)
