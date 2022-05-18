import glob
from tqdm import tqdm
import json
from nltk import sent_tokenize

list_file_silver = glob.glob('data_200k_sentences_indo4b/*.txt')
silver_data = []
for filename in list_file_silver:
    with open(filename) as f:
        silver_data += f.readlines()

for i in range(len(silver_data)):
    silver_data[i] = silver_data[i].strip()

print(len(silver_data))
print(silver_data[0])

# ## check leak in data uji pembangkitan teks 
# list_file_test = glob.glob('../amr-to-text-indonesia/data/test/preprocessed_data/*/test.sent.txt')
# data_uji_pembangkitan_teks = []
# for filename in list_file_test:
#     with open(filename) as f:
#         data_uji_pembangkitan_teks += f.readlines()

# for i in range(len(data_uji_pembangkitan_teks)):
#     data_uji_pembangkitan_teks[i] = data_uji_pembangkitan_teks[i].strip()

# print(len(data_uji_pembangkitan_teks))
# print(data_uji_pembangkitan_teks[0])

# for s1 in tqdm(data_uji_pembangkitan_teks):
#     for s2 in silver_data:
#         if (s1==s2):
#             print('sama', s1, s2)
#             break

## check leak in xlsum indo test
filename = 'indonesian_test.jsonl'
xlsum_test = []

with open(filename, encoding='utf8') as f:
    for line in f:
        raw = json.loads(line)
        xlsum_test += sent_tokenize(raw['text'].strip())
        xlsum_test += sent_tokenize(raw['summary'].strip())
print(len(xlsum_test))
print(xlsum_test[0])

outfile = open('result.txt', 'w')
for s1 in silver_data:
    for s2 in tqdm(xlsum_test):
        if (s1 == s2):
            print('sama', s1, '\n', s2)
            outfile.write(s1)
            outfile.write('\n')
            break

outfile.close()
    