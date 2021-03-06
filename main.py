import sys
sys.path.insert(1, './bib/')

from const import *
import inputoutput
import ui
import translate
import sort

menu = inputoutput.GetFirstValue('input/menu.json')
keys = inputoutput.GetFirstValue('input/keys.json')
status = inputoutput.GetFirstValue('input/status.json')

def ConvertInputFile():
  xml_data = inputoutput.OpenFile(INPUT_FILE)
  anime_list = translate.TranslateTwoFiles(xml_data, keys)
  inputoutput.WriteJson(anime_list, OUTPUT_FILE)
  sort.SortByStatus(anime_list, status, inputoutput.WriteJson)

def PrintSortedFile(file_name, filter):
  anime_list = inputoutput.OpenJson(file_name)
  sort.SortByWatched(anime_list)
  ui.PrintNextAnime(anime_list, filter)

def CountPrintByKey(file_name, key):
  anime_list = inputoutput.OpenJson(file_name)
  count_list = sort.CountByKey(anime_list, key)
  ui.PrintCountList(count_list)

def MenuOptions(option):
  if option == 1:
    ConvertInputFile()
    PrintSortedFile(WATCHING_FILE, END_KEY)

  if option == 2:
    ConvertInputFile()

  if option == 3:
    ConvertInputFile()
    CountPrintByKey(COMPLETED_FILE, TYPE_KEY)

  if option == 4:
    ConvertInputFile()
    CountPrintByKey(COMPLETED_FILE, EPISODES_KEY)

  if option == 5:
    ConvertInputFile()
    CountPrintByKey(PLANT_FILE, TYPE_KEY)

def main():
  print("Welcome to this system!")
  option = ui.PrintMenu(menu)
  MenuOptions(option)
  print("Have a nice day!")

if __name__ == "__main__":
  main()