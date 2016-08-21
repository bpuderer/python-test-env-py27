"""Wrapper for nose/nose2"""

import argparse
import glob
import os
import shlex
import shutil
import subprocess


def main():
    parser = argparse.ArgumentParser(description='nose/nose2 wrapper script',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--testenv', '-te', default='DEFAULT',
                        help='case sensitive section in test_settings.cfg')
    parser.add_argument('--tests', '-t', nargs='+',
                        help='Ex. tests/test_example.py tests.test_example \
                        tests.test_example:ExampleTestCase.test_str_ends_in_r')
    parser.add_argument('--attr', '-a', nargs='+', help='Args are logically \
                        ORed. Arg with comma delimeters is ANDed. \
                        Ex. slow tags=tag2 Ex. slow,tags=tag2')
    parser.add_argument('--eval_attr', '-A', nargs='+', help='python expression for attributes')
    parser.add_argument('--quiet', '-q', action='store_true', default=False)
    parser.add_argument('--nose2', '-n2', action='store_true',
                        default=False, help='use nose2 instead of nose')
    parser.add_argument('--collect_only', '-c', action='store_true',
                        default=False, help='collect and output test names, don\'t run tests')
    parser.add_argument('--xml', action='store_true',
                        default=False, help='write test results xunit xml')
    parser.add_argument('--html', action='store_true',
                        default=False, help='write test results in HTML using ant JUnitReport')
    args = parser.parse_args()

    os.environ['PY_TEST_ENV'] = args.testenv

    # cleanup previous run's reports
    for f in glob.glob('reports/*.xml'):
        os.remove(f)
    if os.path.isdir('reports/html'):
        shutil.rmtree('reports/html')

    if args.nose2:
        cmd = 'python -m nose2 --config framework/nose2.cfg'
    else:
        cmd = 'python -m nose --nocapture --nologcapture'

    if not args.quiet:
        cmd += ' -v'

    if args.collect_only:
        cmd += ' --collect-only'

    if args.tests:
        cmd += ' ' + ' '.join(args.tests)

    if args.attr:
        if args.nose2:
            cmd += ' -A ' + ' -A '.join(args.attr)
        else:
            cmd += ' -a ' + ' -a '.join(args.attr)

    if args.eval_attr:
        if args.nose2:
            cmd += ' -E ' + ' -E '.join(args.eval_attr)
        else:
            cmd += ' -A ' + ' -A '.join(args.eval_attr)

    if args.xml or args.html:
        if args.nose2:
            cmd += ' --junit-xml'
        else:
            cmd += ' --with-xunit --xunit-file reports/nosetests.xml'

    try:
        print subprocess.check_output(shlex.split(cmd))
    except subprocess.CalledProcessError:
        # if any test fails a non-zero exit status is returned
        pass

    if args.html:
        if args.nose2:
            cmd = 'python -m framework.split_xunitxml --infile reports/nose2-junit.xml'
        else:
            cmd = 'python -m framework.split_xunitxml --infile reports/nosetests.xml'
        subprocess.call(shlex.split(cmd))
        subprocess.call(shlex.split('ant -buildfile buildTestReports.xml'))

if __name__ == "__main__":
    main()
