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
from collections import Counter

# Initialize a Counter for package sources and a set for languages
package_source_counts = Counter()
languages_set = set()

print("Counting, fetching started")

# Iterate over the dataset
for ix, item in enumerate(c_cpp_dataset):
    # Update the package source count
    package_source_counts[item['package_source']] += 1
    # Add the language to the set
    languages_set.add(item['language'])
    # Print the current index and language
    print(f"{ix}, {item['package_source']}, {item['language']}")

print("Iteration finished")

# 1. Print out a map { package_source : number_of_occurrences }
print("Package Source Counts:")
for source, count in package_source_counts.items():
    print(f"{source}: {count}")

# 2. Print out the languages used
print("\nLanguages Used:")
for language in languages_set:
    print(language)

# 3. Print out the total number of unique package sources
print(f"\nTotal number of unique package sources: {len(package_source_counts)}")

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


