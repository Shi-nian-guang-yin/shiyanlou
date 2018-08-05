#_*_  coding:utf8 _*_
#!/usr/bin/env python3
import sys
import csv
from math import pow

def get_path(string):
    temp = string
    cfg_index = temp.index('-c')
    usr_index = temp.index('-d')
    o_index   = temp.index('-o')
    cfg_path  = temp[cfg_index+1]
    usr_path  = temp[usr_index+1]
    o_path    = temp[o_index+1]
    return cfg_path,usr_path,o_path

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

def salary_get(path):
    pf = open(path,'r')
    salary_data = csv.reader(pf,delimiter=',')
    work_num = []
    origin_salary = []
    for row in salary_data:
        num = row[0]
        a_salary = row[1]
        work_num.append(num)
        origin_salary.append(a_salary)
    num_sa_dict = dict(zip(work_num,origin_salary))
    pf.close()
    return num_sa_dict


# 传入
# para1  工号：初始工资 (单个)
# para2  保险种类：保险费率   （其中包含上下门限）
# 输出
# 填写文件的一行数据
def calc_tax(usr_num,usr_sa,**cfg):

    secure = safe_cfg.get_final_rate()
    bx_L = cfg['JiShuL']
    bx_H = cfg['JiShuH']
    User = usr_data
    Fast_calc_symbol = [0,105,555,1005,2755,5055,13505]
    Compare_list = [1500,4500,9000,35000,55000,80000,pow(2,64)]
    rate=[0.03,0.1,0.2,0.25,0.3,0.35,0.45]
    write_table[]

    write_table.clear()
    my_salary = int(usr_sa)
    write_table.append(usr_num)
    write_table.append(my_salary)
    if my_salary < bx_H and my_salary < bx_L:
        middlie_sb =  my_salary
    elif my_salary > bx_H:
        middlie_sb =  bx_H  
    elif my_salary < bx_L:
         middlie_sb =  bx_L
    sb = middlie_sb * secure 
    write_table.append(format(sb, '.2f'))
    if( my_salary-sb) > 3500:
        true_salary = my_salary-sb - 3500
    #    print ('true salary is:%.2f'%true_salary)
        rate_dict = dict(zip(Compare_list,rate))
        symbol_dict = dict(zip(Compare_list,Fast_calc_symbol))
        for rmb in Compare_list:
            if true_salary <= rmb:
                tax = true_salary*rate_dict[rmb] - symbol_dict[rmb]
    #           print('tax is %.2f'%tax)  
    else:
        tax = 0
    write_table.append(format(tax, '.2f'))
    After_tax = my_salary - sb - tax
    write_table.append(format(After_tax, '.2f'))
    return write_table


import pdb 
#pdb.set_trace()  
if __name__ == "__main__":
    try:
        url_string  = sys.argv[1:]
        cf_path,ur_path,out_path = get_path(url_string)
        safe_cfg = Cfg_load(cf_path) 
        usr_data = salary_get(ur_path)
#        shebaoH = safe_cfg.get_value('JiShuH')
#        shebaoL = safe_cfg.get_value('JiShuL')
        pf = open(out_path,'w')
        write = csv.writer(pf)
        for u_id,u_id in usr_data.items():
            if int(u_sa) < 0:
                raise ValueError()
            pdb.set_trace()  
            w_data = calc_tax(u_id,u_sa,safe_cfg.data)
            write.writerow(w_data)
        pf.close()
    except IndexError:
#  print('number %d parameter is fault'%count)    
        print('Parameter Error')
    except ValueError:
#  print('number %d parameter is fault'%count)
        print("Parameter Error")


