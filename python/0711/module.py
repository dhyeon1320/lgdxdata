import sys
print(sys.modules)  # 사용 가능한 module 확인
print(sys.path) # module을 찾는 위치 확인
# module을 찾는 위치를 추가하고자 하면 sys.path.append("찾는 위치")

import importpractice

sys.path.append("./") # 현재 directory에서 module이나 package를 검색하도록 설정

print(importpractice.p)
importpractice.func("모듈 사용")
