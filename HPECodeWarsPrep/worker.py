import datetime
import os
import sys

from subprocess import run, TimeoutExpired, CalledProcessError

###
### YOU MIGHT NEED TO CHANGE THE FOLLOWING
### --------------------------------------
### This program assumes that the program under test is called 'probXX.py' where XX is the problem id
### This program assumes that the input data is under the subdirectory called 'input'
### If you run any python program by just doing: python, instead of python3, ... also change the first argument of
### run([...]), to reflect either 'python' or 'python3' accordingly.
###
### Run this program by doing:
### $ python3 worker.py [problem_no] [input_dir]
###

# get problem file from prob no.
prob_id = sys.argv[1]
prog_under_test = f'prob{prob_id}.py'

# get problem directory
input_dir = ''
if len(sys.argv) > 2:
    input_dir = sys.argv[2]
problem_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_dir)
print(problem_dir)

results = []

# function definition to run 1 test case of prog_under_test
def run_one(input, expected_output):
    print(f"Input: {input}")
    print("Output:")
    print(expected_output)
    print()

    res = 0
    seconds = 0.0
    try:
        # run prog_under_test using run()
        start = datetime.datetime.now()
        proc = run(['python3', prog_under_test], capture_output=True, input=input, timeout=10, check=True, text=True) 
        delta = datetime.datetime.now() - start
        seconds = delta.total_seconds()

        # if there is an output
        if proc.stdout:
            output = proc.stdout.split('\n')
            # if there is a trailing new line
            if len(output) and output[-1] == '': output = output[:-1]
            # print test output & expected output
            print("Test")
            print("-------")
            for x in output: print(f"[{x}]")
            print("-------")
            print("Expected")
            print("-------")
            for x in expected_output: print(f"[{x}]")
            print("-------")

            # if the lengths of the output dont match
            if len(output) != len(expected_output):
                res = -3
            else:
                # compares each output line
                for x, y in zip(output, expected_output):
                    if x != y:
                        res = -3
                        break
            # print result of test case
            results.append("Accepted" if res == 0 else "Wrong Answer")
        else:
            results.append("No output produced.  Wrong Answer")
            res = -3
    # timeout error
    except TimeoutExpired:
        res = -1
        results.append("Time Limit Exceeded")
    # runtime error
    except CalledProcessError as proc:
        res = -2
        results.append(f"Runtime Error: {proc.stderr}" if proc.stderr else "Runtime Error")
    return res, seconds

# checks through all files in problem directory
for filename in os.listdir(problem_dir):
    # ignores all files that are not "prob..."
    if not filename.startswith(f'prob{prob_id}'): continue

    # if output file found
    if filename.find('out') >= 0:
        # get expected output
        with open(f"{problem_dir}/{filename}") as f:
            expected_output = [line.rstrip() for line in f]

        # get corresponding input
        input_file = filename.replace('out', 'in')
        if os.path.isfile(f"{problem_dir}/{input_file}"):
            input = None
            with open(f"{problem_dir}/{input_file}") as f:
                input = f.read()

        # run the program with the input & expected output
        res, seconds = run_one(input, expected_output)
        if res != 0:
            break

print("===========")
print("  OVERALL")
print("===========")
for i, r in enumerate(results):
    print(f"Test Case {i+1}:", r)