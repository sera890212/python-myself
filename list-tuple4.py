#有序可變動列表 List

grades=[12,60,15,70,90]#中括號
grades[1:4]=[]#連續刪除列表中1~4(不包含4)所以剩12、90
print(grades)
grades=grades+[12,33]#在本來的列表後面加12，33
print(grades)
length=len(grades)#取得grades的長度，放到新的變數length裡面
print(length)#印出
grades[0]=55#把55放到列表中的第一個位置
print(grades[0])#取得列表中的第1個資料
#列表裡面再放一個列表(巢狀列表)
#data=[[3,4,5],[6,7,8]]#345一個列表 678另一個列表
#data[0][0:2]#345裡面的34 不包含5
#data[0][0:2]=[5,5,5]#34換成555 會變4個5
#print(data[0])#把0代表345印出來
#print(data[0][1])#0代表345 1代表345裡面的4
#print(data)#把整個列表印出來

#有序不可變動列表 Tuple
#data=(3,4,5)#小括號
#print(data[2])#印出5
#print(data[0:2])#印出34
#data[0]=5 # 錯誤 : Tuple的資料不可以變動