import os
print(os.getcwd())  # 상대 경로를 설정할 때 기준 경로
# 파일 쓰기
try:
    file = open('./data/test.txt','w', encoding='utf-8')
    file.write('안녕하세요\n')  # 문자열 기록 - window는 기본이 cp949인데 python은 utf-8이라서 깨짐
    lines = ["kim", "lee", "park", "choi"]
    file.writelines('\n'.join(lines))

except Exception as e:
    print("파일 처리 중 예외 발생", e)

finally:
    file.close()

