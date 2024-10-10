from datasets import load_dataset, get_dataset_split_names, load_dataset_builder

datasetName = 'llvm-ml/ComPile'

### load_dataset_builder
ds_builder = load_dataset_builder(datasetName)
print("Features = ", ds_builder.info.features)
print("Info ", ds_builder.info)


### Download dataset into local
# ds = load_dataset('llvm-ml/ComPile', split='train[:0.001%]')
# for row in ds:
#     print(row)
#     break


### Download dataset as a streamer
ds = load_dataset('llvm-ml/ComPile', split='train[:0.001%]', streaming=True)
for row in ds:
    print(row)
    break


