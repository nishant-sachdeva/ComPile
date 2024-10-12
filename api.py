from datasets import load_dataset, get_dataset_split_names, load_dataset_builder

datasetName = 'llvm-ml/ComPile'

### load_dataset_builder
# ds_builder = load_dataset_builder(datasetName)
# print("Features = ", ds_builder.info.features)
# print("Info ", ds_builder.info)


### Download dataset into local
full_dataset = load_dataset(datasetName, split='train', streaming=True)

c_cpp_dataset = full_dataset.filter(lambda example: example['language'].startswith('c'))

# ds = c_cpp_dataset.t

package_sources = []
package_sources_set = set(package_sources)

languages = []
languages_set = set(languages)

for ix, item in enumerate(c_cpp_dataset):
    package_sources_set.add(item['package_source'])
    languages_set.add(item['language'])

    print(f"{ix}, {item['language']}", end="\r")

print("Languages Captured ", languages_set)

print("Number of unique package_sources", len(package_sources_set))
print("The unique sources are ")

for src in package_sources_set:
    print(src)

# ds = full_dataset.take(3)
# ds = ds.take(10000)

# for ix, item in enumerate(full_dataset):
#     print(ix, item['package_source'])

#     if (ix == 1000):
#         break

# ds = ds.skip(10000)
# print(full_dataset.features)
# print(full_dataset.dataset_size)

# obj = next(iter(full_dataset))
# print(obj['package_source'])

# obj2 = next(iter(full_dataset))
# print(obj['package_source'])

# print("Streaming object fetched")

# print(list(ds))

# for obj in list(ds):
    # print(obj['package_source'], obj['language'], obj['content'])

# obj = next(iter(ds))

# while obj['language'].startswith('c'):
#     print(obj['package_source'] , obj['language'])
#     obj = next(iter(ds))

# for row in ds:
#     print(row)
#     break


### Download dataset as a streamer
# ds = load_dataset('llvm-ml/ComPile', split='train', streaming=True)
# for row in ds:
#     print(row)
#     break


