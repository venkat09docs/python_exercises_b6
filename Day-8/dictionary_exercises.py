# DICTIONARY BASICS

# Creating a dictionary with various key types

model_config = {'model_name': "GPT-4",'layers': 96,'parameters': '200B',10: 'Ten',(1,2): 0.8,True: 'active',"list": [1, 2, 3, 4, 5]}

print(model_config)
print(type(model_config))
print(len(model_config))

hyperparameters = {
    'learning_rate': 0.0001,
    'dropout_rate': 0.3,
    'optimizer': 0.3,
    'dropout_rate': 0.6,
}

# Accessing dictionary values using keys
print(hyperparameters['optimizer'])
print(hyperparameters['learning_rate'])

# print(hyperparameters['dropout'])

print(hyperparameters.get('dropout_rate', 'Key Not Found'))

hyperparameters['optimizer'] = "Adam"

print(hyperparameters)

# BEST PRACTICES FOR DICTIONARIES

# 1. Stick to **immutable keys** (e.g., strings, numbers, tuples)
# 2. Avoid **duplicate keys** (last assigned value will override)
# 3. Use **.get()** for safe access to prevent errors

# NESTED DICTIONARIES

pipeline_config = {
    'GPT-4': {'layers': 48, 'parameters': '175B', 'attention_heads': 96},
    'BERT': {'layers': 24, 'parameters': '345M', 'attention_heads': 16},
    'Opus-4': {'layers': 46, 'parameters': '300B', 'attention_heads': 25}
}

# [2][1]
print(pipeline_config['BERT']['parameters'])
print(pipeline_config['GPT-4']['layers'])
print(pipeline_config['Opus-4']['parameters'])



