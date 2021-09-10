t = int(input())
result = []
fold_list = []
for i in range(t) :
    fold = input()
    fold_list.append(fold)

#1이랑 0변할때를 활용 -> 문자열뒤집기랑 비슷??
#3개씩 기준으로 1 00 혹은 0 11 형태여야함!
for f in fold_list :
    