import json

def OpenJson(file):
  try:
    f = open(file,)
    data = json.load(f)
    f.close()
  except:
    data = {}
  return data
  
def WriteJson(object, file):
  json_object = json.dumps(object, indent = 4)
  with open(file, "w") as outfile:
    outfile.write(json_object)
    
def GetFirstValue(file):
  data = OpenJson(file)
  return list(data.values())[0]

def OpenFile(file_name):
  file = open(file_name)
  file_content = file.read()
  file.close()
  return file_content