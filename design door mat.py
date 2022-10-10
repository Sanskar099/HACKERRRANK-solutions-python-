n, m = map(int,input().split())
#top
i = int((m-3)/2)
j= 1
while i>=3:
    print('-'*i+'.|.'*j+'-'*i)
    i = i-3
    j =j+2
# middle
temp = int((m-7)/2)
print('-'*temp+"WELCOME"+'-'*temp)
# bottom
j = j-2
i = i+3
while i<=int((m-3)/2):
    print('-'*i+'.|.'*j+'-'*i)
    i = i+3
    j =j-2
