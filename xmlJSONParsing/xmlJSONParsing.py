from lxml import html
import json

# 1
    # Found in xmlTree.png in root

# 2
    # university.xml file in root
xmlFile = html.document_fromstring(open('university.xml', 'r').read())
print("2) XML tree:\n", html.tostring(xmlFile, encoding ='unicode'), "\n")

# 3
print("3) studentIDs for people in class using xml:")
for i in xmlFile.xpath('//*/student[contains(courses,"class")]/studentid'):
    print(i.text_content())
print()

# 4
    # university.json file in root
jsonFile = json.load(open('university.json', 'r'))
print("4) JSON tree:\n", json.dumps(jsonFile, indent = 4), "\n")

# 5
print("5) studentIDs for people in class using json:\n", jsonFile['html']['body']['university']['students']['student']['courses'.__contains__('class')]['studentid'])