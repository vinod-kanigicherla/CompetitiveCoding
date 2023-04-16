n = int(input())
total_time = 0
for _ in range(n):
    mins, secs = [int(i) for i in input().split(":")]
    total_time += secs
    total_time += mins * 60
mins_total = str(total_time // 60)
secs_total = str(total_time % 60)

if len(str(secs_total)) == 1:
    secs_total = "0" + secs_total

print(f"{mins_total}:{secs_total}")