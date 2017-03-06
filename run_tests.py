import yaml, sys, os, importlib

script_path =os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,script_path+'/tests')

with open('config.yml') as f:
    config = yaml.safe_load(f.read())

output = {}
for module in config['enabled_modules']:
    i = importlib.import_module(module)
    return_string = i.test()
    if return_string != "":
        output.append('%s: %s' % (module,return_string))
if len(output) ==0:
    print('pass')
else:
    print(', '.join(output)
