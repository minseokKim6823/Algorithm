def solution(arr, queries):
    temp=0
    for i in range(len(queries)):
        fir=queries[i][0]
        sec=queries[i][1]
        temp=arr[fir]
        arr[fir]=arr[sec]
        arr[sec]=temp
    answer = arr
    return answer