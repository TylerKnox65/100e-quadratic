#!python3
'''
This is a challenging problem!

x06. Determine the factored form
You may use the functions you created in previous assignments
'''
import math
def Factored(a,b,c):
  '''
  input parameters:
  a, b, c: signed float
  These are the coefficients in the quadratic function ax^2 + bx + c = 0
  
  Write the equation in a nicely formatted factored form. This means no fractions
  
  return:
  list : 2 string literals representing the factors.  The order does not matter
  None if the quadratic can not be factored

  '''
  nlist = []
  num = b**2-(4*a*c)
  
  if num >= 0:
    if a == 1:
      factored_pos  = ((-1 * b) + math.sqrt((b ** 2) - (4 * a * c))) / (2*a)
      factored_neg = ((-1 * b) - math.sqrt((b ** 2) - (4 * a * c))) / (2*a)
      if factored_pos > 0:
        nlist.append(f"(x - {int(factored_pos)})")
      elif factored_pos < 0:
        nlist.append(f"(x + {int(-1 * factored_pos)})")
      if factored_neg > 0:
        nlist.append(f"(x - {int(factored_neg)})")
      elif factored_neg < 0:
        nlist.append(f"(x + {int(-1 * factored_neg)})")
      return nlist
    else:
      b = b/a
      c = c/a
      a = 1
      factored_pos  = ((-1 * b) + math.sqrt((b ** 2) - (4 * a * c))) / (2*a)
      factored_neg = ((-1 * b) - math.sqrt((b ** 2) - (4 * a * c))) / (2*a)
      ax = (factored_pos).as_integer_ratio()
      Bx = ax(1)
      cx = ax(0)
      ax_n = (factored_neg).as_integer_ratio
      if factored_pos > 0:
        nlist.append(f"({Bx}x - {cx})")
      elif factored_pos < 0:
        nlist.append(f"({Bx}x + {-1 * cx})")
      if factored_neg > 0:
        nlist.append(f"{Bx}x - {cx}")
      elif factored_neg < 0:
        nlist.append(f"{Bx}x + {cx}")
      
      return nlist

    

  else:
    return None
  

def main():
  assert "(x + 3)" in Factored(1,1,-6) == True
  assert "(x - 2)" in Factored(1,1,-6) == True
  assert "(x + 2)" in Factored(1,7,10) == True
  assert "(2x + 1)" in Factored(2,5,2) == True
  assert "(x + 2)" in Factored(2,5,2) == True
  assert "(3x + 1)" in Factored(6,-7,-3) == True
  assert Factored(1,4,7) == None
  assert Factored(2,4,4) == None
  
if __name__ == "__main__":
  main()
  
