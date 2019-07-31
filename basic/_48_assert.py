__pname__    = 'assert'
__author__   = 'Md. Ashikun Nabi'
__email__    = 'ashikunnabituhin@gmail.com'

def avg(marks):
  assert len(marks) != 0, "List is empty."
  return sum(marks)/len(marks)

mark2 = [45, 65, 23]
print("Average of mark2:", avg(mark2))

mark1 = []
print("Average of mark1:", avg(mark1))