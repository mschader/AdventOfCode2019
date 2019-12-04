#!/usr/bin/env python

def is_pattern(i):
    istr = str(i)
    result = False
    final_result = False
    previous = ""
    for num in istr:
        if previous == num:
            result = True
            if previous == previousprevious:
                result = False
        elif result:
            final_result = True
        if previous > num:
            return False
        previousprevious = previous
        previous = num
    return (result or final_result)

counter = 0

for i in range(235741,706948):
    if is_pattern(i):
        counter += 1

print(counter)