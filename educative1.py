def count_low_high(num_list):
  # Write your code here
  count_list = []
  count_high = 0
  count_low = 0
  
  for num in num_list:
    if num > 50 or num%3 == 0:
      count_high += 1
    else:
      count_low += 1
      
  count_list=[count_low,count_high]
  return count_list

num_list = [10,20,30,40,50,60,70,80,90,100]
print(count_low_high(num_list))