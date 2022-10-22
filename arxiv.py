import urllib, urllib.request
from tqdm import tqdm

Str = "https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=&terms-0-field=title&classification-physics=y&classification-physics_archives=hep-ph&classification-include_cross_list=exclude&date-year=&date-filter_by=date_range&date-from_date=2015-01-01&date-to_date=2015-01-31&date-date_type=submitted_date_first&abstracts=hide&size=50&order=-announced_date_first"

Years = ["2015",
         "2016",
         "2017",
         "2018",
         "2019",
         "2020",
         "2021"]

Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

StartDates = ["01-01",
              "02-01",
              "03-01",
              "04-01",
              "05-01",
              "06-01",
              "07-01",
              "08-01",
              "09-01",
              "10-01",
              "11-01",
              "12-01"]

EndDates = ["01-31",
            "02-28",
            "03-31",
            "04-30",
            "05-31",
            "06-30",
            "07-31",
            "08-31",
            "09-30",
            "10-31",
            "11-30",
            "12-31"]

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
    filename = "arxiv-monthly-stat-"+cat+".txt"
    datfile = open(filename, 'w')
    datfile.write("! years considered: ")
    for year in Years:
        datfile.write(year+" ")
    datfile.write("\n")
    for imonth,month in enumerate(Months):
        print("Processing month: ",month)
        datfile.write(month+" ")
        for iyear,year in enumerate(Years):
            print("processing year: ",year)
            url = Str.replace("2015",year).replace("01-01",StartDates[imonth]).replace("01-31",EndDates[imonth]).replace("hep-ph",cat)
            tot = GetArXivTotal(url)
            datfile.write("{} ".format(tot))
        datfile.write("\n")
