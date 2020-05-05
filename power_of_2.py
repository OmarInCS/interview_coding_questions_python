
def is_power(arr):
    result = []
    for n in arr:
        b = 1 if bin(n).count("1") == 1 else 0
        result.append(b)

    return result


in_count = eval(input())
arr = [eval(input()) for _ in range(in_count)]
result_arr = is_power(arr)
for n in result_arr:
    print(n)

