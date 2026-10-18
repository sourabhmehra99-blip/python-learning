def sum_num(num):
    return sum(num)

def higher_order_functon(f,lst):
    ans = f(lst)
    return ans

result = higher_order_functon(sum_num, [1, 2, 3, 4, 5])
print(result)