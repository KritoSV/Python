# -> range(start=0, stop, step=1)
range(5) # -> range(start=0, 5, step=1) -> 0,1,2,3,4
range(2, 10) # -> range(2, 10, step=1) -> 2,3,4,5,6,7,8,9
range(2, 10, 2) # -> range(2, 10, 2) -> 2,4,6,8 
range(10, 2, -2) # -> range(10, 2, -2) -> 10,8,6,4
word = 'Python'
# len(word)= 6
range(len(word) -1, -1, -1) # -> range(6-1=5, -1, -1) -> 5,4,3,2,1,0 
range(-1, -1, -1) # -> range(-1, -1, -1) -> 5,4,3,2,1,0 
for i in range(len(word) -1, -1, -1):
    print(word[i], end='')