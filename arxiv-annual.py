import urllib, urllib.request
from tqdm import tqdm

Str = "https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=&terms-0-field=title&classification-physics=y&classification-physics_archives=hep-ph&classification-include_cross_list=exclude&date-year=&date-filter_by=date_range&date-from_date=2015-01-01&date-to_date=2015-01-31&date-date_type=submitted_date_first&abstracts=hide&size=50&order=-announced_date_first"

Years = ["2000",
         "2001",
         "2002",
         "2003",
         "2004",
         "2005",
         "2006",
         "2007",
         "2008",
         "2009",
         "2010",
         "2011",
         "2012",
         "2013",
         "2014",
         "2015",
         "2016",
         "2017",
         "2018",
         "2019",
         "2020",
         "2021",
         "2022"]

# This routine gets the total from a query supplied thru a Search string:
def GetArXivTotal(url):
  data = urllib.request.urlopen(url)
  #print(data.read().decode('utf-8'))
  DataOut = data.read().decode('utf-8')
  #print(DataOut)
  #print(DataOut[DataOut.index('}],"total":')+11:][:DataOut[DataOut.index('}],"total":')+11:].index("}")])
  try:
    total = DataOut[DataOut.index('Showing 1&ndash;50 of')+22:][:DataOut[DataOut.index('Showing 1&ndash;50 of')+22:].index("results")] 
  except:
    total = 0
  return total

for cat in ["hep-ph", "hep-th"]:
    print("Considering ",cat)
    filename = "arxiv-annual-stat-"+cat+".txt"
    datfile = open(filename, 'w')
    for iyear,year in enumerate(Years):
        print("processing year: ",year)
        datfile.write(year+" ")
        url = Str.replace("2015",year).replace("01-01","01-01").replace("01-31","12-31").replace("hep-ph",cat)
        tot = GetArXivTotal(url).replace(',',"")
        datfile.write("{}\n".format(tot))
