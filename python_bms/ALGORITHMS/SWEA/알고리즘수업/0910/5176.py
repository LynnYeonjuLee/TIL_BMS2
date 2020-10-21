T = int(input())
def inorder(root):
    global idx
    if root <= N:
        inorder(root*2)
        TREE[root] = idx
        idx += 1
        inorder(root*2+1)

for tc in range(1,T+1):
    N = int(input())
    TREE = [0]*(N+1)
    idx = 1
    inorder(1)
    result1 = TREE[1] 
    result2 = TREE[N//2]
    print('#{} {} {}'.format(tc, result1, result2))