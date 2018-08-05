#_*_  coding:utf8 _*_
#!/usr/bin/env python3
import sys
import csv

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
   # return work_num,origin_salary
if __name__ == "__main__":
#    print(sys.argv[1])
    c= salary_get(sys.argv[1])   
    print(c)
