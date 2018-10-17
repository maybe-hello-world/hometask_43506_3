from task_1_quicksort import Quicksorter
from helpers.source_generation_helper import SourceGenerationHelper
from task_2_parsing import Parser

# some variables for testing
# Task 1
elements_count: int = 10;
min_possible_value: int = -100
max_possible_value: int = 100
tests_count: int = 5;
#Task 2
input_path = 'log_source/DhcpSrvLog-Thu.log'
output_path = 'parsing_result/result.txt'
event_id = '12'


def process_source(source):
    """

    :param source: a list to process. Could be incorrect value.
    """
    print('')
    print('There is your source list:')
    print(str(source))
    print('Trying to sort it now...')
    result = Quicksorter.quicksort_list(source)
    print('There is your sorted list:')
    print(str(result))
    print('')


def do_task_1():
    print('Task 1: ')
    source_generation_helper = SourceGenerationHelper(min_possible_value, max_possible_value);

    good_source = source_generation_helper.generate_good_source(elements_count)
    process_source(good_source)

    for i in range(tests_count):
        try:
            probably_bad_source = source_generation_helper.generate_any_source(elements_count)
            process_source(probably_bad_source)
        except Exception as e:
            print('There are some problems with your source: ', str(e))


def do_task_2():
    print('')
    parser = Parser(input_path)
    print('Trying to process event with event_id = ' + event_id + ' in the logfile with the path: ' + input_path)
    try:
        parser.process_event(event_id=event_id,output_path=output_path)
        print('Event have been processed. Output path is: ' + output_path)
    except Exception as e:
        print('There are some problems with your logfile: ', str(e))


def main():
    do_task_1()
    do_task_2()


if __name__ == "__main__":
    main()