def numToRomanNum(num):
    """translate num from 1 to 3999 to roman num"""
    numDic = {
        0:'',
        1:u'\u2160',
        2:u'\u2161',
        3:u'\u2162',
        4:u'\u2163',
        5:u'\u2164',
        6:u'\u2165',
        7:u'\u2166',
        8:u'\u2167',
        9:u'\u2168'
        }
    numDic_10 = {
        0:'',
        1:u'\u2169',
        2:u'\u2169\u2169',
        3:u'\u2169\u2169\u2169',
        4:u'\u2169\u216C',
        5:u'\u216C',
        6:u'\u216C\u2169',
        7:u'\u216C\u2169\u2169',
        8:u'\u216C\u2169\u2169\u2169',
        9:u'\u2169\u216D'
        }
    numDic_100 = {
        0:'',
        1:u'\u216D',
        2:u'\u216D\u216D',
        3:u'\u216D\u216D\u216D',
        4:u'\u216D\u216E',
        5:u'\u216E',
        6:u'\u216E\u216D',
        7:u'\u216E\u216D\u216D',
        8:u'\u216E\u216D\u216D\u216D',
        9:u'\u216D\u216F'
        }
    numDic_1000 = {
        0:'',
        1:u'\u216F',
        2:u'\u216F\u216F',
        3:u'\u216F\u216F\u216F'
        }
    try:
        num_1000,mod = divmod(num,1000)
        num_100,mod = divmod(mod,100)
        num_10,mod = divmod(mod,10)
        out_str = numDic_1000[num_1000]+numDic_100[num_100]+numDic_10[num_10]+numDic[mod]
        return out_str
    except:
        return 'Please input a integer num Between 1-3999'
