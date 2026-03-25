test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21, "rita": 21, "Hari": 21, "Haritha": 21}

del test_dict["Mani"]
print(test_dict)
# del test_dict["Mani"]
# print(test_dict) --> Will raise exception

popped_value = test_dict.pop('Haritha')
print(popped_value) # Shows the value of the key which is popped.
print(test_dict)
