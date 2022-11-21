import urllib, urllib.request
from tqdm import tqdm
"""
  Python script to get stat numbers from INSPIRE:

  All requests to the inspire API starts with:
  https://inspirehep.net/api/literature?fields=hits.total&format=json&q=
  Possible fields are:
  publication_info.year:YYYY
  document_type:article
  dois:*
  arxiv_eprints.categories:hep-ph
  ac 1 -> 10
  collaborations.value:atlas/cms
"""

# This routine gets the total from a query supplied thru a Search string:
def GetInspireTotal(SearchString):
  url = DefaultURLprefix + urllib.parse.quote(SearchString)
  #print("url: ",url)
  data = urllib.request.urlopen(url)
  #print(data.read().decode('utf-8'))
  DataOut = data.read().decode('utf-8')
  #print(DataOut)
  #print(DataOut[DataOut.index('}],"total":')+11:][:DataOut[DataOut.index('}],"total":')+11:].index("}")])
  try:
    total = DataOut[DataOut.index('}],"total":')+11:][:DataOut[DataOut.index('}],"total":')+11:].index("}")] 
  except:
    total = 0
  return total

# This routine takes a file name and parameters for the API and stores the annual data:
def StoreAnnual(fname, Years=[], APIparams=[], Exclude=[]):
  datfile = open(fname, 'w')
  datfile.write("! This file was created with the following query parameters:\n")
  for i in APIparams:
    comment = "! " + i + "\n"
    datfile.write(comment)
  for year in tqdm(range(Years[0],Years[1]+1)):
    SearchString = ""
    for j,itm in enumerate(APIparams):
      if j != 0:
        SearchString += " AND "
      SearchString += itm 
    SearchString += " AND publication_info.year:{}".format(year)
    for j,itm in enumerate(Exclude):
      SearchString += " AND NOT " + itm
    tot = GetInspireTotal(SearchString)
    datfile.write("{} {}\n".format(year,tot))
  datfile.close()
  return

DefaultURLprefix = 'https://inspirehep.net/api/literature?fields=hits.total&format=json&q='
#total = GetInspireTotal("")
#print("Total is: ",total)
#
#  All publications with hep-ph on an annual basis:
#
fname = "inspire-annual-doi-hep-ph.dat"
print(fname)
StoreAnnual(fname,[2001,2021],["dois.value:*","document_type:article","arxiv_eprints.categories:hep-ph"])


#
#  All publications with hep-th on an annual basis:
#
fname = "inspire-annual-doi-hep-th.dat"
print(fname)
StoreAnnual(fname,[2001,2021],["dois.value:*","document_type:article","arxiv_eprints.categories:hep-th"])
#
#  All publications with hep-ph on an annual basis without ATLAS and CMS:
#
fname = "inspire-annual-doi-hep-ph-no-atlas-cms.dat"
print(fname)
StoreAnnual(fname,[2001,2021],["dois.value:*","document_type:article","arxiv_eprints.categories:hep-ph"], ["collaborations.value:atlas", "collaborations.value:cms"])
#
#  All publications with hep-th on an annual basis without ATLAS and CMS:
#
fname = "inspire-annual-doi-hep-th-no-atlas-cms.dat"
print(fname)
StoreAnnual(fname,[2001,2021],["dois.value:*","document_type:article","arxiv_eprints.categories:hep-th"], ["collaborations.value:atlas", "collaborations.value:cms"])
#
#  Lone wolf publications with hep-ph on an annual basis without ATLAS and CMS and not hep-th:
#
fname = "inspire-annual-doi-hep-ph-lone-wolf-no-atlas-cms-hep-th.dat"
print(fname)
StoreAnnual(fname,[2001,2021],
                  ["dois.value:*","document_type:article","arxiv_eprints.categories:hep-ph","ac 1"], 
                  ["collaborations.value:atlas", "collaborations.value:cms","arxiv_eprints.categories:hep-th"])
