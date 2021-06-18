#시간 문제 땜에..
#idx, 요소 & enumerate 활용했었는데.. 더 좋은 방법??
def solution(genres, plays):
    
    answer = []
    genre_dic = {}
    genre_total_play = {}
    
    
    for i in range(len(genres)): 
        if genres[i] not in genre_dic.keys(): 
            #genre_dic와 genre_total_play를 동시에 만들어가야함.
            genre_dic[genres[i]] = [(plays[i], i)] 
            genre_total_play[genres[i]] = plays[i] 
                
        else: 
            genre_dic[genres[i]].append((plays[i], i)) 
            genre_total_play[genres[i]] = genre_total_play[genres[i]] + plays[i]

    sorted_total_play = sorted(genre_total_play.items(), key=lambda x : x[1], reverse=True)
    #items()는 무조건 tuple형식
    print(sorted_total_play)
    
    for key in sorted_total_play :
        
        play_list = genre_dic[key[0]]
        
        play_list = sorted(play_list, key = lambda x : (-x[0], x[1]))
        #튜플원소들 정렬할땐 이렇게!
        
        for i in range(len(play_list)) :
            if i == 2 :
                break
            
            answer.append(play_list[i][1])
            
    
    
    return answer

#먼저 총 점수를 활용하여 많이 재생된 장르를 선택
#장르가 선택됐으면, 저장해뒀던 genre_dic[[key[0]]] 를 가져와서 활용
#key[0]은 장르 이름 -> 이걸 활용하여 장르 : 각각 노래 횟수들 에서 노래 횟수들만 가져올 수 있음.