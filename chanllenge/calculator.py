#_*_  coding:utf8 _*_
#!/usr/bin/env python3
import sys
import csv
from math import pow
from my_cfg import Cfg_load
from salary import salary_get
secure = 0
def calc_tax(my_salary):
    global secure
    Fast_calc_symbol = [0,105,555,1005,2755,5055,13505]
    Compare_list = [1500,4500,9000,35000,55000,80000,pow(2,64)]
    rate=[0.03,0.1,0.2,0.25,0.3,0.35,0.45]
    if( my_salary-my_salary * secure) > 3500:
        true_salary = my_salary-my_salary * secure - 3500
    else:
        return 0
#    print ('true salary is:%.2f'%true_salary)
    rate_dict = dict(zip(Compare_list,rate))
    symbol_dict = dict(zip(Compare_list,Fast_calc_symbol))
    if true_salary > Compare_list[-1]:
        print('''This poor_man don't need a tax_calc ''')    
    for rmb in Compare_list:
        if true_salary <= rmb:
            After_tax = true_salary*rate_dict[rmb] - symbol_dict[rmb]
 #           print('After_tax is %.2f'%After_tax)  
            return After_tax

def get_path(string):
    temp = string
    cfg_index = temp.index('-c')
    usr_index = temp.index('-d')
    o_index   = temp.index('-o')
    cfg_path  = temp[cfg_index+1]
    usr_path  = temp[usr_index+1]
    o_path    = temp[o_index+1]
    return cfg_path,usr_path,o_path

import pdb 
#pdb.set_trace()  
if __name__ == "__main__":
    try:
        url_string  = sys.argv[1:]
        cf_path,ur_path,out_path = get_path(url_string)
        safe_cfg =Cfg_load(cf_path) 
        secure = safe_cfg.get_final_rate()
        shebaoH = safe_cfg.get_value('JiShuH')
        shebaoL = safe_cfg.get_value('JiShuL')
 #       pdb.set_trace()
        usr_num,usr_data = salary_get(ur_path)
       # usr_list = list(usr_data.keys())
        write_table = []
        write_tables = []
        pf = open(out_path,'w')
        write = csv.writer(pf)
  #      pdb.set_trace()
        for i in usr_num:
            st_temp = int(usr_data[i])
            if st_temp > shebaoL and st_temp < shebaoH:
                sb_temp = st_temp
            elif st_temp < shebaoL:
                sb_temp = shebaoL
            elif st_temp > shebaoH:
                sb_temp = shebaoH
            write_table.clear()
            write_table.append(i)
            write_table.append(usr_data[i])
            sa_temp =('%.2f'%(sb_temp*secure)) 
            write_table.append(sa_temp)
            sc_temp =('%.2f'%(calc_tax(sb_temp)))
            write_table.append(sc_temp)
            sd_temp =('%.2f'%(sb_temp -float( sa_temp) - float(sc_temp)))
            write_table.append(sd_temp)            
       #     print(write_table)
            if sb_temp < 0  :
                raise ValueError()
            else:
              #  write_tables.append(write_table)
                write.writerow(write_table)
        pf.close()
    except IndexError:
#  print('number %d parameter is fault'%count)    
        print('Parameter Error')
    except ValueError:
#  print('number %d parameter is fault'%count)
        print("Parameter Error")


