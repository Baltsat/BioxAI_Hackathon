import torch, json

def load_env(device="cuda"):
    """
    Return a binary function to predict the interaction
    likelihood from two drugs and a list of possible drugs.
    
    Usage:
    >>> predict, drugs = load_env()
    >>> test1, test2 = drugs[42], drugs[1337]
    >>> predict(test1, test2)
    """
    model = torch.load("/workspace/data/model.pk").to(device)
    drugs = json.load(open("/workspace/data/drugs.txt"))
    drug2feature = json.load(open("/workspace/data/drug2feature.txt"))
    def predict(drug1, drug2):
        drug1, drug2 = (
            torch.tensor(drug2feature[d], device=device)
            for d in (drug1, drug2)
        )
        return model(drug1, drug2)[0][0].item()
    return predict, drugs