import zipfile
# 압축할 파일 목록 생성
# filelist = ['./data/data.dat', './data/test.bin']
# # 파일 목록을 순회하며 압축
# with zipfile.ZipFile('./data/datas.zip', 'w') as myzip:
#     for temp in filelist:
#         myzip.write(temp)

zipfile.ZipFile("./data/datas.zip").extractall()