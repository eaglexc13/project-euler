def selfPowers():
    ans = 0
    for x in range(1,1001,1):
        ans += x**x
    s_ans = str(ans)
    return s_ans[-10:]

print(selfPowers())
