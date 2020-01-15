#     ___                  _             _ _
#    / __\__ _ _ __       /_\  _   _  __| (_)_ __       /\  /\___   ___ __ _
#   / /  / _` | '_ \     //_\\| | | |/ _` | | '_ \     / /_/ / _ \ / __/ _` |
#  / /__| (_| | | | |   /  _  \ |_| | (_| | | | | |   / __  / (_) | (_| (_| |
#  \____/\__,_|_| |_|___\_/ \_/\__, |\__,_|_|_| |_|___\/ /_/ \___/ \___\__,_|____
#                  |_____|     |___/             |_____|                   |_____|
#     ___           _            ___    _            _
#    / _ \_ __ ___ (_) ___      /___\__| | _____   _(_)
#   / /_)/ '__/ _ \| |/ _ \    //  // _` |/ _ \ \ / / |
#  / ___/| | | (_) | |  __/   / \_// (_| |  __/\ V /| |
#  \/    |_|  \___// |\___|___\___/ \__,_|\___| \_/ |_|
#                |__/    |_____|                                     Version 0.0.1
#
#                                Emre Ucar   contact_info:ucar.emre@ogr.deu.edu.tr
#
# Doc.Dr.Can Aydın'a teslim edilmek üzere, ödevimin ilk versiyonudur.
#
# Bu projeyi, ikinci dönem derslerinde göreceğimiz,
# Html,Css, Bootstrap, Php gibi teknolojileri kullanarak websayfası ve veritabanı destekli web uygulaması yapıp, geliştireceğim.
#
#  ===============================================================================
#
#  Copyright (C) [2020] [Emre Ucar]
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  ===============================================================================
#
import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def Acikla(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Bunu mu demek istediniz '%s' ? Evetse klavyeden -büyük Harf- E tusuna basın, yoksa H tuşuna basın: " % get_close_matches(w, data.keys())[0])
        if yn == "E":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "H":
            return "Girdiğiniz kelime veritabanında bulunamadı:("
        else:
            return "Ne demek istediniz anlayamadım eyy DEU YBS YL öğrencileri::)"
    else:
        return "Girdiğiniz kelime veritabanında bulunamadı. Demek ki çok zor sordunuz::)"


while True:
  kelime = input("Kelime Girin(Eğer çıkmak isterseniz q tuşuna basınız) : ")
  if kelime == 'q':
    print("Görüşmek üzere. Yine bekleriz:)")
    break
  sonuc = Acikla(kelime)
  if type(sonuc) == list:
      for item in sonuc:
          print(item)
  else:
      print(sonuc)
    
    
 


