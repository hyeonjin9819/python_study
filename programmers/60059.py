def solution(s):
    num = len(s)//2
    real = []
    for i in range(1, num+1):
        ans = []
        list_chunked = list_chunk(s, i)
        if has_duplicates(list_chunked):
            first = list_chunked[0]
            cnt = 0
            for j in list_chunked:
                if first == j:
                    cnt += 1
                else:
                    if cnt != 1:
                        ans.append(str(cnt))
                    ans.append(first)
                    first = j
                    cnt = 1
            if cnt != 1:
                ans.append(str(cnt))
            ans.append(first)
            #print(list_chunked)
            result = "".join(ans)
            #print(ans)
            real.append(len(result))
    if len(real) >0:
        return min(real)
    else:
        return len(s)

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def has_duplicates(seq):
    return len(seq) != len(set(seq))