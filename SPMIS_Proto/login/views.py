from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from collections import OrderedDict
#from django.core.context_processors import csrf



def register1(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('registration_complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update((request))
    token['form'] = form

    return render(request, 'register.html', token)


def registration_complete(request):
    return render(request, 'register_complete.html')

def results(request):
    api_results = [OrderedDict([('title',
               'Evidence for diversification of Calophyllum L. '
               '(Calophyllaceae) in the Neogene Siwalik forests of eastern '
               'Himalaya'),
              ('abstract',
               'AbstractHere, we report fossil leaves, woods, and pollen '
               'grains comparable to Calophyllum L. (mainly to Calophyllum '
               'inophyllum L. and Calophyllum polyanthum Wall. ex Choisy) of '
               'Calophyllaceae from the'),
              ('publicationDate', '2017-03-01'),
              ('url', 'http://dx.doi.org/10.1007/s00606-016-1376-5'),
              ('issn', '1615-6110')]),
   OrderedDict([('title',
               'Conservation status of the American horseshoe crab, (Limulus '
               'polyphemus): a regional assessment'),
              ('abstract',
               'AbstractHorseshoe crabs have persisted for more than 200 '
               'million years, and fossil forms date to 450 million years ago. '
               'The American horseshoe crab (Limulus polyphemus), one of four '
               'extant horseshoe c'),
              ('publicationDate', '2017-03-01'),
              ('url', 'http://dx.doi.org/10.1007/s11160-016-9461-y'),
              ('issn', '1573-5184')]),
   OrderedDict([('title',
               'A new fossil from the mid-Paleocene of New Zealand reveals an '
               'unexpected diversity of world’s oldest penguins'),
              ('abstract',
               'AbstractWe describe leg bones of a giant penguin from the '
               'mid-Paleocene Waipara Greensand of New Zealand. The specimens '
               'were found at the type locality of Waimanu manneringi and '
               'together with this spe'),
              ('publicationDate', '2017-02-23'),
              ('url', 'http://dx.doi.org/10.1007/s00114-017-1441-0'),
              ('issn', '1432-1904')]),
   OrderedDict([('title',
               'Taxonomic examination of longgu (Fossilia Ossis Mastodi, '
               '“dragon bone”) and a related crude drug, longchi (Dens '
               'Draconis, “dragon tooth”), from Japanese and Chinese crude '
               'drug markets'),
              ('abstract',
               'AbstractLonggu (“dragon bone,” Ryu-kotsu, Fossilia Ossis '
               'Mastodi, or Os Draconis) is the only fossil crude drug listed '
               'in the Japanese Pharmacopoeia. All longgu in the current '
               'Japanese market is impor'),
              ('publicationDate', '2017-02-20'),
              ('url', 'http://dx.doi.org/10.1007/s11418-016-1062-5'),
              ('issn', '1861-0293')]),
   OrderedDict([('title',
               'Agri-food-energy system metabolism: a historical study for '
               'northern France, from nineteenth to twenty-first centuries'),
              ('abstract',
               'AbstractWe reconstruct the metabolism of cereal grain '
               'production and processing systems in the Seine river basin at '
               'four time points between 1860 and 2010 in terms of nitrogen '
               'and energy flows, on the'),
              ('publicationDate', '2017-02-15'),
              ('url', 'http://dx.doi.org/10.1007/s10113-017-1119-3'),
              ('issn', '1436-378X')]),
   OrderedDict([('title',
               'Erosion of insect diversity in response to 7000\xa0years of '
               'relative sea-level rise on a small Mediterranean island'),
              ('abstract',
               'AbstractWe have investigated the potential effects of global '
               'sea-level rise on Mediterranean coastal wetlands by studying '
               'the Coleoptera and pollen fossil remains in a 7000-year '
               'sedimentary record, wh'),
              ('publicationDate', '2017-02-15'),
              ('url', 'http://dx.doi.org/10.1007/s10531-017-1322-z'),
              ('issn', '1572-9710')]),
   OrderedDict([('title',
               'Characteristics and source apportionment of black carbon '
               'aerosols over an urban site'),
              ('abstract',
               'AbstractAethalometer based source apportionment model using '
               'the measured aerosol absorption coefficients at different '
               'wavelengths is used to apportion the contribution of fossil '
               'fuel and wood burning '),
              ('publicationDate', '2017-02-10'),
              ('url', 'http://dx.doi.org/10.1007/s11356-017-8453-3'),
              ('issn', '1614-7499')]),
   OrderedDict([('title',
               'Future Directions in the Field of High-Temperature Corrosion '
               'Research'),
              ('abstract',
               'AbstractHigh-temperature corrosion research will face a '
               'significant change in the near future. Up until now, this '
               'research area was dominated by materials issues related to the '
               'use of fossil fuels in '),
              ('publicationDate', '2017-02-03'),
              ('url', 'http://dx.doi.org/10.1007/s11085-017-9719-3'),
              ('issn', '1573-4889')]),
   OrderedDict([('title',
               'The Evolution of Angiosperm Trees: From  Palaeobotany to '
               'Genomics'),
              ('abstract',
               'AbstractAngiosperm trees now rival the largest conifers in '
               'height and many species reach over 80 m high. The large tree '
               'life form, with extensive secondary xylem, originated with the '
               'progymnosperms an'),
              ('publicationDate', '2017-02-03'),
              ('url', 'http://dx.doi.org/10.1007/7397_2016_31'),
              ('issn', '')]),
   OrderedDict([('title', 'Detection capabilities: some historical footnotes'),
              ('abstract',
               'AbstractPart I Summary of relevant topics from 1923 to '
               'present—including: Currie (Anal Chem 40:586–593, 1968) '
               'detection concepts & capabilities; International detection & '
               'uncertainty standards; Failur'),
              ('publicationDate', '2017-02-01'),
              ('url', 'http://dx.doi.org/10.1007/s10967-016-4925-z'),
              ('issn', '1588-2780')])]

    today = "hello there"

    # for paper in results:
    #     print(paper)
    return render(request, "results.html", {"api_results" : api_results, "today" : today})
