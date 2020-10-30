T = int(input())
for t in range(1, T+1):
    K, N, M = map(int,input().split())
    # K 최대한 이동할 수 있는 정류장 수 
    # 0에서 N 번 정류장까지 이동 
    # M 충전기가 설치된 정류장 번호 
    # chargers = [0] * (N+1)
    charge_stops = list(map(int,input().split()))
    # for charge_stop in charge_stops:
    #     chargers[charge_stop] = 1
    
    # print(chargers)
    # 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력
    stops = [0] * (N+1) # 0부터 N 까지 정류장
    bus = 0 
    for 
    # print(stops)
