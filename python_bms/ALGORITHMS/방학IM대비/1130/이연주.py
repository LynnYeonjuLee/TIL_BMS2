w,h = list(map(int,input().split()))
p, q = list(map(int, input().split()))
t = int(input())
# p_point = p 
# q_point = q
# for _ in range(t):
#     if p_point < w and q_point < h:
#       p_point += 1
#       q_point += 1
#     elif p_point == w:
#         p_point -= 1
#         q_point += 1
#     elif p_point == w or q_point == h:
#         p_point -= 1
#         q_point -= 1
#     elif p_point > 0 and q_point == 0:
#         p_point -= 1
#         q_point += 1
#     elif p_point == 0:
#         p_point += 1
#         q_point += 1
# print(p_point)
# print(q_point)

p_length = p + t
p_location = p_length%w
if (p_length // w) % 2 == 0:
    p_location == p_location
else: 
    p_location = w - p_location
q_length = q + t
q_location = q_length%h
if (q_length // h) % 2 == 0:
    q_location == q_location
else: 
    q_location = h - q_location
print(p_location, q_location)