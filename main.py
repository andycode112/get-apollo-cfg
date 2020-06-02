'''
@Author: andycode112
@Date: 2020-06-02 10:22:10
@LastEditTime: 2020-06-02 21:55:33
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\get-apollo-cfg\main.py
'''
import flask
from flask import request
import requests,pickle,json,os

app = flask.Flask(__name__)
@app.route('/',methods=['get'])
def health():
    ret={'code':200,'message':'the server is ok'}
    return json.dumps(ret,ensure_ascii=False)

@app.route('/getapollocfg',methods=['get'])
def getapollocfg():
    _appname = request.values.get('appname')
    _env = request.values.get('env')
    _namespace = request.values.get('namespace')
    _access_token = request.values.get('access_token')
    ret = {}
    if _appname != None and len(_appname) > 0 and \
       _env != None and len(_env) > 0 and \
       _namespace != None and len(_namespace) > 0 and  \
       _access_token != None and len(_access_token) > 0 :
       _apolloip = os.environ['apolloip']
       _apolloport = os.environ['apolloport']
       url = 'http://{0}:{1}/apps/{2}/envs/{3}/clusters/default/namespaces/{4}?access_token={5}'.format(_apolloip,_apolloport,_appname,_env,_namespace,_access_token)
       res = requests.get(url,verify=False)
       res.encoding = 'utf-8'   #通过修改编码方式为utf-8，使得汉字得到识别
       if res.status_code == 200 :
           try:
               responsedata = res.json()
               mylist=[]
               for item in responsedata['items']:
                   newitem = {'key':item['item']['key'],'value':item['item']['value']} 
                   mylist.append(newitem)
                   # print(item['item']['key']+'      '+item['item']['value'])
               ret= {'success':True,'data':mylist,'msg':''} # pickle.dumps(mylist)#dict(mylist) 
           except Exception as e:
               #print(e.args)
               ret= {'success':False,'data:':'','msg':e.args}       
       else:
           ret= {'success':False,'data:':'','msg':'the requests status_code is ' + res.status_code}
    else:
       ret= {'success':False,'data:':'','msg':'the appname、env、namespace and access_token params is None or empty'}
    # print(ret)
    return ret # pickle.dumps(ret)

if __name__ == "__main__":
     app.run(debug=True,port = 5000,host='0.0.0.0')
    
