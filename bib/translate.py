from const import *
import json
import xmltodict

def ConvertXmlToJson(xml_data):
  xml_object = xmltodict.parse(xml_data)
  object = json.dumps(xml_object, indent = 4)
  json_object = json.loads(object)
  return json_object

def AssignTags(xml_tags):
  if xml_tags == None:
    xml_tags = ''
  xml_tags = xml_tags.replace(" ", "")
  return xml_tags.split(',')

def TranslateTwoFiles(xml_data, keys):
  json_object = ConvertXmlToJson(xml_data)
  anime_list = json_object["myanimelist"]["anime"]
  new_anime_list = []

  for anime_item in anime_list:
    new_entry = {}
    for key in keys:
      xml_key = key["xml"]
      json_key = key["json"]
      if json_key == TAG_KEY:
        new_entry[json_key] = AssignTags(anime_item[xml_key])
      else:
        new_entry[json_key] = anime_item[xml_key]
      
    new_anime_list.append(new_entry)

  return new_anime_list