import pandas as pd
import torch
from transformers import BertModel, BertTokenizer

data = pd.read_csv("/Users/liuzihao/Downloads/APIs.csv", encoding='iso-8859-1')

model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

descr = data['Description'].dropna()
sentences = descr

bianma_APIs = []

for sentence in sentences:
    input_ids = tokenizer.encode(sentence, add_special_tokens=True, truncation="longest_first")

    input_ids = torch.tensor([input_ids])

    with torch.no_grad():
        last_hidden_states = model(input_ids)[0]
        bianma_APIs.append(last_hidden_states[0][0])

