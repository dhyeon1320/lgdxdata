# 접속
import redis
print(dir(redis))

# 데이터베이스 접속
with redis.StrictRedis(host='localhost', port=6379) as conn:
    # 문자열 저장
    conn.set("name", "kim")
    # 문자열 가져오기 - bytes로 반환
    data = conn.get("name")
    print(data)  # 인코딩 결과 출력됨
    print(data.decode('utf-8'))  # 인코딩 결과 출력됨

# Connection Pool 이용한 접속
import time
redis_pool = redis.ConnectionPool(host='localhost', port=6379, max_connections=4)
with redis.StrictRedis(connection_pool=redis_pool) as conn:
    # 만료 시간 설정 가능
    conn.set("name", "kim", 10)  # 만료 시간 10초
    # 만료 시간 확인
    print(conn.ttl("name"))

    conn.set("song", "노래")
    conn.expire("song", 10) # 데이터 만료 시간 10초 설정
    print(conn.get("song"))
    time.sleep(20)
    print(conn.get("song")) # 20초 후 데이터 가져올 때는 데이터 없어서 None

with redis.StrictRedis(connection_pool=redis_pool) as conn:
    # 리스트에 데이터 저장
    conn.lpush("album", "genesis")
    conn.rpush("album", "exodus")

    for album in conn.lrange("album", 0, 10):
        print(album)