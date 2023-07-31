code = []
ip = []
traffic = []
ipcount = {}
cnt = 0
total = 0
ipCount = {}
with open('./data/log.txt') as file:
    # 줄 단위로 읽기
    for line in file:
        total += 1
        # 읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        code.append(ar[-2])
        # ip 별 접속 횟수 세기 - dict
        if ar[0] not in ipcount:
            ipcount[ar[0]] = 1
        else:
            ipcount[ar[0]] += 1
        ipCount[ar[0]] = ipCount.get(ar[0], 0)+1
        ip.append(ar[0])
        if ar[-1] != '-':
            traffic.append(ar[-1])
        # 응답 코드가 200인 데이터의 개수 세기
        if ar[-2] == '200':
            cnt += 1




print(ip)
print(len(ip))
print(ipcount)
print(traffic)
print(len(traffic))
print(code)
print(len(code))

print(total)
for ip in ipCount:
    print(ip, ipCount[ip])

# 응답 코드가 200인 데이터의 개수 세기
cnt = 0
with open('./data/log.txt') as file:
    # 줄 단위로 읽기
    for line in file:
        total += 1
        # 읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        if ar[-2] == '200':
            cnt += 1

print("200의 개수:", cnt)


# ip 별 접속 횟수 세기 - dict
# 내 풀이
ipcount = {}
with open('./data/log.txt') as file:
    # 줄 단위로 읽기
    for line in file:
        total += 1
        # 읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        if ar[0] not in ipcount:
            ipcount[ar[0]] = 1
        else:
            ipcount[ar[0]] += 1

print(ipcount)

# 답안
ipCount = {}
with open('./data/log.txt') as file:
    # 줄 단위로 읽기
    for line in file:
        total += 1
        # 읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        # ar[0] - IP
        # ar[0]을 key로 해서 ar[0]의 값에 1 더하기
        # 기존의 값을 가져오는데 없으면 0
        ipCount[ar[0]] = ipCount.get(ar[0], 0) + 1

print(ipCount)






# ip별 트래픽 합계
# 내 풀이1
trafficsum = {}
with open('./data/log.txt') as file:
    # 줄 단위로 읽기
    for line in file:
        # 읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        # ip 별 접속 횟수 세기 - dict
        if ar[-1].isdigit() == False:
            continue
        else:
            if ar[0] not in trafficsum:
                trafficsum[ar[0]] = int(ar[-1])
            else:
                trafficsum[ar[0]] += int(ar[-1])


print(trafficsum)

# 내 풀이2
trafficsum1 = {}
with open('./data/log.txt') as file:
    # 줄 단위로 읽기
    for line in file:
        # 읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        # ip 별 접속 횟수 세기 - dict
        if ar[-1] == '-' or ar[-1] == '''"-"''':
            continue
        else:
            if ar[0] not in trafficsum1:
                trafficsum1[ar[0]] = int(ar[-1])
            else:
                trafficsum1[ar[0]] += int(ar[-1])

print(trafficsum1)


# 답안
iptraffic = {}
with open('./data/log.txt') as file:
    # 줄 단위로 읽기
    for line in file:
        # 읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        try:
            iptraffic[ar[0]] = iptraffic.get(ar[0],0) + int(ar[9])
        except Exception as e:  # 숫자 문자열 아닌 건 except로 처리
            print(e)

for ip in iptraffic:
    print(ip, ":", iptraffic[ip])


