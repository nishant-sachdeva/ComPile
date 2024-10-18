# Take file - data_list.txt

# for every row in file, split by spaces/Tabs
# Take last element
# Add core path to it
# save output of list in new file


# Define the core path to be added
ir_source_path = "/Pramana/ML_LLVM_Tools/IR2Vec_data/train/"

# Open the input and output files
with open('data_list.txt', 'r') as input_file, open('ir_paths.txt', 'w') as output_file:
    for line in input_file:
        # Strip leading/trailing whitespace and check if the line is not empty
        line = line.strip()
        if line:
            # Split the line by any whitespace (spaces or tabs)
            elements = line.split()
            # Get the last element from the split line
            last_element = elements[-1]
            # Concatenate the core path with the last element
            new_line = ir_source_path + last_element
            # Write the new line to the output file
            output_file.write(new_line + '\n')
