import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'BUSAN02_LEESANGHOON'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
# HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
HOLES = [[2, 2], [127, 2], [252, 2], [2, 125], [127, 125], [252, 125]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

def cal_angle(st_x, st_y, ed_x, ed_y):
    width = ed_x - st_x
    height = ed_y - st_y

    tmp = math.degrees(math.atan2(math.fabs(height), math.fabs(width)))  # 임시로 사용할 각도

    if width >= 0 and height >= 0:  # 1사분면
        return 90 - tmp
    elif width <= 0 and height >= 0: # 2사분면
        return 270 + tmp
    elif width <= 0 and height <= 0:  # 3사분면
        return 270 - tmp
    else:                            # 4사분면
        return 90 + tmp

def cal_distance(st_x, st_y, ed_x, ed_y):
    return math.sqrt((ed_x - st_x)**2 + (ed_y - st_y)**2)

def find_destination(st, ed):
    rad_angle = math.radians(cal_angle(st[0], st[1], ed[0], ed[1]))
    dx = math.sin(rad_angle) * value
    dy = math.cos(rad_angle) * value
    return st[0] - dx, st[1] - dy


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

# sadfasdf
    if order == 1:
        target_nums = [1, 3]
    else:
        target_nums = [2, 4]
    
    if balls[target_nums[0]] == [-1.0, -1.0] and balls[target_nums[1]] == [-1.0, -1.0]:  # 내 타켓구가 다 없으면(내꺼 다 넣었으면)
        target_nums = [5]
    value = 5.73

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    min_ = 9999999
    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    for t in target_nums:
        if balls[t][0] < 0:
            continue
        
        targetBall_x = balls[t][0]
        targetBall_y = balls[t][1]

        for hole in HOLES:
            dif_angle = abs(cal_angle(targetBall_x, targetBall_y, hole[0], hole[1]) - cal_angle(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y))
            print(min_, dif_angle)
            if min_ > dif_angle:
                min_ = dif_angle
                min_distance = cal_distance(targetBall_x, targetBall_y, hole[0], hole[1]) + cal_distance(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)
                min_x, min_y = find_destination(balls[t], hole)
            
    print(min_)
    print(min_x, min_y)
    if min_ > 80:
        value = 5.3
        
    t_dist = cal_distance(balls[0][0], balls[0][1], min_x, min_y)
    angle = cal_angle(balls[0][0], balls[0][1], min_x, min_y)
    print(angle)
    if min_distance > t_dist * 2:
        power = min_distance * 0.3
    else:
        power = t_dist * 0.7



    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')