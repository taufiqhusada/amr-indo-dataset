def filter_leak(subfile_name):
    list_leak_sent = ['saya tidak tahu.', 'tanya dia.', 'kata dia.']

    sent_file = f'preprocessed_silver_data/{subfile_name}.sent.txt'
    amr_file = f'preprocessed_silver_data/{subfile_name}.amr.txt'

    list_sent = []
    list_amr = []
    with open(sent_file) as f:
        for item in f:
            list_sent.append(item.strip())
    with open(amr_file) as f:
        for item in f:
            list_amr.append(item.strip())
            
    print(len(list_sent), len(list_amr))
    list_idx_leak = []
    for i in range(len(list_sent)):
        if(list_sent[i] in list_leak_sent):
            list_idx_leak.append(i)
    print(list_idx_leak)

    filtered_list_amr = []
    filtered_list_sent = []
    for i in range(len(list_sent)):
        if (i in list_idx_leak):
            continue
        
        filtered_list_amr.append(list_amr[i])
        filtered_list_sent.append(list_sent[i])

    print(len(filtered_list_sent), len(filtered_list_amr))

    with open(sent_file, 'w') as f:
        for sent in filtered_list_sent:
            f.write(sent)
            f.write('\n')

    with open(amr_file, 'w') as f:
        for sent in filtered_list_amr:
            f.write(sent)
            f.write('\n')

filter_leak('linearized_penman')
filter_leak('dfs')
filter_leak('nodes_only')