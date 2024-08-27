

import requests
import json,time
from fake_useragent import UserAgent

proxy_list = [
  '116.62.35.65,80',
  '101.37.163.83,80',
  '121.41.53.86,80',
  '121.41.87.128,80',
  '47.96.253.74,80',

]
class RequestHttp():

  def __init__(self,use_proxy):
    if use_proxy:
      self.proxy_index = 0
      self.proxy = self.get_proxy(self.proxy_index)
    else:
      self.proxy = {}
    self.ua = UserAgent()
    agent = self.ua.random
    self.headers = {
      "User-Agent": agent
    }




  def get_proxy(self,index):
      proxy = proxy_list[index]
      proxy_host = proxy.split(",")[0]
      proxy_port = proxy.split(",")[1]
      proxyMeta = "https://%(host)s:%(port)s" % {
        "host" : proxy_host,
        "port" : proxy_port
      }

      proxies = {
        "http" : proxyMeta
      }
      return proxies



  def gen_request(self,url,method='GET',headers=None,params=None,body=None,timeout=15):
    print("[request]url={},headers={},proxy={}".format(url,self.headers,self.proxy))

    response = None
    if method == 'GET':
      response = requests.get(url,headers= self.headers,timeout=timeout,proxies=self.proxy)
    elif method == 'POST':
      response = requests.post(url,headers= self.headers,data=params,json=body,proxies=self.proxy)

    content = response.content
    status = response.status_code
    print("[response]response status={},response body={}".format(status,json.dumps(content.decode("UTF-8"),ensure_ascii=False)))
    if '频繁' in content.decode("UTF-8") and self.proxy_index < len(proxy_list) -1:
      print("访问请求频繁，切换代理")
      time.sleep(5)
      self.proxy_index += 1
      self.proxy = self.get_proxy(self.proxy_index)

      agent = self.ua.random
      print("生成新的user-agent:{}".format(agent))
      self.headers = {
        "User-Agent": agent
      }

      return self.gen_request(url,method,headers,params,body,timeout)

    return response




