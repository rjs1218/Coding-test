'''
영일이는 생명과학에 관심이 생겨 왕개미를 연구하고 있었다.

왕개미를 유심히 살펴보던 중 특별히 성실해 보이는 개미가 있었는데,
그 개미는 개미굴에서 나와 먹이까지 가장 빠른 길로 이동하는 것이었다.

개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.

미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
'''

box = []

# 10 * 10 크기의 미로 상자 만들기
for i in range(11):
    box.append([])
    for j in range(11):
        box[i].append(0)

# 10 * 10 크기의 미로 상자 입력하기
for i in range(10):
    inputBox = list(map(int, input().split()))
    for j in range(10):
        box[i+1][j+1] = inputBox[j]

# 먹이 위치 찾기
foodX, foodY = 0, 0
for i in range(2, 10):
        for j in range(2, 10):
             if box[i][j] == 2:
                 foodX, foodY = i, j

# 개미 출동!
x, y = 2, 2
while True:                 # 벽이라면 1, 아니라면 0
    if box[x][y] == 0:      # 벽이 아니면 가기
        box[x][y] = 9
        y += 1

    elif box[x][y] == 2:    # 먹이를 찾으면 STOP
        box[x][y] = 9
        break

    else:                   # 벽을 만났다면 한 칸 되돌아오고 아래로
        x += 1
        y -= 1
        if box[x][y] == 1:  # 내려갔는데도 벽이면 STOP
            break

# 개미가 지나간 10 * 10 크기의 미로 상자 출력하기
for i in range(1, 11):
    for j in range(1, 11):
        print(box[i][j], end = ' ')
    print()
