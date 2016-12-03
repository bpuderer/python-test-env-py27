"""Split nose/nose2 xunit xml to multiple xmls"""

import argparse
import os.path
import xml.etree.ElementTree as ET


def write_suite(suite, outpath):
    """write individual testsuite XML"""
    filename = 'TEST-' + suite.attrib['name'] + '.xml'
    full_path = os.path.join(outpath, filename)
    ET.ElementTree(suite).write(full_path, xml_declaration=True, encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description='split xunit xml')
    parser.add_argument('infile', help='xunit xml from nose or nose2')
    args = parser.parse_args()

    # write to same location as infile
    outpath = os.path.dirname(args.infile)
    tree = ET.parse(args.infile)
    input_suite = tree.getroot()

    prev_suite_name = ''
    suite = None
    for test_case in input_suite:
        suite_name = '.'.join(test_case.attrib['classname'].split('.')[1:])

        if prev_suite_name != suite_name:
            # first testcase
            if suite is not None:
                write_suite(suite, outpath)
            suite = ET.Element('testsuite', attrib={'name': suite_name, 'tests': '0', 'failures': '0',
                                                    'errors': '0', 'skipped': '0', 'time': '0.0'})

        suite.append(test_case)
        suite.attrib['tests'] = str(int(suite.attrib['tests']) + 1)
        suite.attrib['time'] = str(float(suite.attrib['time']) + float(test_case.attrib['time']))
        if len(test_case):
            if test_case[0].tag == 'failure':
                suite.attrib['failures'] = str(int(suite.attrib['failures']) + 1)
            if test_case[0].tag == 'error':
                suite.attrib['errors'] = str(int(suite.attrib['errors']) + 1)
            if test_case[0].tag == 'skipped':
                suite.attrib['skipped'] = str(int(suite.attrib['skipped']) + 1)

        prev_suite_name = suite_name

    # write last testsuite
    if suite is not None:
        write_suite(suite, outpath)

if __name__ == "__main__":
    main()