#
#  Lone wolf publications with hep-th on an annual basis without ATLAS and CMS and not hep-ph:
#
fname = "inspire-annual-doi-hep-th-lone-wolf-no-atlas-cms-hep-ph.dat"
print(fname)
StoreAnnual(fname,[2001,2021],
                  ["dois.value:*","document_type:article","arxiv_eprints.categories:hep-th","ac 1"], 
                  ["collaborations.value:atlas", "collaborations.value:cms","arxiv_eprints.categories:hep-ph"])
#
#  Small collaborations publications with hep-ph on an annual basis without ATLAS and CMS and not hep-th:
#
fname = "inspire-annual-doi-hep-ph-ac-2-to-5-no-atlas-cms-hep-th.dat"
print(fname)
StoreAnnual(fname,[2001,2021],
                  ["dois.value:*","document_type:article","arxiv_eprints.categories:hep-ph","ac 2 -> 5"], 
                  ["collaborations.value:atlas", "collaborations.value:cms","arxiv_eprints.categories:hep-th"])
#
#  Small collaborations publications with hep-th on an annual basis without ATLAS and CMS and not hep-ph:
#
fname = "inspire-annual-doi-hep-th-ac-2-to-5-no-atlas-cms-hep-ph.dat"
print(fname)
StoreAnnual(fname,[2001,2021],
                  ["dois.value:*","document_type:article","arxiv_eprints.categories:hep-th","ac 2 -> 5"], 
                  ["collaborations.value:atlas", "collaborations.value:cms","arxiv_eprints.categories:hep-ph"])
#
#  Medium collaborations publications with hep-ph on an annual basis without ATLAS and CMS and not hep-th:
#
fname = "inspire-annual-doi-hep-ph-ac-6-to-10-no-atlas-cms-hep-th.dat"
print(fname)
StoreAnnual(fname,[2001,2021],
                  ["dois.value:*","document_type:article","arxiv_eprints.categories:hep-ph","ac 6 -> 10"], 
                  ["collaborations.value:atlas", "collaborations.value:cms","arxiv_eprints.categories:hep-th"])
#
#  Medium collaborations publications with hep-th on an annual basis without ATLAS and CMS and not hep-ph:
#
fname = "inspire-annual-doi-hep-th-ac-6-to-10-no-atlas-cms-hep-ph.dat"
print(fname)
StoreAnnual(fname,[2001,2021],
                  ["dois.value:*","document_type:article","arxiv_eprints.categories:hep-th","ac 6 -> 10"], 
                  ["collaborations.value:atlas", "collaborations.value:cms","arxiv_eprints.categories:hep-ph"])
#
#  Big collaborations publications with hep-ph on an annual basis without ATLAS and CMS and not hep-th:
#
fname = "inspire-annual-doi-hep-ph-ac-gt-10-no-atlas-cms-hep-th.dat"
print(fname)
StoreAnnual(fname,[2001,2021],
                  ["dois.value:*","document_type:article","arxiv_eprints.categories:hep-ph","ac > 10"], 
                  ["collaborations.value:atlas", "collaborations.value:cms","arxiv_eprints.categories:hep-th"])
#
#  Big collaborations publications with hep-th on an annual basis without ATLAS and CMS and not hep-ph:
#
fname = "inspire-annual-doi-hep-th-ac-gt-10-no-atlas-cms-hep-ph.dat"
print(fname)
StoreAnnual(fname,[2001,2021],
                  ["dois.value:*","document_type:article","arxiv_eprints.categories:hep-th","ac > 10"], 
                  ["collaborations.value:atlas", "collaborations.value:cms","arxiv_eprints.categories:hep-ph"])
#
#  Atlas papers:
#
fname = "inspire-annual-doi-hep-ex-atlas.dat"
print(fname)
StoreAnnual(fname,[2001,2021],
                  ["dois.value:*","document_type:article","arxiv_eprints.categories:hep-ex","collaborations.value:atlas"], 
                  ["collaborations.value:cms","arxiv_eprints.categories:hep-ph"])
#
#  CMS papers:
#
fname = "inspire-annual-doi-hep-ex-cms.dat"
print(fname)
StoreAnnual(fname,[2001,2021],
                  ["dois.value:*","document_type:article","arxiv_eprints.categories:hep-ex","collaborations.value:cms"], 
                  ["collaborations.value:atlas","arxiv_eprints.categories:hep-ph"])
"""
"""
