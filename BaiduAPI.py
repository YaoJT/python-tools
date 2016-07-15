## encoding: utf-8
## this script is used to write the json result from Baidu API to excel file

ak = 'your key of Baidu api'
city = ['北京']
query = ['农业园','农业园区','种植园','养殖场']
xls_file = 'g:/Beijing/data/survey'
xls_name = 'point2.xls'
title = ['name','lat','lng','address','telephone','uid']

import urllib,json,xlwt,os

if os.path.exists(xls_file) == False:
    os.makedirs(xls_file)

wb = xlwt.Workbook()
for c in city:
    for q in query:
        print c+': '+q
        ws = wb.add_sheet(c.decode('utf-8')+'_'+q.decode('utf-8'))
        for t in range(len(title)):
            ws.write(0,t,title[t])
        row = 1        
        for i in range(1000):
            url = 'http://api.map.baidu.com/place/v2/search?query='+q+'&page_size=10&page_num='+str(i)+'&scope=1&region='+c+'&output=json&ak='+ak
##            print url
            aa = urllib.urlopen(url)
            text = json.loads(aa.read())
            if len(text['results']) == 0:
                break
            else:
                for r in text['results']:
                    for t in range(len(title)):
                        try:
                            ws.write(row,t,r[title[t]])
                        except:
                            try:
                                ws.write(row,t,r['location'][title[t]])
                            except:
                                ws.write(row,t,'None')
                    print r['name']+' has been succesfully recoded'
                    row += 1
                print 'total '+str(row)+' of results of {0} in city {1} has been recoded'.format(q,c)
wb.save(os.path.join(xls_file,xls_name))
        



