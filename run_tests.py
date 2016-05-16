"""Wrapper for nosetests which sets env vars for test config."""

import argparse
import os
import shlex
import subprocess


def main():
    parser = argparse.ArgumentParser(description='nose wrapper script')
    parser.add_argument('--testenv', '-testenv', default='DEFAULT',
                        help='case sensitive section in test_settings.cfg')
    parser.add_argument('--tests', '-tests', nargs='+',
                        help='Ex. tests/test_example.py tests.test_example \
                        tests.test_example:ExampleTestCase.test_str_ends_in_r')
    parser.add_argument('--quiet', '-quiet', action='store_true', default=False)
    parser.add_argument('--xml_out', '-xml_out', action='store_true',
                        default=False, help='write reports/nosetests.xml')
    parser.add_argument('--html_out', '-html_out', action='store_true',
                        default=False, help='write reports/results.html')
    args = parser.parse_args()

    os.environ['PY_TEST_ENV'] = args.testenv
    #the subprocess call uses PYTHONPATH not sys.path
    #sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    os.environ['PYTHONPATH'] = os.path.dirname(os.path.abspath(__file__))

    cmd = 'nosetests --nocapture --nologcapture'
    if not args.quiet:
        cmd += ' -v'
    if args.tests:
        cmd += ' ' + ' '.join(args.tests)
    if args.xml_out or args.html_out:
        cmd += ' --with-xunit --xunit-file reports/nosetests.xml'

    try:
        print subprocess.check_output(shlex.split(cmd))
    except subprocess.CalledProcessError:
        #if any test fails a non-zero exit status is returned
        pass

    if args.html_out:
        cmd = 'python parse_nosetests.py reports/nosetests.xml --outfile reports/results.html'
        subprocess.call(shlex.split(cmd))

if __name__ == "__main__":
    main()
