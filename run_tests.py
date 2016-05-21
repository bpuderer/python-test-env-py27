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
    parser.add_argument('--attrib', '-a', nargs='+', help='Args are logically \
                        ORed. Arg with comma delimeters is ANDed. \
                        Ex. slow tags=tag2 Ex. slow,tags=tag2')
    parser.add_argument('--eval_attrib', '-A', nargs='+', help='python expression for attributes')
    parser.add_argument('--quiet', '-quiet', action='store_true', default=False)
    parser.add_argument('--nose2', '-nose2', action='store_true',
                        default=False, help='use nose2 instead of nose')
    parser.add_argument('--xml_out', '-xml_out', action='store_true',
                        default=False, help='write reports/nosetests.xml')
    parser.add_argument('--html_out', '-html_out', action='store_true',
                        default=False, help='write reports/results.html')
    args = parser.parse_args()

    os.environ['PY_TEST_ENV'] = args.testenv

    if args.nose2:
        cmd = 'python -m nose2 --config framework/nose2.cfg'
    else:
        cmd = 'python -m nose --nocapture --nologcapture'
    if not args.quiet:
        cmd += ' -v'
    if args.tests:
        cmd += ' ' + ' '.join(args.tests)
    if args.attrib:
        if args.nose2:
            cmd += ' -A ' + ' -A '.join(args.attrib)
        else:
            cmd += ' -a ' + ' -a '.join(args.attrib)
    if args.eval_attrib:
        if args.nose2:
            cmd += ' -E ' + ' -E '.join(args.eval_attrib)
        else:
            cmd += ' -A ' + ' -A '.join(args.eval_attrib)
    if args.xml_out or args.html_out:
        if args.nose2:
            cmd += ' --junit-xml'
        else:
            cmd += ' --with-xunit --xunit-file reports/nosetests.xml'

    try:
        print subprocess.check_output(shlex.split(cmd))
    except subprocess.CalledProcessError:
        #if any test fails a non-zero exit status is returned
        pass

    if args.html_out and not args.nose2:
        # TODO update script for nose and nose2 xml
        cmd = 'python parse_nosetests.py reports/nosetests.xml --outfile reports/results.html'
        subprocess.call(shlex.split(cmd))

if __name__ == "__main__":
    main()
