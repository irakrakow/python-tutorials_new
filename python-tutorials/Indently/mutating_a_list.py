# initial list
a = [1, 2, 3]

b = a       # b is a pointer to whatever a is holding

b[2] = 100  # 3 is replaced by 100.  Index starts as 0, so
 
# Answer is [1, 2, 100]
print(a)
