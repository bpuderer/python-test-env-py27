"""Split nose/nose2 xunit xml to multiple xmls."""

import argparse
import xml.etree.ElementTree as ET


def write_suite(suite):
    """write individual testsuite XML"""
    suite.attrib['tests'] = str(suite.attrib['tests'])
    suite.attrib['failures'] = str(suite.attrib['failures'])
    suite.attrib['errors'] = str(suite.attrib['errors'])
    suite.attrib['skipped'] = str(suite.attrib['skipped'])
    suite.attrib['time'] = str(suite.attrib['time'])

    # TODO make output location flexible
    filename = 'reports/' + 'TEST-' + suite.attrib['name'] + '.xml'
    ET.ElementTree(suite).write(filename, xml_declaration=True, encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description='split xunit xml')
    parser.add_argument('--infile', '-i', default='reports/nosetests.xml',
                        help='xunit xml from nose or nose2')
    args = parser.parse_args()

    tree = ET.parse(args.infile)
    input_suite = tree.getroot()

    prev_suite_name = ''
    suite = None
    for test_case in input_suite:
        suite_name = '.'.join(test_case.attrib['classname'].split('.')[1:])

        if prev_suite_name != suite_name:
            # first testcase
            if suite is not None:
                write_suite(suite)
            suite = ET.Element('testsuite', attrib={'name': suite_name, 'tests': 0, 'failures': 0,
                                                    'errors': 0, 'skipped': 0, 'time': 0.0})

        suite.append(test_case)
        suite.attrib['tests'] += 1
        suite.attrib['time'] += float(test_case.attrib['time'])
        if len(test_case):
            if test_case[0].tag == 'failure':
                suite.attrib['failures'] += 1
            if test_case[0].tag == 'error':
                suite.attrib['errors'] += 1
            if test_case[0].tag == 'skipped':
                suite.attrib['skipped'] += 1

        prev_suite_name = suite_name

    # write last testsuite
    if suite is not None:
        write_suite(suite)

if __name__ == "__main__":
    main()
