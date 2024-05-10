import random

people = {
    "Zhang san": 20,
    "Li si": 18,
    "Wang wu": 26
}

for person in people:
    print("name: {}, age: {}".format(person, people[person]))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i, num in enumerate(nums):
    newNum = nums[i] + 10
    nums[i] = newNum
print(nums)

for i in range(2, 10):
    print(i, ", ", random.randint(1, 10))
