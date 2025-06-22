def compute_squares(nums:list[int]):
    square =[]
    for n in nums:
        square.append(n*n)
    return square

print(compute_squares([1,2,3]))
print(compute_squares([4,5,6]))