def super_fibonacci(n, m):
    nums = [1 for a in range(0,m)]
    if n > m:
        for a in range(m, n):
            sum_prev = 0
            for b in range(a-m,a):
                sum_prev += nums[b]
            nums.append(sum_prev)

    return nums[n-1]

print super_fibonacci(2, 1)