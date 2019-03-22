data = {0: [33361,"Abdullah","021-32734352","0321-2243424"], 1: [39859,"Saif","021-34756434","0312-4346487"] , 2: [42342,"Zara","021-36533567","0345-7588436"] ,
        3:[" "] ,4:[" "] , 5:[" "] , 6:[" "] , 7:[33222,"Ali","021-35343556","0334-6322480"] , 8:[" "] , 9:[32567,"Bilal","021-35323457","0321-4532445"] ,
        10:[38261,"Asher","021-34521356","0333-5547732"] , 11:[" "] , 12:[" "] , 13:[" "] , 14:[" "] ,15:[11111,"Hamza","021-34557760","0312-2092294"] ,
        16:[" "] , 17:[68564,"Varisha","00233-340252","000242464566"] , 18:[68637,"Wajahat Sarwat","021-32157896","0345-6431286"] ,
        19:[89953,"Umer","021-32167853","00932442425637"] , 20:[69076,"Samreen","021-32189554","0332-2562567"] , 21:[" "] ,
        22:[" "] , 23:[" "] , 24:[" "] , 25:[" "] , 26:[12144,"Saad","04221-2342577","0003-445564677"],
        27:[18641,"Wajahat","021-37897542","0301-3675885"] , 28:[24556,"Ukasha","021-3456784","0321-2358756"] , 29:[" "] , 30:[" "] ,
        31:[" "] , 32:[" "] , 33:[" "] , 34:[" "] , 35:[" "] , 36:[" "] ,
        37:[" "] , 38:[" "] , 39:[" "] , 40:[" "] ,
        41:[48950,"Faraz jaffery","021-32743017","0333-3567759"] , 42:[42455,"Arsh","021-34567896","0300-0004677"] , 43:[" "] , 44:[" "] , 45:[" "] ,
        46:[" "] , 47:[" "] , 48:[" "] , 49:[33556,"Sana","021-38421678","0301-0009653"] , 50:[" "] , 51:[" "] ,
        52:[" "] , 53:[" "] , 54:[" "] , 55:[" "] , 56:[88824,"Saad Alam","021-34217782","0315-6532145"] ,
        57:[" "] , 58:[78678,"Umair aslam","021-37868995","0300-0009443"] , 59:[88825,"Fahad","9992-302424242","0313-4442421"] ,
        60:[70724,"Ukasha","021-37899655","0345-0909786"] , 61:[75615,"Ali Imran","021-34213456","0346-0978560"] , 62:[99999,"Osama","021-32190875","0312-2956657"] , 63:[" "] ,
        64:[" "] , 65:[" "] , 66:[" "] , 67:[" "] , 68:[" "] , 69:[22334,"Anas","9911-32445675","0004-5242523623"] ,
        70:[" "] , 71:[" "] , 72:[65334,"Rubab","021-32145672","0311-0099776"] , 73:[" "] , 74:[" "] }





## ***** For Insertion of Data****
def insert():
    empNum = int(input("enter 5 digit employe number: "))
    empName = input("enter Employe name: ")
    empTel = input("enter Employe telephone number: ")
    empLand = input("Enter employe mobile Number: ")

    hashCode = empNum % 73
    info = [empNum , empName, empTel, empLand,hashCode]
    probes = 1
    i=0
    for i in data.keys():
        if i == hashCode:
            while i <= max(data.keys()):
                if data[i] == [" "]:
                    data[i] = info
                    break
                else:
                    i+=1
                    probes+=1
    print(data)
    print("\n")
    print("Hash code is ",hashCode)
    print("\n")
    print("Number of probes is ",probes)
    print("\n")


## 5 digits multiples of 73 are 33288, 34237, 42267
    
## **** For Searching of Data****
    
def search():

    empNum = int(input(' enter emp id: '))

    hashing = empNum % 73
    count = 0
    i=0
    for i in data.keys():
        if i == hashing:
            while count<= max(data.keys()):
                a=data[count]
                if empNum == a[0]:
                    print(a)
                    print('hash key is ',hashing)
                    print('No. of successful probes is ',(count+1) - hashing)
                    break
                else:
                    count+=1
            break
        else:
            i=i+1

    if empNum !=a[0]:
        print('Sorry Not Found')
        lis=[]
        for x in data.keys():
            if data[x] == [" "]:
                lis.append(1)
            else:
                y= x+1
                while y <= max(data.keys()):
                    if data[y] == [" "]:
                        lis.append((y+1)-x)
                        break
                    else:
                        y=y+1

        print('hash key is ',hashing)
        print('NO. of unsuccessful probes is ',lis[hashing])


