from InstagramAPI import InstagramAPI
import threading
import datetime
import time

#game function
def gamemode():
    p3_sc = 0
    print("ready")
    for i in range(3):
        time.sleep(1)
        
        print(3-i)
    time.sleep(1)
    print("start")
    
    sc1 = []
    
    now = time.time()
    future = now + 2
    
    while time.time() < future :
        innum = input()
        sc1.append(innum)
    
    
    
    p1_sc = len(sc1)
    print("stop")
    
    #print(p1_sc)
    
    time.sleep (3)
    
    print("ready")
    for i in range(3):
        time.sleep(1)
    
        print(3-i)
    print("start")
    
    sc2 = []
    
    now = time.time()
    future = now + 2
    
    while time.time() < future :
        innum = input()
        sc2.append(innum)
    
    p2_sc = len(sc2) - p1_sc
    print("stop")
    #print(p2_sc)
    
    if (p1_sc > p2_sc):
        #print("player1 win")
        return p1_sc
    elif(p1_sc < p2_sc):
        #print("player2 win")
        return p2_sc
    else :
        #print("draw")
        return p3_sc
    #c = counter()
    #print(c)

#아이디 비번 사진  입력 구간
p1_id = "p1_id"
p1_pw = "p1_pw"
p1_pi = "p1_pi"

p2_id = "p2_id"
p2_pw = "p2_pw"
p2_pi = "p2_pi"

p1_api = InstagramAPI("sample_id", "sample_pw")
p2_api = InstagramAPI("sample_id", "sample_pw")

api = InstagramAPI("sample_id", "sample_pw")

def check_time(curr_minute):
    dt = datetime.datetime.now()
    gaming = gamemode()
    if (gaming == p1_sc):
        
        global api
        global p1_api
        global p2_api
        
        api = p2_api
        #사진 경로 수정 필요
        photo_path_1 = 'D:/28750952_126473978106488_9046258563504144384_n.jpg'
        #게시글 내용 수정 필요
        caption = "뻐꾹"*minute + str(minute)
        api.uploadPhoto(photo=photo_path_1, caption=caption, upload_id=None)
        print("Upload succes!")

    elif(gaming == p2_sc):
        global api
        global p1_api
        global p2_api

        api = p1_api
        
        #사진 경로 수정 필요
        photo_path_2 = 'D:/28750952_126473978106488_9046258563504144384_n.jpg'
        #게시글 내용 수정 필요
        caption = "게임 벌칙으로 사진을 강제 업로드 합니다. - "Instacraft"
        api.uploadPhoto(photo=photo_path_2, caption=caption, upload_id=None)
        print("Upload succes!")
        
    elif(gaming == p3_sc):
        global api
        global p1_api
        global p2_api
        
        print("draw, don't upload")

    threading.Timer(1, check_time, args=[curr_minute]).start()

    

#api = InstagramAPI("sample_id", "sample_pw")
#로그인 하는 부분 간섭 ㅇㅇ
if (api.login()):

    api.getSelfUserFeed()  # get self user feed

    print(api.LastJson)  # print last response JSON

    print("Login succes!")

else:

    print("Can't login!")
    exit()

check_time(-1)


"""
#사진 및 게시글 포스팅

InstagramAPI = InstagramAPI("", "")

InstagramAPI.login()  # login


#사진 주소 \ 대신 /로
photo_path ="C:/Users/USER/Desktop/py/photo/black.jpg"
#게시글
caption = "Instgram_bot testing_Cecom"

InstagramAPI.uploadPhoto(photo_path, caption=caption)

"""
