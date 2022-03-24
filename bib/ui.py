from const import *

def PrintMenu(menu):
  for i, item in enumerate(menu, 1):
    print(f"{i}. {item}")
  option = input("Selecciona una opción:\t")
  if option == '':
    option = 0
  return int(option)

def GetMessageNextAnime(anime_element, i):
  title = anime_element[TITLE_KEY]
  episodes = anime_element[EPISODES_KEY]
  watched = anime_element[WATCHED_KEY]
  remaining = anime_element[REMAINING_KEY]
  return f"{i}. {title} {watched}/{episodes}\n\tRemaining: {remaining}"

def PrintNextAnime(anime_list, filter):
  i = 1
  for anime_element in anime_list:
    tags = anime_element[TAG_KEY]
    if filter in tags:
      message = GetMessageNextAnime(anime_element, i)
      i = i + 1
      print(message)
  print()