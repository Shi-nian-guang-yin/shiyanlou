#_*_  coding:utf8 _*_
#!/usr/bin/env python3
import sys
from math import pow
secure = 0.165
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
  
if __name__ == "__main__":
    try:
        count = 1
        peo_list = sys.argv[1:]
        for i in peo_list:
            count = +1        
            middle_i = i.split(':')
            work_num =int( middle_i[0])
            salary = int(middle_i[1])
            if salary < 0  :
                raise ValueError()
            else:
                print("%d:%.2f"%(work_num,((salary -( salary * secure) )-calc_tax(salary))))
    except IndexError:
#  print('number %d parameter is fault'%count)    
        print('Parameter Error')
    except ValueError:
#  print('number %d parameter is fault'%count)
        print("Parameter Error")


