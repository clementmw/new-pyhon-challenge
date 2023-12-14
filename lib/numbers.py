def true_or_false (a,b,c):
   # Check if at least two of the three variables are positive
    # (a and b) or (a and c) or (b and c)
    
   if (a > 0 and b > 0) or (a > 0 and c > 0) or (b > 0 and c > 0):
      return True
   else:
      return False

print(true_or_false(1,-2,3))

