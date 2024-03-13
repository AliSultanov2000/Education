# Дан массив интервалов intervals, где intervals[i] = [starti, endi], верните минимальное количество интервалов, которые вам нужно удалить, чтобы остальные интервалы не перекрывались.

# LeetCode Medium level

def erase_overlapping_intervals(intervals: list) -> int:
    ans = 0
    intervals.sort()

    prev_end = float('-inf')
    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            ans += 1
            prev_end = min(end, prev_end)
        
    return ans


print(erase_overlapping_intervals([(1, 2), (1, 4), (2, 3)]))
