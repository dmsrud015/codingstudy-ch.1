n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

sorted_a = sorted(a_list, reverse=True)
sorted_b = sorted(b_list)

s = 0
for i in range(n):
    s += sorted_a[i] * sorted_b[i]

print(s)


#여기서 내가 느낀것은 문제는 풀수 있으나 코드화를 시키지 못한것이다.6번~7번째줄 보면 오름차순정렬 하고 내림차순 정렬을 서로 해주었다.
#11번째줄에서는 1~5번째열을 양쪽으로 곱해준거를 5번 반복해서 더해주었다.그래서 최종적으로 느낀것은 더쉬운걸 풀어야 겠다는 생각이들었다.
#이 문제역시 풀지 못했다.
