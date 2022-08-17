direction = [[1,0],[-1,0],[0,1],[0,-1]]
def solution(board, aloc, bloc):
    # A가 먼저 시작하기때문에
    # A가 단 한번이라도 이길 수 있으면, A는 무조건 이길 수 있는 플레이어임.
    # A에서 B를 호출해서 False일경우 최댓값. True일경우 최솟값을 가져오면 됨.
    # B입장도 같음. B에서도 A를 호출해서 False 일 경우 최댓값, True일경우 최솟값을 가져옴.
    # 그래서 A가 True가 하나라도 있으면, A의 최솟값 + B의 최댓값을 더해준것을 리턴
    # A가 True가 하나도 없다면, A의 최댓값 + B의 최솟값을 더해준것을 리턴해줌
    return(AMove(aloc[0],aloc[1],bloc[0],bloc[1],board,0))
    
    

def AMove(ay,ax,by,bx,board,cnt):
    rowN = len(board)
    colN = len(board[0])
    
    if board[ay][ax] == 0:
        return False, cnt
    
    
    board[ay][ax] = 0
    state = []
    dis = []
    for addY,addX in direction:
        Y = ay+addY
        X = ax+addX
        
        #범위 확인
        if (Y <0 or Y >= rowN or X <0 or X >= colN) or (board[Y][X] == 0):
            continue
        s,d = BMove(Y,X,by,bx,board,cnt+1)
        dis.append(d)
        state.append(s)

    board[ay][ax] = 1
    
    
    if False in state:
        return True, min(dis)
    else:
        return False, max(dis)
    

        
def BMove(ay,ax,by,bx,board,cnt):
    rowN = len(board)
    colN = len(board[0])
    
    if board[by][bx] == 0:
        return False,cnt

    board[by][bx] = 0
    state = []
    dis = []
    for addY,addX in direction:
        Y = by+addY
        X = bx+addX
        
        #범위 확인
        if (Y <0 or Y >= rowN or X <0 or X >= colN) or (board[Y][X] == 0):
            continue
        s,d = AMove(Y,X,by,bx,board,cnt+1)
        dis.append(d)
        state.append(s)
    board[by][bx] = 1

    
    if False in state:
        return True, min(dis)
    else:
        return False, max(dis)
            
        
    
    
    
            

a = solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]],[1,0],[1,2])
print(a)
    
    
