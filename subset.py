
def subset_sum(arr, target):
    result = []

    def solve(i, current, total):
        if total == target:
            result.append(current[:])
            return

        if i == len(arr) or total > target:
            return

        # Include the current element
        current.append(arr[i])
        solve(i + 1, current, total + arr[i])
        current.pop()

        # Exclude the current element
        solve(i + 1, current, total)

    solve(0, [], 0)

    if result:
        for subset in result:
            print(subset)
    else:
        print("No subset found")


arr = [3, 4, 5, 2]
target = 7
subset_sum(arr, target)
print(92460118292)
