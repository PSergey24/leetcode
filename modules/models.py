import torch
from transformers import AutoTokenizer, AutoModel


def embed_bert_cls(text, model, tokenizer):
    t = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**{k: v.to(model.device) for k, v in t.items()})
    embeddings = model_output.last_hidden_state[:, 0, :]
    embeddings = torch.nn.functional.normalize(embeddings)
    return embeddings[0].cpu().numpy()


if __name__ == '__main__':
    # "cointegrated/rubert-tiny2"
    tokenizer = AutoTokenizer.from_pretrained("data/rubert-tiny2/tokenizer")
    # "cointegrated/rubert-tiny2"
    model = AutoModel.from_pretrained("data/rubert-tiny2/model")

    embeddings = embed_bert_cls('привет мир', model, tokenizer)
