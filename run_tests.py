import json, yaml, sys, os, importlib

script_path =os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,script_path+'/tests')

with open('config.yml') as f:
    config = yaml.safe_load(f.read())

output = {}
for module in config['enabled_modules']:
    i = importlib.import_module(module)
    output[module] = i.test()

print(json.dumps(output))
