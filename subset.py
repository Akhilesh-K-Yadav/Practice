def find_subsets(nums):
    subs = []
    subs.append([])
    print(subs)
    for num in nums:
        length = len(subs)
        for i in range(length):
            
            new_sub = subs[i].copy()
            new_sub.append(num)
            print(new_sub)
            subs.append(new_sub)
            print(subs)
    print(subs)

def main():
    find_subsets([1,5,3])

main()
