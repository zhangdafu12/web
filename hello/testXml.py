from xml.etree import ElementTree as ET
import time
import pymysql
from flask import render_template

STRINGS = "<xs:element name='Name'/>\n\
<xs:complexType>\n\
<xs:sequence>\n\
<xs:element name='A11'/>\n\
<xs:complexType>\n\
<xs:sequence>\n\
<xs:element name='A21'/>\n\
<xs:complexType>\n\
<xs:sequence>\n\
<xs:element name='A31' type='xs:string'/>\n\
<xs:element name='A32' type='xs:string'/>\n\
</xs:sequence>\n\
</xs:complexType>\n\
<xs:element name='A22' type='xs:string'/>\n\
</xs:sequence>\n\
</xs:complexType>\n\
<xs:element name='A12' type='xs:string'/>\n\
</xs:sequence>\n\
</xs:complexType>\n"


def writeXMLPoints(string, hangye):
    timeTick = str(int(time.time()))
    xmlPoints = []
    lastNames = []
    addStrings = []
    ceng = 1
    strings = string.split('\n')
    Name = strings[0][strings[0].find("=") + 2:strings[0].find("/") - 1]
    """for i in range(len(strings)-4):
        if strings[i+3].find("name") != -1 and strings[i+3].find("type") != -1: # 这种情况就是满足单个节点的
            name = strings[i+3][int(strings[i+3].find("name"))+6:int(strings[i+3].find("type"))-2]
            type = strings[i+3][int(strings[i+3].find("type"))+9:int(strings[i+3].find("/"))-1]
            xmlPoints.append((ceng,name,type))
        if strings[i+3].find("sequence") != -1 and strings[i+3].find("/") == -1:
            ceng += 1
        if strings[i+3].find("sequence") != -1 and strings[i+3].find("/") != -1:
            ceng -= 1
        if strings[i + 3].find("name") != -1 and strings[i+3].find("type") == -1:
            name = strings[i+3][int(strings[i+3].find("name"))+6:int(strings[i+3].find("/"))-1]
            xmlPoints.append((ceng, name, 'complexType'))"""

    for i in range(-3, len(strings) - 4):
        strings[i + 3] = strings[i + 3].replace("xs:", "")
        strings[i + 3] = strings[i + 3].replace("'", "", 2)
        # strings[i + 3] = strings[i + 3].replace(":", "=")
        # strings[i + 3] = strings[i + 3].replace(" ", "")
        if strings[i + 3].find("element") != -1:
            strings[i + 3] = strings[i + 3].replace("element ", "")
        if strings[i + 3].find("name=") != -1:
            strings[i + 3] = strings[i + 3].replace("name=", "")
        # print(strings[i + 3])
        if i < len(strings) - 4 - 2:
            if strings[i + 4].find("complexType") != -1 and strings[i + 5].find("sequence") != -1 and\
                    strings[i+4].find("/") == -1 and strings[i+5].find("/") == -1:
                indexTemp = strings[i + 3].find("/")
                lastNames.append("</" + strings[i + 3][1:indexTemp] + ">")
                addString = strings[i + 3][0:indexTemp] + " type='complexType'>"
                addStrings.append(addString)
                i = i + 2
        if i < len(strings) - 4 - 2:
            if strings[i + 4].find("complexType") != -1 and strings[i + 3].find("sequence") != -1 and\
                    strings[i+3].find("/") != -1 and strings[i+4].find("/") != -1:
                lastNamesMax = len(lastNames)
                addStrings.append(lastNames[lastNamesMax-1])
                del lastNames[lastNamesMax-1]
                i = i + 1

        if strings[i + 3].find("type") != -1:
            addStrings.append(strings[i + 3])
    print(addStrings)
    # addStrings = "<?xml version='1.0' encoding='gb2312'?>\n" + addStrings
    with open(timeTick + ".xml", "a+") as f:
        f.write("<?xml version='1.0' encoding='gb2312'?>\n")
    for add in addStrings:
        with open(timeTick+".xml", "a+") as f:
            f.write(add)
            f.write("\n")
    sql = "INSERT INTO xml(id,xml,hangye)VALUES ('%s', '%s', '%s')" % \
          (timeTick, timeTick, hangye)
    print(sql)
    db = pymysql.connect("localhost", "root", "123456", "translation")
    cursor = db.cursor()
    # SQL 插入语句
    try:
        # 执行sql语句
        c = cursor.execute(sql)
        db.commit()
        print("操作完成!")
        return render_template('page2.html')
    except Exception as e:
        print(e)
    return render_template('page2.html')

