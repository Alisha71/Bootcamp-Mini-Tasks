# Total number of lines in the pattern 
n = 9

# Loop for generating the pattern 
for i in range(1, n):
    if i <= 5: # First half of the pattern (increasing stars)
        print('*' * i)
    else:      # Second half of the pattern (decreasing stars)
    print('*' * (n-i))
        