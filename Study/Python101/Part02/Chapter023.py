# The xml module

'''
minidom
ElementTree
'''

'''
# Working with minidom
import xml.dom.minidom
import urllib.request

class AppParser(object):

    def __init__(self, url, flag='url'):
        self.list = []
        self.appt_list = []
        self.flag = flag
        self.rem_value = 0
        xml = self.getXml(url)
        self.handleXml(xml)

    def getXml(self, url):
        try:
            print(url)
            f = urllib.request.urlopen(url)
        except:
            f = url
        
        doc = xml.dom.minidom.parse(f)
        node = doc.documentElement
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            print('Element name: %s' % node.nodeName)
            for (name, Value) in node.attributes.items():
                print('    Attr -- Name: %s   Value: %s' % (name, Value))
        return node
    
    def  handleXml(self, xml):
        rem = xml.getElementsByTagName('zAppointments')
        appointments = xml.getElementsByTagName("appointment")
        self.handleAppt(appointments)

    def getElement(self, element):
        return self.getText(element.childNodes)
    
    def handleAppt(self, appts):
        for appt in appts:
            self.handleAppt(appt)
            self.list = 90
    
    def handleAppt(self, appt):
        begin = self.getElement(appt.getElementsByTagName('begin')[0])
        duration = self.getElement(appt.getElementsByTagName('duration')[0])
        subject = self.getText(appt.getElementsByTagName('subject')[0])
        location = self.getElement(appt.getElementsByTagName('location')[0])
        uid = self.getText(appt.getElementsByTagName('uid')[0])

        self.list.append(begin)
        self.list.append(duration)
        self.list.append(subject)
        self.list.append(location)
        self.list.append(uid)
        if self.flag == 'file':

            try:
                state = self.getElement(appt.getElementsByTagName("state")[0])
                self.list.append(state)
                alarm = self.getElement(appt.getElementsByTagName("alarmTime")[0])
                self.list.append(alarm)
            except Exception as e:
                print(e)
        
        self.appt_list.append(self.list)
    
    def getText(self, nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc
    
if __name__ == "__main__":
    appt = AppParser("Chapter024_appt.xml")
    print(appt.appt_list)
'''

'''
import xml.dom.minidom as minidom

def getTitles(xml):
    """
    print out all titles found in xml
    """
    doc = minidom.parse(xml)
    node = doc.documentElement
    books = doc.getElementsByTagName("book")

    titles = []
    for book in books:
        titleobj = book.getElementsByTagName("title")[0]
        titles.append(titleobj)

    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print(node.data)

if __name__ == "__main__":
    document = 'Chapter024_example.xml'
    getTitles(document)
'''

'''
# Parsing with ElementTree
# How to Create XML with ElementTree

import xml.etree.ElementTree as xml

def createXML(filename):
    """
    Create an example XML file
    """
    root = xml.Element("zAppointments")
    appt = xml.Element("appointment")
    root.append(appt)

    # add appointment children
    begin = xml.SubElement(appt, "begin")
    begin.text = "1181251680"

    uid = xml.SubElement(appt, "uid")
    uid.text = "040000008200E000"

    alarmTime = xml.SubElement(appt, "alarmTime")
    alarmTime.text = "1181572063"

    state = xml.SubElement(appt, "state")

    location = xml.SubElement(appt, "location")

    duration = xml.SubElement(appt, "duration")
    duration.text = "1800"

    subject = xml.SubElement(appt, "subject")
    
    tree = xml.ElementTree(root)
    with open(filename, "w") as fh:
        tree.write(fh)

if __name__ == "__main__":
    createXML(".\Python_study_re\Python101\Part02\Chapter024_appt_2.xml")
'''

'''
# How to Edit XNK with ElementTree

import time
import xml.etree.cElementTree as ET

def editXML(filename):
    """
    Edit an example XML file
    """
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()

    for begin_time in root.iter("begin"):
        begin_time.text = time.ctime(int(begin_time.text))

    tree = ET.ElementTree(root)
    with open(".\Python_study_re\Python101\Part02\Chapter024_example03.xml", "wb") as f:
        tree.write(f)

if __name__ == "__main__":
    editXML(".\Python_study_re\Python101\Part02\Chapter024_example02.xml")
'''
    

# How to Parse XML with ElementTree
import xml.etree.cElementTree as ET

def parseXML(xml_file):
    """
    Parse XML with ElementTree
    """
    tree = ET.ElementTree(file=xml_file)
    print(tree.getroot())
    root = tree.getroot()
    print("tag=%s, attrib=%s" %(root.tag, root.attrib))

    for child in root:
        print(child.tag, child.attrib)
        if child.tag == "appointment":
            for step_child in child:
                print(step_child.tag)
    
    # iterate over the entire tree
    print("-" * 40)
    print("Iterating using a tree iterator")
    print("-" * 40)
    iter_ = tree.getiterator()
    for elem in iter_:
        print(elem.tag)

    # get the information via the children
    print("-" * 40)
    print("Iterating using getchildren()")
    print("-" * 40)
    appointments = root.getchildren()
    for appointment in appointments:
        appt_children = appointment.getchildren()
        for appt_child in appt_children:
            print("%s=%s" %(appt_child.tag, appt_child.text))
        
if __name__ == "__main__":
    parseXML(".\Python_study_re\Python101\Part02\Chapter024_appt.xml")


                                     