import MySQLdb

# ClearDB에 연결
db = MySQLdb.connect(
    host="us-cluster-east-01.k8s.cleardb.net",
    user="b72db6db36294f",
    passwd="ea9118b3",
    db="heroku_1672c264c8a5662"
)

cursor = db.cursor()

# 연결된 모든 세션을 조회하고 종료
cursor.execute("SHOW PROCESSLIST")
processes = cursor.fetchall()

for process in processes:
    id = process[0]
    if process[1] != 'system user':  # 시스템 프로세스는 종료하지 않음
        try:
            cursor.execute(f"KILL {id}")
        except Exception as e:
            print(f"Error killing process {id}: {e}")

cursor.close()
db.close()
