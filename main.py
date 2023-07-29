def two_sum(nums, target):
    for i in range(len(nums) - 1):
        wanted = target - nums[i]
        for j in range(i + 1, len(nums)):
            print(len(nums))
            if nums[j] == wanted:
                return [i, j]


def twoSum(nums, target):
    seen_nums = {}

    for i in range(len(nums) - 1):
        wanted_match = target - nums[i]

        if wanted_match in seen_nums:
            return[seen_nums[wanted_match], i]

        else:
            seen_nums[nums[i]] = i

    print(seen_nums)
    return []


def main():
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSum(nums, target))


main()
