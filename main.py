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

def fizz_buzz():
    for i in range(1, 100):
        if i % 3 == 0:
            print('fizz')

        if i % 5 == 0:
            print('Buzz')

        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')

        else:
            print(i)

def main():
    fizz_buzz()


main()
