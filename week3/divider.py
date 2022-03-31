import os
import time

def divider():
  print("Select a different part of the menu.")

def balloon():
  distance_from_top = 10
  while distance_from_top > 0:
    print("\n" * distance_from_top)
    print("   _..._  ,s$$$s.")
    print(" .$$$$$$$s$$ss$$$$,")
    print(" $$$sss$$$$s$$$$$$$")
    print(" $$ss$$$$$$$$$$$$$$")
    print(" '$$$s$$$$$$$$$$$$'")
    print("  '$$$$$$$$$$$$$$'")
    print("    S$$$$$$$$$$$'")
    print("     '$$$$$$$$$'")
    print("       '$$$$$'")
    print("        '$$$'")
    print("          ;")
    print("         ;")
    print("         ;")
    print("         ',")
    print("          ;")
    print("         ,'")
    time.sleep(0.2)
    os.system('clear')  
    distance_from_top -= 1

def animation():
  balloon()
  divider()
