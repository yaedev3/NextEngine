from const import *

def PrintMenu(menu):
  for i, item in enumerate(menu, 1):
    print(f"{i}. {item}")
  option = input(f"Selecciona una opción (default = {DEFAULT_MENU}):\t")
  if option == '':
    option = DEFAULT_MENU
  return int(option)

def GetMessageNextAnime(anime_element, i):
  title = anime_element[TITLE_KEY]
  episodes = anime_element[EPISODES_KEY]
  watched = anime_element[WATCHED_KEY]
  remaining = anime_element[REMAINING_KEY]
  return f"{i}. {title} {watched}/{episodes}\n\tRemaining: {remaining}"

def GetRemaining(anime_element):
  return anime_element[REMAINING_KEY]

def PrintNextAnime(anime_list, filter):
  i = 1
  remaining = 0
  for anime_element in anime_list:
    tags = anime_element[TAG_KEY]
    if filter in tags:
      remaining = remaining + GetRemaining(anime_element)
      message = GetMessageNextAnime(anime_element, i)
      i = i + 1
      print(message)
  print(f"\tTotal: {remaining}")
  print()
  
def PrintSimpleObject(simple_object):
  i = 1
  for key in simple_object:
    count = simple_object[key]
    message = f"{i}. {key}: {count}"
    i = i + 1
    print(message)

def PrintCountList(count_list):
  for count_element in count_list:
    name = count_element[TITLE_KEY]
    count = count_element[COUNT_KEY]
    message = f"{name}: {count}"
    print(message)