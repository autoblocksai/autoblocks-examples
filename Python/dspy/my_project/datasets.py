from dspy.datasets.gsm8k import GSM8K, gsm8k_metric

# Load math questions from the GSM8K dataset
gsm8k = GSM8K()

trainset = gsm8k.train[:10]
devset = gsm8k.dev[:10]
metric = gsm8k_metric
