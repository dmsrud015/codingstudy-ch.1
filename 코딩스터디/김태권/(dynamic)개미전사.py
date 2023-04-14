n = int(input())
arr = list(map(int,input().split()))

d=[0]*100
d[0]=arr[0]
d[1]=max(arr[0],arr[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+arr[i])

print(d[n-1])

#여기서 내가 깨달은 건지 아닌지 모르겠지만 왜 8이 나오는냐! 
#그것은 arr[i]열을 for문에서 2~3까지 반복한다는 가정하에 
#arr[2],arr[3]을 더해주면 8이된다.그러나 여기서 d에서는 덧셈을 하지않는 것으로 가정을 
