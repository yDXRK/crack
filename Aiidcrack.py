import os
#os.system('pip install OneClick')
#os.system('pip install stdiomask')
#os.system('pip install requests')
#os.system('pip install random')
#os.system('pip install threading ')
#os.system('pip install time')
#os.system ("pip install uuid ")
#os.system ("pip install user_agent")
#os.system ("pip install bs4")
os.system("clear")
import requests , uuid , stdiomask , time , os , random , threading
from uuid import uuid1,uuid4 ; from OneClick import Hunter ; from user_agent import generate_user_agent
#𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
uid=str(uuid.uuid4())
true=0
false=0
chk=0
error=0
#𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳
B = '\x1b[38;5;208m'  # برتقالي
E = '\033[1;31m'  # أحمر
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
Ca = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\x1b[38;5;208m'
V1 = '\033[2;32m'
V2 = '\033[1;33m'
V3='\x1b[38;5;209m'
V4= '\x1b[1;97m'
V5 = '\x1b[38;5;8m'
a32 = '\x1b[38;5;180m'  # بني فاتح
a14 = '\x1b[38;5;153m'  # أزرق فاتح
P = '\x1b[1;97m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
R1 = '\033[1;31;40m'
X1 = '\033[1;33;40m' 
F1= '\033[1;32;40m' 
C1 = "\033[1;97;40m" 
B1 = '\033[1;36;40m'
K1 = '\033[1;35;40m'
V1 = '\033[1;36;40m'
E = '\033[1;31m' #احمر
X= '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
Ca = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
Ca = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
#𓏳𓏳𓏳𓏳𓏳𓏳𓏳𓏳


def clear():
	print(f"{V4} ")
	print('\n')
ID = input(f'\n{a32} Enter Id Telegram : ')
token = input(f'\n{a14} Enter Token Bot Telegram : ')
os.system('clear' if os.name == 'posix' else 'cls')
clear()



def hh():
    uk= [Z,X,F,f]
    global true,false,chk,error,uid,logo
    
    while True:
        uk= [X,F,f,Y,B,Ca,y]
        co1= random.choice(uk)
        col2= random.choice(uk)
        col3= random.choice(uk)
        col4= random.choice(uk)
        col5= random.choice(uk)    
        th = time.ctime()
        v1= ''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v2 =''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v3= ''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v4 = ''.join(random.choice('aqswedrftgyhujikopzxcvbnm')for i in range(1))
        v5= ''.join(random.choice('1234567890')for i in range(1))
        v6= ''.join(random.choice('1234567890')for i in range(1))
        user1 = v1+'_'+v2+'_'+v3
        user2 = v1+'.'+v2+'.'+v3
        user4 = v1+'_'+v2+'.'+v3
        user5 = v1+'.'+v2+'_'+v3
        user6 = v1+v2+v3+'_'+v4
        user7 = v1+v2+v3+'.'+v4
        user8 = '_'+v1+v2+v3+v4
        user9 = '.'+v1+v2+v3+v4
        user10 = v1+v2+'.'+v3+v4
        user11 = v1+v2+'_'+v3+v4
        user12= "_"+v1+v1+'_'+v3
        num= '_'+v5+v5+'_'+v6
        num2= '.'+v5+v5+'.'+v6
        m3= v1+v2+v2+v1+v5
        usse= [user1,user2,user4,user5,user6,user7,user8,user9,user11,user10,user12,num,num2]
        user= random.choice(usse)
 
        url='https://i.instagram.com/api/v1/accounts/create/'
        hea={
            'Host': 'i.instagram.com',
            'cookie': 'mid=Y16iBgABAAFggfUYwajggkGFz-hs',
            'x-ig-capabilities': 'AQ==',
            'cookie2': '$Version=1',
            'x-ig-connection-type': 'WIFI',
            'user-agent': Hunter.Services(),
            'content-type': 'application/x-www-form-urlencoded',
            'content-length': '159',

        }
        data={
            'password':'qqwwaassddffgghh4455',
            'device_id':uid,
            'guid':uid,
            'email':'ll9678785@gmail.com',
            'username':user,
        }
        res=requests.post(url,headers=hea,data=data,proxies=None).text
        #print(res);exit()

        
        if '{"account_created": false, "errors": {"email": ["Another account is using the same email."]}, "status": "ok", "error_type": "email_is_taken"}'in res:
            os.system('cls'if os.name=='nt'else'clear')
            true+=1
            chk+=1
            clear()
            print(f'''{co1}            < ¦ {F}True : {Ca}{true} ~ {E}User-False {Ca}{false} {co1} ¦ >{P}''')               
            hit = f'''
┏━━━━━𓆩Mmd𓆪━━━━┓
╟ ● 𝗨𝘀𝗲𝗿𝗡𝗮𝗺𝗲 ↝ {user}
┗━━━━━𓆩Mmd𓆪━━━━┛
𝗣𝗥𝗢𝗚𝗥𝗔𝗠 : @S628l
'''
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={hit}')
        
        elif 'Please wait a few minutes before you try again.'in res:
            os.system('cls'if os.name=='nt'else'clear')
            error+=1
            chk+=1
            clear()
            print(f'''{co1}            < ¦ {F}True : {Ca}{true} ~ {E}User-False {Ca}{false} {co1} ¦ >{P}''')               
            exit()
        else:
            
            os.system('cls'if os.name=='nt'else'clear')
            chk+=1
            false+=1
            clear()
            print(f'''{co1}            < ¦ {F}True : {Ca}{true} ~ {E}User-False {Ca}{false} {co1} ¦ >{P}''')                   
threads = []
for i in range(10):  
    t = threading.Thread(target=hh)
    threads.append(t)
    t.start()
for t in threads:
    t.join()