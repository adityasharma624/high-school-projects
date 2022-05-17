def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    print("Partial",partial)
    if s == target: 
        print(partial,"=",target)
    if s >= target:
        return
    for i in range(len(numbers)):
        n = numbers[i]
        print("Numero",n)
        remaining = numbers[i+1:]
        print("Remaining",remaining)
        subset_sum(remaining, target, partial + [n]) 
   

subset_sum([3,9,8,4,5,7,10],15)
