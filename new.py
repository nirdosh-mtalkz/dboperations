from flask import Flask,request
import math
import datetime
app=Flask(__name__)

app.config['DEBUG']=True

@app.route('/checkPrime/<int:val>',methods=['GET'])
def check_prime(val):
    if val==2 or val==3:
        return "True"
    else:
        for i in range(2,int(math.sqrt(val))+1):
            if val%i==0:
                return "False"
        return "True"


@app.route('/checkFact/<int:val>',methods=['POST'])
def fact(val):
    if val==0 or val==1:
        return str(1)
    else:
        fct=1
        for i in range(2,val+1):
            fct *= i
        return str(fct)

@app.route('/date',methods=['GET'])
def date():
    return str(datetime.date.today())


@app.route('/vowels',methods=['GET','POST'])
def vowels():
    args = request.args
    txt = args.get('text')
    #txt = request.data
    a=e=i=o=u=0
    for letter in txt:
        if letter=='a':a+=1
        if letter=='e':e+=1
        if letter=='i':i+=1
        if letter=='o':o+=1
        if letter=='u':u+=1
    vowel_count ={}
    vowel_count['a'] = a
    vowel_count['e'] = e
    vowel_count['i'] = i
    vowel_count['o'] = o
    vowel_count['u'] = u
    return vowel_count

if __name__ == '__main__':
    app.run()