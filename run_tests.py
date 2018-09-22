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
    parser.add_argument('tests', nargs='*',
                        help='Only run specified tests. Ex. tests.test_example \
                        Ex. tests.test_example:ExampleTestCase.test_str_ends_in_r \
                        Ex. tests/test_example.py')
    parser.add_argument('--testenv', '-te', default='DEFAULT',
                        help='Case sensitive section in test_settings.cfg')
    parser.add_argument('--attr', '-a', nargs='+', help='Select tests by attribute. \
                        Args are logically OR\'d. Arg with comma delimeter(s) is AND\'d. \
                        Ex. slow tags=tag2 Ex. slow,tags=tag2')
    parser.add_argument('--eval_attr', '-A', nargs='+', help='Select tests where python expression \
                        for attributes evaluates to True')
    parser.add_argument('--quiet', '-q', action='store_true', default=False)
    parser.add_argument('--nose2', '-n2', action='store_true',
                        default=False, help='Use nose2 instead of nose which is in maintenance mode')
    parser.add_argument('--collect_only', '-c', action='store_true',
                        default=False, help='Collect and output test names, don\'t run tests')
    parser.add_argument('--xml', action='store_true',
                        default=False, help='Write test results xUnit XML')
    parser.add_argument('--html', action='store_true',
                        default=False, help='Write test results in HTML using ant JUnitReport')
    args = parser.parse_args()

    os.environ['PY_TEST_ENV'] = args.testenv

    # cleanup previous run
    for f in glob.glob('reports/*.xml'):
        os.remove(f)
    for f in glob.glob('log/*'):
        os.remove(f)
    for f in glob.glob('screenshots/*'):
        os.remove(f)
    if os.path.isdir('reports/html'):
        shutil.rmtree('reports/html')

    if args.nose2:
        cmd = 'python -m nose2 --config framework/nose2.cfg'
    else:
        cmd = 'python -m nose --nocapture --nologcapture'

    if args.tests:
        cmd += ' ' + ' '.join(args.tests)

    if not args.quiet:
        cmd += ' -v'

    if args.collect_only:
        cmd += ' --collect-only'

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
    except subprocess.CalledProcessError as e:
        print e.output

    if args.html:
        if args.nose2:
            cmd = 'python -m framework.split_xunitxml reports/nose2-junit.xml'
        else:
            cmd = 'python -m framework.split_xunitxml reports/nosetests.xml'
        subprocess.call(shlex.split(cmd))
        subprocess.call(shlex.split('ant -buildfile buildTestReports.xml'))

if __name__ == "__main__":
    main()
