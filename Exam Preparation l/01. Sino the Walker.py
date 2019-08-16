h, m, s = input().split(":")
steps = int(input())
stepPerSec = int(input())
 
time_step = stepPerSec* steps
home_time = (int(h) * 3600) + (int(m) * 60) + int(s) + time_step
 
min, sec = divmod(home_time, 60)
hour , min = divmod(min, 60)
d, hour = divmod(hour, 24)
 
print(f"Time Arrival: {hour:02d}:{min:02d}:{sec:02d}")