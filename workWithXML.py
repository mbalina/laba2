from xml.dom import minidom
import xml.etree.ElementTree as ET


def downloadFromXML():
    tree = ET.parse('point.xml')
    root = tree.getroot()
    kor = []
    kor.append(float(root.find('x').text))
    kor.append(float(root.find('y').text))
    kor.append(float(root.find('z').text))
    speed = []
    speed.append(float(root.find('vx').text))
    speed.append(float(root.find('vy').text))
    speed.append(float(root.find('vz').text))
    return kor, speed

def saveInXml(koor, speed):
    root = ET.Element('point')

    x = ET.SubElement(root, 'x')
    x.text = str(koor[0])
    y = ET.SubElement(root, 'y')
    y.text = str(koor[1])
    z = ET.SubElement(root, 'z')
    z.text = str(koor[2])

    vx = ET.SubElement(root, 'vx')
    vx.text = str(speed[0])
    vy = ET.SubElement(root, 'vy')
    vy.text = str(speed[1])
    vz = ET.SubElement(root, 'vz')
    vz.text = str(speed[2])

    filename = 'point.xml'
    xml_string = ET.tostring(root).decode()

    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
    with open(filename, 'w') as xml_file:
        xml_file.write(xml_prettyxml)
