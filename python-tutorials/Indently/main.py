a = [1, 2, 3]
b = a       # b is a pointer to whatever a is holding
b[2] = 100  # 3 is replaced by 100.  Index starts as 0, so
print(a)  # b = a is a pointer to whatever data a holds.  Answer is [1, 2, 100]
