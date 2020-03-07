# #break 的簡易範例
# n=0
# while n<5:
#     if n==3:#if的條件對,就會執行break強制跳出迴圈外到print("最後的n: ",n).if的條件錯,就會跳過break直接下一行print(n)
#         break
#     print(n)#印出迴圈中的n
#     n+=1
# print("最後的n: ",n)#印出迴圈結束後的n#印出結果012最後的n:  3

# #continue的簡易範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: #x是偶數
#         continue #if的條件對,就continue往回for繼續.if的條件錯,跳過continue直接下一行print(x)
#     print(x)
#     n+=1
# print("最後的n: ",n)#印出結果13 最後的n:  2


#else 的簡易範例
# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum)#印出 0+1+2+...+10的結果

#綜合範例:找出整數平方根
#輸入9:得到3
#輸入11:得到【沒有】整數的平方根
# n=input("輸入一個正整數: ")
# n=int(n) #轉換輸入成數字
# for i in range(n): # i 從 0 ~ n-1
#     if i*i==n:
#         print("整數平方根",i)
#         break #if的條件對,就會print,再break直接強制結束迴圈,不執行else區塊.if條件錯了就直接跳else
# else:
#         print("沒有整數平方根")

