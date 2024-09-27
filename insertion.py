import sys
from countcompares import CountCompares
from countswaps import CountSwaps

class Insert:

    def __init__(self):
        self.insert_list = []
        self.insert_swaps = 0
        self.insert_cmp = 0

    def read_file(self,filename):

        try:
            with open(filename, 'r') as file:
                for line in file:
                    # Convert each line to an integer and append to the list
                    self.insert_list.append(int(line.strip()))
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            exit(1)

    def write_file(self,filename):

        try:
            with open(filename, 'w') as file:
                for num in self.insert_list:
                    file.write(f"{num}" +"\n")
        except IOError:
            print(f"Error writing to '{filename}'")
            exit(1)

    def insertionSort(self):
        i = 1

        # #make a swaps counter that wraps the list
        # swaps_counter = CountSwaps(self.insert_list)
        # #swaps_counter.swaps = 0

        for i in range(1,len(self.insert_list)):
            j = i
            # make an instance of compare counter for the two indexes to be compared
            # but we count compares for the key to be checked, not for both
            # cmp_counter = CountCompares(self.insert_list[j])
            # cmp_counter2 = CountCompares(self.insert_list[j-1])
            self.count_cmp(self.insert_list[j-1], self.insert_list[j])


            while j >= 0 and self.insert_list[j-1] > self.insert_list[j]:

                #self.do_and_count_swap(self.insert_list[j-1], self.insert_list[j])
                self.insert_list[j-1], self.insert_list[j] = self.insert_list[j], self.insert_list[j-1]
                self.insert_swaps+=1
                # self.insert_cmp+=1

                j-=1
            
        print('swaps ', self.insert_swaps)
        print('compares ', self.insert_cmp)

        return self.insert_list, self.insert_cmp, self.insert_swaps
    
    def count_cmp(self, int1, int2):
        if int1 < int2 or int2 < int1:
            self.insert_cmp+=1

    def do_and_count_swap(self, i, j):
        self.insert_list[i], self.insert_list[j] = self.insert_list[j], self.insert_list[i]
        self.insert_swaps+=1
    
    def get_cmp(self):
        return self.insert_cmp
    
    def get_swp(self):
        return self.insert_swaps


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python script.py input_file")
        exit(1)

    input_file = sys.argv[1]
    insert_list = Insert()

    # Read integers from the input file
    insert_list.read_file(input_file)

    # Perform insertion sort
    insert_list.insertionSort()

    # Write sorted integers to a new file
    output_file = input_file.replace(".csv", "_insert.out.csv")

    # Enter your own file path here to ensure easy access
    output_file = '/Users/tiffanylopez/IN2010/Oblig1/' + output_file
    insert_list.write_file(output_file)

    print(f"Sorted integers written to '{output_file}'")

        # teller = 0

        # with open(sys.argv[0], 'r') as file:
        #     lines = file.readlines()

        # new_out_filename = str(sys.argv[0])
        # insert_list = Insert()

        # for line in lines:
        #     teller+=1
        #     line = line.strip().split()
        #     insert_list.insert_list.append(line)

        # #her legger jeg til egen begrensning for 'større' filer
        # #skal ikke skrives ut til ny fil hvis det er flere enn 20 linjer
        # #dette for at rettere må ikke sjekke flere enn 20 linjer ;)
        # if teller < 20:
        #     insert_list.insertionSort(insert_list)
        #     insert_list.write_file()
