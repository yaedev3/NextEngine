from const import *

def RemoveKey(directory, key):
  new_directory = dict(directory)
  del new_directory[key]
  return new_directory

def SortByStatus(anime_list, status_object, writting_function):
  sorted_anime_list = {}
  
  for anime_status in status_object:
    status = anime_status[STATUS_KEY]
    sorted_anime_list[status] = []
  
  for anime_element in anime_list:
    status = anime_element[STATUS_KEY]
    new_element = RemoveKey(anime_element, STATUS_KEY)
    sorted_anime_list[status].append(new_element)

  for anime_status in status_object:
    status = anime_status[STATUS_KEY]
    file_name = anime_status[FILE_KEY]
    sorted_element = sorted_anime_list[status]
    writting_function(sorted_element, file_name)

def SortByWatched(anime_list):
  for anime_element in anime_list:
    try:
      episodes = int(anime_element[EPISODES_KEY])
      watched = int(anime_element[WATCHED_KEY])
      anime_element[REMAINING_KEY] = episodes - watched
    except:
      anime_element[REMAINING_KEY] = 9999
  anime_list.sort(key=lambda x: x[REMAINING_KEY])

def NewCountElement(name, count):
  new_element = {
    TITLE_KEY: name,
    COUNT_KEY: count
  }
  return new_element

def CountByKey(anime_list, const_key):
  key_object = {}
  for anime_element in anime_list:
    key = anime_element[const_key]
    if key in key_object:
      key_object[key] = key_object[key] + 1
    else:
      key_object[key] = 1
  key_object["Total"] = len(anime_list)

  key_list = []
  for key in key_object:
    new_element = NewCountElement(key, key_object[key])
    key_list.append(new_element)

  key_list.sort(key=lambda x: x[COUNT_KEY])
  return key_list