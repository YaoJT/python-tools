## coding: utf-8
## url = http://api.map.baidu.com/geocoder/v2/?ak=ZLzGo9cxxpMLlKDr8GzMsSfmwZYkmRsS&callback=renderOption&output=json&address=%E5%8C%97%E4%BA%AC%E5%B8%82%E7%99%BE%E5%BA%A6%E5%A4%A7%E5%8E%A6
## renderOption&&renderOption({"status":0,
##                           "result":{"location":{"lng":116.30775539540982,"lat":40.05685561073758},
##                           "precise":1,"confidence":80,"level":"商务大厦"}})

import json,arcpy,urllib
ff = 'h:/soil.mdb/environment'
out_file = open('soil.csv','w+')
out_file.write('SID,place,status,lng,lat,precise,confidence,level,url')
key= '**********' ## your key
cursor = arcpy.SearchCursor(ff)
record = 0
for row in cursor:
    if row.province != None and row.place != None:
        address = row.province + row.place
    elif row.place != None:
        address = row.place
    else:
        out_file.write(row.SID+'\n')
        record += 1
        continue
    try:
        url = 'http://api.map.baidu.com/geocoder/v2/?ak={0}&callback=renderOption&output=json&address={1}'.format(key,address.encode('utf-8'))
        tt = urllib.urlopen(url)
        tt = tt.read().decode('utf-8').replace('renderOption&&renderOption(','').replace(')','')
        res = json.loads(tt)
        if res['status'] == 0:
            out_file.write('{0},{1},{2},{3},{4},{5},{6},{7},{8}\n'.format(row.SID,row.place.encode('utf-8'),res['status'],
                                                                        res['result']['location']['lng'],res['result']['location']['lat'],
                                                                        res['result']['precise'],res['result']['confidence'],res['result']['level'].encode('utf-8'),url))
            print str(record)+address +': ' + str(res['result']['location']['lng']) + ',' + str(res['result']['location']['lat'])
        else:
            out_file.write('{0},{1},{2},{3},{4},{5},{6},{7},{8}\n'.format(row.SID,row.province,row.place,res['status'],
                                                                        '0','0','0','0','0',url))
            print str(record)+address + 'failed: ' + url
        record += 1
    except:
        out_file.write(row.SID+'\n')
        record += 1
        continue

del cursor
out_file.close()
####ff example###########
"""
SID province place
1 山西 晋城市陵川县第二中学
2 北京 天安门
"""
###result###########
"""
SID,place,status,lng,lat,precise,confidence,level,url
1002,华安县城关后山,0,117.54380455,24.9186880946,0,14,区县,http://api.map.baidu.com/geocoder/v2/?ak=ZsSfmwZYkmRsS&callback=renderOption&output=json&address=福建省华安县城关后山
1004,诏安县红星农场,0,117.132941957,23.8740407254,0,14,区县,http://api.map.baidu.com/geocoder/v2/?ak=ZLxpMLlKDr8GzMsSfmwZYkmRsS&callback=renderOption&output=json&address=福建省诏安县红星农场
1006,诏安县汾水关,0,117.087219274,23.6877183971,0,50,UNKNOWN,http://api.map.baidu.com/geocoder/v2/?ak=ZLzGo9cxxpMsS&callback=renderOption&output=json&address=福建省诏安县汾水关
"""
