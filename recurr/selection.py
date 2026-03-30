# Open the file in write and read mode ('w+')
file = open('cscproj.txt', 'w+')

# Write "Hello World," to the file
file.write('Hello World,')

# Seek back to the beginning of the file to read
file.seek(0)

# Read the content back
content = file.read()

# Print the read content
print(content)

# Explicitly close the file
file.close()




# def selection(arr):
#     for i in range(len(arr)):
#         minIdx=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[minIdx]:
#                 minIdx=j
#         [arr[i],arr[minIdx]]=[arr[minIdx],arr[i]]
#     return arr
# print(selection([6,5,7,3,9,55,1]))