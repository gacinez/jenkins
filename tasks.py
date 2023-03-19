import os
from invoke import task


GLOBAL_VAR1 = os.environ.get('GLOBAL_VAR1', 'GLOBAL_VAR1_from_invoke_task')
ANOTHER_GLOBAL = os.environ.get('ANOTHER_GLOBAL', 'ANOTHER_GLOBAL_from_invoke_task')
OUTPUT_DIR = 'output'
TEST_DIR = 'tests'


def make_string_with_params():
    robo_string = 'robot'
    robo_string += f' --outputdir {OUTPUT_DIR}'
    robo_string += f' --variable GLOBAL_VAR1:{GLOBAL_VAR1}'
    robo_string += f' --variable ANOTHER_GLOBAL:{ANOTHER_GLOBAL}'
    robo_string += f' {TEST_DIR}'
    return robo_string


@task
def robot(c):
    command = make_string_with_params()
    c.run(command)
