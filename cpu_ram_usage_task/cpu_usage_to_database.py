import csv
import os
import  psycopg2
conn=psycopg2.connect(database="cpu_ram_usage", user="raghugr", password="raghugr@27", host="127.0.0.1", port="5432")
cur=conn.cursor()
cur.execute("select * from cpu_ram_usage")
print(cur.fetchall())
with open("input.csv", "r") as f:
    r = csv.reader(f)
    for i in r:
        cpu_usage = os.popen(
            "ssh {}@{} {}".format(
                i[0], i[1], "top -b -n1 | grep \"Cpu(s)\" | awk '{print $2 + $4}'"
            )
        )
        ram_usage = os.popen(
            "ssh {}@{} {}".format(
                i[0], i[1], "free -t | awk 'FNR == 2 {print $3/$2*100}'"
            )
        )
        cur.execute("insert into cpu_ram_usage(hostname,ip_address,cpu_usage,ram_usage) values(%s,%s,%s,%s)",
                    (i[0],
            (i[1]),
            cpu_usage.read().rstrip("\n"),
            ram_usage.read().rstrip("\n")))
        conn.commit()

