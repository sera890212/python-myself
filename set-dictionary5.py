#集合的運算
#s1={3,4,5}#大括號
#print(3 in s1)#3在s1中? 有就印出true 沒就印出false
#print(10 not in s1)#10不在s1中

#s1={3,4,5}
#s2={4,5,6,7}
#s3=s1&s2# & : 交集 :取兩個集合中，相同的資料
#s3=s1|s2 # | : 聯集 :取兩個集合中的所有資料，但不重複取 
#s3=s1-s2 # - : 差集 : 從s1中，減去和s2重疊的部分 #所以只印出3
#s3=s1^s2 # ^ : 反交集 : 取兩個集合中，不重疊的部分 #所以印出367
#print(s3)

#s=set("Hello")#把字串中的字母拆解成集合 : set(字串)重複的部分不會取 所以印出HELO
#print(s)
#print("a" in s)
#字典的運算:key-value配對
#dic={"apple":"蘋果","bug":"蟲蟲"}
#dic["apple"]="小蘋果"#更改
#print(dic["apple"])
#print("test"  not in dic)#判斷key是否存在

#dic={"apple":"蘋果","bug":"蟲蟲"}
#print(dic)
#del dic["apple"]#刪除字典中的鑑值對(key-value pair):刪除apple蘋果
#print(dic)

dic={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic)
