from datasets import load_dataset, get_dataset_split_names, load_dataset_builder
import subprocess

datasetName = 'llvm-ml/ComPile'
ir_source_path = "/Pramana/ML_LLVM_Tools/IR2Vec_data/train/"

def save_ir(ir, file_path):
    try:
        # Open the file at file_path in write mode
        with open(file_path, 'w') as file:
            # Write the IR text to the file
            file.write(ir)
        print(f"IR saved successfully at {file_path}")
    except IOError as e:
        print(f"An error occurred while saving the IR: {e}")

ir_paths_list = []

def convert_bytecode_to_ir(mod, idx):
    print("Inside convert bytecode function ", idx)

    bytecode = mod['content']
    ir_file_path = ir_source_path + str(idx) + ".ll"
    ir_paths_list.append(ir_file_path)

    dis_command_vector = ['llvm-dis', '-']
    with subprocess.Popen(
        dis_command_vector,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE) as dis_process:

        output = dis_process.communicate(
            input=bytecode
        )[0].decode('utf-8')

        save_ir(output, ir_file_path)

    return mod



### Download dataset into local
full_dataset = load_dataset(datasetName, split='train', streaming=True)

c_cpp_dataset = full_dataset.filter(lambda example: example['language'].startswith('c'))
print("Counting, fetching started")

# Iterate over the dataset
for ix, item in enumerate(c_cpp_dataset):
    print("Working on ", ix, item["package_source"], item["language"])
    convert_bytecode_to_ir(item, ix)
print("Iteration finished")

print("Saving ir paths")
def write_paths_to_file(ir_file_paths, file_path):
    try:
        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write each path in the list to the file, one per line
            for path in ir_file_paths:
                file.write(f"{path}\n")
        print(f"Paths successfully written to {file_path}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")


ir_paths_list_file = "/home/intern23002/iitH/comPile/ir_paths.txt"
write_paths_to_file(ir_paths_list, ir_paths_list_file)

