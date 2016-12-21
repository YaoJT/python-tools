##import pandas as pd
##import numpy as np
from sklearn import linear_model
##import matplotlib.pyplot as plt


if __name__ == '__main__':
    ff = open('data.txt').readlines()
    out_f = open('result_TCE10281.csv','w+')
    try:
        ff.remove('\n')
    except:
        None
    data_lst = [x.replace('\n','').split() for x in ff]
    index = [x[0] for x in data_lst[1:]]
    column = data_lst[0][1:]
    out_f.write('index,real,predict\n')
    data_lst1 = data_lst[1:]
    data_lst2 = [x[1:] for x in data_lst1]
    for i in range(len(data_lst2)):
        for j in range(len(data_lst2[i])):
            data_lst2[i][j] = float(data_lst2[i][j]) 

##    df = pd.DataFrame(data_lst2,index = index, columns = column)

    clf = linear_model.LinearRegression()
    clf.fit_intercept = False
    
    out_lst = [[],[]]
    for i in range(len(data_lst2)):
        out_f.write(index[i]+',')
        real_row = data_lst2[i]
        real_X = real_row[:len(column)-1]
        real_y = real_row[len(column)-1]
        fit_rows = [data_lst2[x] for x in range(len(data_lst2)) if x != i]
        fit_X = [x[:len(column)-1] for x in fit_rows]
        fit_y = [x[len(column)-1] for x in fit_rows]
        clf.fit(fit_X,fit_y)
        pre_y = clf.predict(real_X)
        out_lst[0].append(real_y)
        out_lst[1].append(pre_y)
        out_f.write(str(real_y)+',')
        out_f.write(str(pre_y)+'\n')
    out_f.close()
        
        
    
        
        
    
        
    
