sampleSize = 24

#storing the 160K features in an external file called 160Kfeatures.txt
f = open("160Kfeatures.txt", "w")

#horizontal features

#feature 1x2
for i in range(0,sampleSize+1):
    for j in range(0,sampleSize+1):
        for w in range(1,int(sampleSize/2)+1): # from i = 1 to i = 12
            for h in range(1,sampleSize+1): # from i = 1 to i = 24
                #print('1 , i , j , h , wW , wB')
                if(w <= int((sampleSize-j)/2) and h <= (sampleSize-i)):
                    string = str(1)+' '+str(i)+' '+str(j)+' '+ str(h) +' '+str(0)+' '+str(w)+' '+str(w)+'\n'
                    f.write(string)
                    #print(1,',',i,',',j,',', h,',','0 ,',w,',',w)

#feature 1x3
for i in range(0,sampleSize+1):
    for j in range(0,sampleSize+1):
        for w in range(1,int(sampleSize/3)+1): # from i = 1 to i = 12
            for h in range(1,sampleSize+1): # from i = 1 to i = 24
                #print('1 , i , j , h , wW , wB')
                if(w <= int((sampleSize-j)/3) and h <= (sampleSize-i)):
                    string = str(2)+' '+str(i)+' '+str(j)+' '+ str(h) +' '+str(w)+' '+str(w)+' '+str(w)+'\n'
                    f.write(string)
                    #print(2,' ',i,' ',j,' ', h,' ', w,' ', w,' ',w)

#vertical features

#feature 2x1
for i in range(0,sampleSize+1):
    for j in range(0,sampleSize+1):
        for h in range(1,int(sampleSize/2)+1): # from i = 1 to i = 24
            for w in range(1,sampleSize+1): # from i = 1 to i = 12
                #print('1 , i , j , h , wW , wB')
                if(h <= int((sampleSize-i)/2) and w <= (sampleSize-j)):
                    string = str(3)+' '+str(i)+' '+str(j)+' '+ str(h) +' '+str(h)+' '+str(0)+' '+str(w)+'\n'
                    f.write(string)
                    #print(3,' ',i,' ',j,' ', h,' ',h,' ',0,' ',w)

#feature 3x1
for i in range(0,sampleSize+1):
    for j in range(0,sampleSize+1):
        for h in range(1,int(sampleSize/3)+1): # from i = 1 to i = 24
            for w in range(1,sampleSize+1): # from i = 1 to i = 12
                #print('1 , i , j , h , wW , wB')
                if(h <= int((sampleSize-i)/3) and w <= (sampleSize-j)):
                    string = str(4)+' '+str(i)+' '+str(j)+' '+ str(h) +' '+str(h)+' '+str(h)+' '+str(w)+'\n'
                    f.write(string)
                    #print(4,' ',i,' ',j,' ', h,' ', h,' ',h,' ',w)

#feature 2x2
for i in range(0,sampleSize+1):
    for j in range(0,sampleSize+1):
        for w in range(1,int(sampleSize/2)+1): # from i = 1 to i = 12
            for h in range(1,int(sampleSize/2)+1): # from i = 1 to i = 24
                if(h <= int((sampleSize-i)/2) and w <= int((sampleSize-j)/2)):
                    string = str(5)+' '+str(i)+' '+str(j)+' '+ str(h) +' '+str(h)+' '+str(w)+' '+str(w)+'\n'
                    f.write(string)
                    #print(5,' ',i,' ',j,' ', h,' ', h,' ',w,' ',w)

#closing the file
f.close()
