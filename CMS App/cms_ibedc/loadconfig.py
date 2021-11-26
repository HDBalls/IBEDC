import json,os
my_path = os.path.abspath(os.path.dirname(__file__))
my_path = my_path.replace("\\", "/")
print("Path to config file =============> ",my_path)
try:
    def configload(args):
        with open(my_path+'/config.json') as json_file:
            data = json.load(json_file)
            json_file.close()
            results = list()
            for parameter in args:
                results.append(data[''+parameter])
            return results
        
except Exception as e:
    print("Error occured ",e)