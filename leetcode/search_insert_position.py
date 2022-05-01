def search(nums, target):
  size = len(nums)

  if target <= nums[0]:
    print("Add {} at index 0" .format(target))

  if (target > nums[size-1]):
    print("Add {} at index {}" .format(target, size))

  for i in range(size):
    if (i + 1 < size):
      if (nums[i] <= target <= nums[i+1]):
        print("Add {} at index {}" .format(target, i+1))

if __name__ == '__main__':
  int_list = []
  int_list = [int(item) for item in input("List: ").split()]
  num = int(input("Target: "))
  search(int_list, num)