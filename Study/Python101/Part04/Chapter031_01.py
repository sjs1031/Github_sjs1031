# Parsing XML with lxml

# How to Parse XML with lxml
# A Refactoring example
# How to Parse XML with lxml.objectify
# How to Create XML with lxml.objectify

import os.path
from lxml import etree, objectify
from icecream import ic
#from pathlib import Path

BASE = os.path.dirname(os.path.abspath(__file__))

#path = Path("C:\\Users\\sjs10\\OneDrive\\git\\My_Codes\\Study_001")
#new_path = path / 'Python_Study_re'/ 'Python101' / 'Part04' / 'data' / 'Chapter031_04_new.xml'

'''
def parseXML(xmlFile):
    """
    Parse the xml
    """
    with open(xmlFile) as fobj:
        xml = fobj.read()

    root = etree.fromstring(xml)

    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + " => " + text)

if __name__ == "__main__":
    #ic (os.path.join(BASE,"data\Chapter031_01_example.xml"))
    parseXML(os.path.join(BASE,"data\Chapter031_01_example.xml"))
'''

'''
# Parsing the Book Example
def parseBookXML(xmlFile):

    with open(xmlFile) as fobj:
        xml = fobj.read()
    
    root = etree.fromstring(xml)

    book_dict = {}
    books = []
    for book in root.getchildren():
        for elem in book.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + ": " + text)
            book_dict[elem.tag] = text
        if book.tag == "book":
            books.append(book_dict)
            book_dict = {}
    return books

if __name__ == "__main__":
    parseBookXML(os.path.join(BASE, "data\Chapter031_02_Book_Example.xml"))
'''

'''
# Parsing XML with lxml.objectify

def parseXML(xmlFile):
    """Parse the XML file"""
    with open(xmlFile) as f:
        xml = f.read()

    root = objectify.fromstring(xml)

    # return attributes in element node as dict
    attrib = root.attrib

    # how to extract element data
    begin = root.appointment.begin
    uid = root.appointment.uid

    # loop over elements and print their tags and text
    for appt in root.getchildren():
        for e in appt.getchildren():
            print("%s => %s" % (e.tag, e.text))
        print()

    # how to changean element's text
    root.appointment.begin = "something else"
    print(root.appointment.begin)

    # how to add a new element
    root.appointment.new_element = "New data"

    # remove the py:pytype stuff
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)
    obj_xml = etree.tostring(root, pretty_print=True)
    print(obj_xml)

    # save your xml
    with open(os.path.join(BASE, ".\data\Chapter031_04_new.xml"), "wb") as f:
        f.write(obj_xml)

if __name__ == "__main__":
    #ic(BASE)
    # ic(type(os.path.join(BASE, ".\data\Chapter031_04_new.xml")))
    f = r'.\data\Chapter031_03_example.xml'
    # ic(type(os.path.join(BASE, f)))
    parseXML(os.path.join(BASE, f))
'''

# Creating XML with lxml.objectify

from lxml import etree, objectify

def create_appt(data):
    """
    Create an appointment XML element
    """
    appt = objectify.Element("appointment")
    appt.begin = data["begin"]
    appt.uid = data["uid"]
    appt.alarmTime = data["alarmTime"]
    appt.state = data["state"]
    appt.location = data["location"]
    appt.duration = data["duration"]
    appt.subject = data["subject"]
    return appt

def create_xml():
    """
    Create an XML file
    """
    #xml = '''<?xml version="1.0" encoding="UTF-8"?><zAppointments></zAppointments>'''
    xml = u'<?xml version="1.0" encoding="UTF-8"?><zAppointments></zAppointments>'
    xml = bytes(bytearray(xml, encoding='utf-8'))
    root = objectify.fromstring(xml)
    root.set("reminder", "15")

    appt = create_appt({"begin":1191251680,
                        "uid":"0400000008200E000",
                        "alarmTime":1181572063,
                        "state":"",
                        "location":"",
                        "duration":"1800",
                        "subject":"Bring pizza home"}
                        )
    root.append(appt)

    uid = "604f4792-eb89-478b-a14f-dd34d3cc6c21-1234360800"
    appt = create_appt({"begin":123460800,
                        "uid":uid,
                        "alarmTime":1181572063,
                        "state":"",                        
                        "location":"",
                        "duration":"1800",
                        "subject":"Check MS Office website for updates"}
                        )
    root.append(appt)

    # remove lxml annotation
    objectify.deannotate(root)
    etree.cleanup_namespaces(root)

    # create the xml string
    obj_xml = etree.tostring(root, pretty_print=True, xml_declaration=True)
    #ic (BASE)
    #ic (os.path.join(BASE, ".\data\Chapter031_05_example.xml"))
    #ic (type(os.path.join(BASE, ".\data\Chapter031_05_example.xml")))
    #ic(str(new_path))
    #ic(type(new_path))
    
    #with open(str(new_path), "wb") as xml_writer:
    #        xml_writer.write(obj_xml)
    with open(os.path.join(BASE, ".\data\Chapter031_05_example.xml"), "wb") as xml_writer:
            xml_writer.write(obj_xml)
    #except IOError:
    #    pass
    #'''

if __name__ == "__main__":
    create_xml()