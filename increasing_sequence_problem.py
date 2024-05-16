# Test Script

list = [1,2,3,5,9]
prev = 0

for i in list:
    new_list = []
    if i > prev:
        new_list.append('Yes')
    else:
        new_list.append('No')
    prev = i

exists = 'No' not in new_list
print(exists)
