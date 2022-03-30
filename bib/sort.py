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

def CountByKey(anime_list, key):
  key_object = {}
  for anime_element in anime_list:
    episodes = anime_element[key]
    if episodes in key_object:
      key_object[episodes] = key_object[episodes] + 1
    else:
      key_object[episodes] = 1
  key_object["Total"] = len(anime_list)
  return key_object