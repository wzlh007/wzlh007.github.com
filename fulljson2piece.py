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

def value2color(value):
    d1 = (255-232)/5
    d2 = (255-57)/5
    d3 = (255-41)/5
    d4 = (255-22)/4
    d5 = (255-94)/4
    d6 = (255-131)/4
    if(value<=-7):
        return [22,94,131,255]
    elif(value<=-4):
        return [22+d4,94+d5,131+d6,255]
    elif(value<=-2):
        return [22+d4*2,94+d5*2,131+d6*2,255]
    elif(value<=-1):
        return [22+d4*3,94+d5*3,131+d6*3,255]
    elif(value<=0):
        return [255,255,255,255]
    elif(value<=1):
        return [232+4*d1,57+4*d2,41+4*d3,255]
    elif(value<=2):
        return [232+3*d1,57+3*d2,41+3*d3,255]
    elif(value<=4):
        return [232+2*d1,57+2*d2,41+2*d3,255]
    elif(value<=5):
        return [232+d1,57+d2,41+d3,255]
    else:
        return [232,57,41,255]
    
def value2color2(value):
    d1 = (255-232)/5
    d2 = (255-57)/5
    d3 = (255-41)/5
    d4 = (255-22)/4
    d5 = (255-94)/4
    d6 = (255-131)/4
    if(value<=1):
        return [22,94,131,255]
    elif(value<=2):
        return [22+d4,94+d5,131+d6,255]
    elif(value<=3):
        return [22+d4*2,94+d5*2,131+d6*2,255]
    elif(value<=4):
        return [22+d4*3,94+d5*3,131+d6*3,255]
    elif(value<=5):
        return [255,255,255,255]
    elif(value<=6):
        return [232+4*d1,57+4*d2,41+4*d3,255]
    elif(value<=7):
        return [232+3*d1,57+3*d2,41+3*d3,255]
    elif(value<=8):
        return [232+2*d1,57+2*d2,41+2*d3,255]
    elif(value<=9):
        return [232+d1,57+d2,41+d3,255]
    else:
        return [232,57,41,255]

    
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
czml = [{"id" : "document","name" : "fulldata pieces","version" : "1.0"}]
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
for i in range(0, rownum):
    ##开始
    if(lists[i]["gridID"]!=num):
        entity = {}
        entity["id"] = str(lists[i]["gridID"])
        entity["name"] = 'grid'+str(lists[i]["gridID"])
        print entity["name"]
        entity["availability"] = starttime+'/'+endtime
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

        rgba = []
        rgba.append(lists[i]["time"])
        rgb = value2color2(lists[i]["avgEmoValue"])
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
		
        height = {}
        number = []
        number.append(lists[i]["time"])
        number.append(lists[i]["weiboCount"]*100+1000)
        height["number"] = number
        rectangle["height"] = height
        entity["rectangle"] = rectangle
        num=num+1
    ##中间添加
    else:
        rgba.append(lists[i]["time"])
        rgb = value2color2(lists[i]["avgEmoValue"])
        rgba.append(rgb[0])
        rgba.append(rgb[1])
        rgba.append(rgb[2])
        rgba.append(rgb[3])

        rectangle["material"]["solidColor"]["color"]["rgba"] = rgba
        number.append(lists[i]["time"])
        number.append(lists[i]["weiboCount"]*100+1000)
        height["number"] = number
        rectangle["height"] = height
        entity["rectangle"] = rectangle
        if(i+1<rownum):
            if(lists[i]["gridID"]!=lists[i+1]["gridID"]):
                ##最后一天
                czml.append(entity)
            else:
                print '中间'
                ##中间
        else:
            czml.append(entity)
##print czml
s3 = json.dumps(czml)
##print s3
##创建新文件
fileout = 'fulldataPieces2.czml'
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


