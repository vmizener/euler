#!/usr/bin/env python3
import argparse
import importlib
import os
import pprint
import sys
import time

PROBLEMSDIR = 'src/problems'
PROBLEMFILE = 'main.py'
PROBLEMCALL = 'main'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run known ProjectEuler solutions.")
    parser.add_argument('problems', metavar='P', type=int, nargs='*',
            help="Which problem(s) to run solutions for.  Will run in the order received (skipping dupliates and unimplemented solutions).")
    parser.add_argument('--list', dest='checklist', action='store_true',
            help="List all known problem solutions instead of running anything.")

    args = parser.parse_args()
    problems = os.listdir(PROBLEMSDIR)
    if args.checklist:
        print('Known problems:')
        for problem in sorted(problems):
            print(int(problem), end=' ', flush=True)
        quit(0)
    problem_map = {int(problem.replace('p', '')): problem for problem in problems}
    seen = set()
    for arg in args.problems:
        arg = int(arg)
        print('/============================================================')
        print(' PROBLEM: {}'.format(arg))
        if arg in seen:
            print(' ... Problem already run.  Skipping.')
            continue
        seen.add(arg)
        if arg not in problem_map:
            print(' ... No implementation for this problem.  Skipping.')
            continue
        os.chdir('{}/{}/{}'.format(os.getcwd(), PROBLEMSDIR, problem_map[arg]))
        module = importlib.import_module('{}.{}.{}'.format(
            PROBLEMSDIR.replace('/', '.'), problem_map[arg], PROBLEMFILE[:-3]))
        if not hasattr(module, 'main'):
            print(' ... No main() function defined for this problem.  Skipping.')
            continue
        start = time.time()
        ret = module.main()
        elapsed = time.time() - start
        print()
        pprint.pprint(ret)
        print()
        minutes, seconds = divmod(elapsed, 60)
        print('Time elapsed: ', end='')
        if minutes > 0:
            print('{}m, '.format(minutes), end='')
        print('{:.8f}s'.format(seconds))
