def search(nums: int, key: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = int((start + end) / 2)
        if nums[mid] > key:
            end = mid - 1
        elif nums[mid] < key:
            start = mid + 1
        elif nums[mid] == key:
            print("Key found")
            return mid

    print("Key not found!")
    return 0


def main():
    print(search([10, 6, 4], 10))


main()
