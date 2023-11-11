
import requests
import os

def retstr(s:str,ss:str,inits:int)->str:
    a=s.find(ss,inits,len(s))
    if a<0:
        return s[inits:len(s)]
    return s[inits:a]


print("\x1bc\x1b[43;30m")

page = requests.get("https://www.bing.com/search?q=codebuil+github.com")
s=str(page.content)

ii=0
i=0
a=0
t=""
x1=0
x2=0
x3=0
i=s.find("<")
if i<0:
    i=0
l1=len(s)-1
xxx=0
while(1):
      
      if ii==True:
        break
      if i>=l1:
        break
      aa=retstr(s,'<',i)
      bb=retstr(s,"'",i)
      cc=retstr(s,'"',i)
      dd=retstr(s,">",i)
      a1=len(aa)
      b1=len(bb)
      c1=len(cc)
      d1=len(dd)
      if a1< b1 and a1<c1 and a1 < d1 and x1==0 and x2==0:
          print(aa)
          i=i+a1+1
          
      if d1< b1 and d1<c1 and d1 < a1 and x1==0 and x2==0:
          print(dd)
          i=i+d1+1
          
      if b1< a1 and b1<c1 and b1 < d1  and x2==0:
          print(bb,end="")
          i=i+b1+1
          if x1==0:
              x1=1
          else:
              x1=0
          
      if c1< a1 and c1<b1 and c1 < d1 and x1==0:
          print(cc,end="")
          i=c1+i+1
          if x2==0:
              x2=1
          else:
              x2=0
      if x1!=0 or x2!=0:
           xxx+=1
      if xxx>3:
           x1=0
           x2=0   
