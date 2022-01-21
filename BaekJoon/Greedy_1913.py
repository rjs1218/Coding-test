'''
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
'''

room = []

n = int(input())
for i in range(n):
    room.append([])
    time = list(map(int, input().split()))  # 회의 시간을 입력받아 넣어준다.
    room[i] = time

room.sort() # 오름차순 정렬
print(room)

# 회의실을 사용하려면 조건을 갖추어야한다.
# 조건1. 회의 시작시간이 현재 회의 종료시간보다 크거나 같아야 된다.
# 조건2. 조건1을 충족한 회의들 중 종료시간이 제일 빨라야 된다.

# 변수
# 현재 회의 -> now
# 제일 빠른 종료 시간 -> fastEnd

# 천천히 다시하자
