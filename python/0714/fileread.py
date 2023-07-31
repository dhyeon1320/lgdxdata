import os
import csv
print(os.getcwd())  # 상대 경로를 설정할 때 기준 경로

# 파일 읽기
try:
    file = open('./data/test.txt', encoding='utf-8')  # 파일 깨지는 지 확인하고 인코딩 방식 추가
    content = file.read()  # 전체 읽기
    print(content)
except Exception as e:
    print("파일 처리 중 예외 발생", e)
finally:
    file.close()


# 줄 단위로 파일 읽기
try:
    file1 = open('./data/test1.txt', encoding='utf-8')  # 파일 깨지는 지 확인하고 인코딩 방식 추가
    for line in file1:
        print(line)
except Exception as e:
    print("파일 처리 중 예외 발생", e)
finally:
    file.close()


# with 사용
with open('./data/test1.txt', encoding='utf-8') as file:
    for line in file:
        print(line)
        print()

# 텍스트 파일을 읽어서 list로 변환
# 마지막 데이터에는 \n 추가됨
# 마지막 데이터는 \n 제거해야 함
data = []
with open('./data/경상북도 울릉군_대회정보_20211013.csv', encoding='cp949') as file2:
    for line in file2:
        ar = line.split(",")
        data.append(ar)
print(data)

data1 = []
with open('./data/경상북도 울릉군_대회정보_20211013.csv', encoding='cp949') as file2:
    # 줄 단위로 읽어서 list를 만들어주는 reader 객체를 생성
    rdr = csv.reader(file2)
    for line in rdr:
        data1.append(line)
print(data1)


data2 = []
# w 모드로 열면 기존 내용을 지우고 기록하고 a 모드로 열면 기존 내용 뒤에 추가함
with open('./data/경상북도 울릉군_대회정보_20211013.csv', 'w', encoding='cp949') as file3:
    wr = csv.writer(file)
    wr.writerow(['경상북도','울릉군','대회정보'])
    wr.writerow(['20211013'])
