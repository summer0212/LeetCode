from stack import Stack

def convert_int_to_bin(dec_num):
  s = Stack()
  
  while dec_num != 0:
    dig = dec_num % 2
    dec_num = dec_num // 2
    s.push(dig)
    
  bin_num = ""
  
  while not s.is_empty():
    bin_num += str(s.pop())
  
  return bin_num