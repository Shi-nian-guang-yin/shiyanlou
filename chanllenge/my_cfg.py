#_*_ coding:utf8 _*_
#! /usr/bin/env python3
class Cfg_load(object):
    def __init__(self,string):
        f_path = string
        fp = open(f_path,'r')
        str_stream = fp.read().strip()
        fp.close()
        self.para = []
        self.rate = []
        self.orgin_data = str_stream.split('\n')
       # print(self.orgin_data)
        for data in self.orgin_data:
            temp  = data.split('=')
        #    print(temp)
            self.para.append(temp[0].strip())
            self.rate.append(float(temp[1].strip()))
        self.data = dict(zip(self.para,self.rate))
    def get_name_list(self):
         return self.para
    def get_rate_list(self):
         return self.rate
    def get_value(self,key):
         return self.data[key]
    def get_final_rate(self):
         total_rate = 0
         temp = self.para
         temp.remove('JiShuL')
         temp.remove('JiShuH')
         for i in temp:
             total_rate += self.data[i]
         return total_rate
  
            
           
