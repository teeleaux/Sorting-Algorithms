from merge_sort import Merge
from insertion_sort import Insert
import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file")
        exit(1)

    input_file = sys.argv[1]

    merge_instance = Merge()
    insert_instance = Insert()

    # Read the list of integers from the input file
    merge_instance.read_file(input_file)
    insert_instance.read_file(input_file)
    #print('input file: ', input_file)

    t = time.time_ns()
    # Perform merge sort
    merge_instance.mergeSort()

    # Measure time for mergeSort method
    timeus = (time.time_ns() - t /1000)
    print(timeus)

    # Perform and measure time for insertion_sort
    t2 = time.time_ns()
    insert_instance.insertion_sort()
    timeus2 = (time.time_ns() - t2 /1000)
    print(timeus2)

    # Write the sorted list to the output file
    output_file = input_file.replace(".csv", "_merge.out.csv")
    print(output_file)

    output_file2 = input_file.replace(".csv", "_insert.out.csv")
    
    # Enter your own filepath here
    output_file = '/Users/tiffanylopez/IN2010/Oblig1/' + output_file
    output_file2 = '/Users/tiffanylopez/IN2010/Oblig1/' + output_file2

    merge_instance.write_file(output_file)
    insert_instance.write_file(output_file2)

    print(f"Sorted integers written to '{output_file}' and '{output_file2}")
    print(merge_instance.cmp_count)

main()

