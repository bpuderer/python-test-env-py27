import argparse
from collections import OrderedDict
#import json
import xml.etree.ElementTree as ET


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='xunit xml to html')
    parser.add_argument('xunit_xml')
    parser.add_argument('--outfile', '-outfile', default='results.html')
    args = parser.parse_args()

    tree = ET.parse(args.xunit_xml)
    test_suite = tree.getroot()

    test_results = OrderedDict()
    for test_case in test_suite:

        class_name = test_case.get('classname')
        if class_name not in test_results:
            test_results[class_name] = {'total': 0, 'failures': 0, 'errors': 0, 'skip': 0, 'success': 0, 'tests': []}
        test_results[class_name]['total'] += 1

        temp_test = {'name': test_case.get('name'), 'time': test_case.get('time')}

        # if test_case: generates a FutureWarning
        # limitation: only checking first element under test case
        # not reporting system-err message
        if len(test_case) and (test_case[0].tag == 'failure' or test_case[0].tag == 'error' or test_case[0].tag == 'skipped'):
            non_success = test_case[0]
            temp_test['message'] = non_success.get('message')
            temp_test['type'] = non_success.get('type')
            temp_test['text'] = non_success.text
            if non_success.tag == 'failure':
                test_results[class_name]['failures'] += 1
                temp_test['result'] = 'Failed'
            elif non_success.tag == 'error':
                test_results[class_name]['errors'] += 1
                temp_test['result'] = 'Error'
            elif non_success.tag == 'skipped':
                test_results[class_name]['skip'] += 1
                temp_test['result'] = 'Skipped'
        else:
            test_results[class_name]['success'] += 1
            temp_test['result'] = 'Passed'
        test_results[class_name]['tests'].append(temp_test)

    #DEBUG
    #print json.dumps(dict(test_results), indent=4)


    # write html
    with open(args.outfile, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n')
        f.write('  <head>\n')
        f.write('    <title>Test Results</title>\n')
        f.write('  </head>\n')
        f.write('  <body>\n')

        # Summary
        f.write('    <h1>Summary</h1>\n')
        f.write('    <table border="1">\n')
        f.write('      <tr>\n')
        f.write('        <td>Class</td>\n')
        f.write('        <td>Fail</td>\n')
        f.write('        <td>Error</td>\n')
        f.write('        <td>Skip</td>\n')
        f.write('        <td>Success</td>\n')
        f.write('        <td>Total</td>\n')
        f.write('      </tr>\n')
        for test_class, data in test_results.iteritems():
            f.write('      <tr>\n')
            f.write('        <td><a href="#' + test_class + '">' + test_class + '</a></td>\n')
            f.write('        <td>' + str(data['failures']) + '</td>\n')
            f.write('        <td>' + str(data['errors']) + '</td>\n')
            f.write('        <td>' + str(data['skip']) + '</td>\n')
            f.write('        <td>' + str(data['success']) + '</td>\n')
            f.write('        <td>' + str(data['total']) + '</td>\n')
            f.write('      </tr>\n')
        success = int(test_suite.get('tests')) - int(test_suite.get('failures')) - int(test_suite.get('errors')) - int(test_suite.get('skip'))
        f.write('      <tr>\n')
        f.write('        <td>Total</td>\n')
        f.write('        <td>' + test_suite.get('failures') + '</td>\n')
        f.write('        <td>' + test_suite.get('errors') + '</td>\n')
        f.write('        <td>' + test_suite.get('skip') + '</td>\n')
        f.write('        <td>' + str(success) + '</td>\n')
        f.write('        <td>' + test_suite.get('tests') + '</td>\n')
        f.write('      </tr>\n')
        f.write('    </table>\n')

        # Failures
        f.write('    <h1>Failures</h1>\n')
        for test_class, data in test_results.iteritems():
            if data['failures']:
                f.write('    <h2>' + test_class + ' (' + str(data['failures']) + ' failures)</h2>\n')
                for test in data['tests']:
                    if test['result'] == 'Failed':
                        # TODO move to function
                        f.write('    <h3>' + test['name'] + '</h3>\n')
                        f.write('    <ul style="list-style-type:none">\n')
                        f.write('      <li>' + test['type'] + '</li>\n')
                        f.write('      <li>' + test['message'] + '</li>\n')
                        f.write('      <li>' + test['text'].rstrip() + '</li>\n')
                        f.write('    </ul>\n')

        # Errors
        f.write('    <h1>Errors</h1>\n')
        for test_class, data in test_results.iteritems():
            if data['errors']:
                f.write('    <h2>' + test_class + ' (' + str(data['errors']) + ' errors)</h2>\n')
                for test in data['tests']:
                    if test['result'] == 'Error':
                        # TODO refactor
                        f.write('    <h3>' + test['name'] + '</h3>\n')
                        f.write('    <ul style="list-style-type:none">\n')
                        f.write('      <li>' + test['type'] + '</li>\n')
                        f.write('      <li>' + test['message'] + '</li>\n')
                        f.write('      <li>' + test['text'].rstrip() + '</li>\n')
                        f.write('    </ul>\n')

        # Skipped
        f.write('    <h1>Skipped</h1>\n')
        for test_class, data in test_results.iteritems():
            if data['skip']:
                f.write('    <h2>' + test_class + ' (' + str(data['skip']) + ' skipped)</h2>\n')
                for test in data['tests']:
                    if test['result'] == 'Skipped':
                        # TODO refactor
                        f.write('    <h3>' + test['name'] + '</h3>\n')
                        f.write('    <ul style="list-style-type:none">\n')
                        f.write('      <li>' + test['type'] + '</li>\n')
                        f.write('      <li>' + test['message'] + '</li>\n')
                        f.write('      <li>' + test['text'].rstrip() + '</li>\n')
                        f.write('    </ul>\n')

        # All Tests
        f.write('    <h1>All Tests</h1>\n')
        for test_class, data in test_results.iteritems():
            f.write('    <h2><a name="' + test_class + '">' + test_class + '</a></h2>\n')
            f.write('    <ul style="list-style-type:none">\n')
            for test in data['tests']:
                if test['result'] == 'Passed':
                    f.write('      <li><font color="green">' + test['name'] + '</font></li>\n')
                elif test['result'] == 'Failed' or test['result'] == 'Error':
                    f.write('      <li><font color="red">' + test['name'] + '</font></li>\n')
                elif test['result'] == 'Skipped':
                    f.write('      <li><strike>' + test['name'] + '</strike></li>\n')
            f.write('    </ul>\n')

        f.write('  </body>\n')
        f.write('</html>\n')
