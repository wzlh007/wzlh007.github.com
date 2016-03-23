#!/usr/bin/python
import json
import random
import math
#Function:Analyze json script
#Json is a script can descript data structure as xml, 
#for detail, please refer to "http://json.org/json-zh.html".

#Note:
#1.Also, if you write json script from python,
#you should use dump instead of load. pleaser refer to "help(json)".

#json file:
#The file content of temp.json is:
#{
# "name":"00_sample_case1",
# "description":"an example."
#}
#f = file("temp.json");
#s = json.load(f)
#print s
#f.close

def value2color2(value):
    d = 255/9
    if(value<=4):
        return [0,0,0,150]
    elif(value<=13):
        return [d,d,d,150]
    elif(value<=24):
        return [2*d,2*d,2*d,150]
    elif(value<=35):
        return [3*d,3*d,3*d,150]
    elif(value<=46):
        return [4*d,4*d,4*d,150]
    elif(value<=61):
        return [5*d,5*d,5*d,150]
    elif(value<=79):
        return [6*d,6*d,6*d,150]
    elif(value<=104):
        return [7*d,7*d,7*d,150]
    elif(value<=154):
        return [8*d,8*d,8*d,150]
    else:
        return [255,255,255,150]

    
#json string:
file = 'fullInput.json'
##打开数据文件
fp = open(file,'r')
print type(fp)
##读取数据文件
content = fp.read()
print type(content)
##将str转化为list
lists = json.loads(content)
print type(lists)

##创建cmzl文本
czml = [{"id" : "document","name" : "fulldata bifollow pieces","version" : "1.0"}]
##print type(czml)
##entity = {}
##entity["id"] = "123123"
##print entity
##czml.append(entity)
##print czml[1]["id"]
starttime = '2016-03-17T17:00:00Z'
endtime = '2016-03-18T17:00:00Z'
num = -1
rownum = len(lists)
##rownum = 100
for i in range(0, rownum):
    ##开始
    if(lists[i]["gridID"]!=num):
        entity = {}
        entity["id"] = str(lists[i]["gridID"])
        entity["name"] = 'grid'+str(lists[i]["gridID"])
        print entity["name"]
        
        ##创建rectangle图形
        rectangle = {}
        ##rectangle 的位置坐标
        coordinates = {}
        lon =lists[i]["lon"]
        lat =lists[i]["lat"]
        wsenDegrees = [lon-0.025,lat-0.025,lon+0.025,lat+0.025]
        coordinates["wsenDegrees"] = wsenDegrees
        rectangle["coordinates"] = coordinates
        ##rectangle的样式
        rectangle["outline"] = 0
        rectangle["fill"] = 1
##        rectangle["outlineWidth"] = 4
##        outlineColor = {}
        rgba = []
        rgba.append(lists[i]["time"])
        starttime = lists[i]["time"]
        rgb = value2color2(lists[i]["biFollow"])
        rgba.append(rgb[0])
        rgba.append(rgb[1])
        rgba.append(rgb[2])
        rgba.append(rgb[3])

        color = {}
        solidColor = {}
        material ={}
        color["rgba"] = rgba
        solidColor["color"] = color
        material["solidColor"] = solidColor
        rectangle["material"] = material
		
        entity["rectangle"] = rectangle
        num=num+1
    ##中间添加
    else:
        rgba.append(lists[i]["time"])
        rgb = value2color2(lists[i]["biFollow"])
        rgba.append(rgb[0])
        rgba.append(rgb[1])
        rgba.append(rgb[2])
        rgba.append(rgb[3])
        rectangle["material"]["solidColor"]["color"]["rgba"] = rgba

        entity["rectangle"] = rectangle
        if(i+1<rownum):
            if(lists[i]["gridID"]!=lists[i+1]["gridID"]):
                ##最后一天
                endtime = lists[i]["time"]
                entity["availability"] = starttime+'/'+endtime
                czml.append(entity)
            else:
                print '中间'
                ##中间
        else:
            endtime = lists[i]["time"]
            entity["availability"] = starttime+'/'+endtime
            czml.append(entity)
##print czml
s3 = json.dumps(czml)
##print s3
##创建新文件
fileout = 'fullBifollow.czml'
##打开数据文件
fout = open(fileout,'w')
fout.write(s3)
fout.close();
fp.close()

# print s
# print s.keys()
# print s["name"]
# print s["type"]["name"]
# print s["type"]["parameter"][1]


