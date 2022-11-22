import pandas as pd
import numpy as np
from faker import Faker

# create some fake data
fake = Faker()

# function to create a dataframe with fake values for our transport business
def make_doprava(num):
    # lists to randomly assign to doprava
    region_list = ['Hlavní město Praha',
                   'Jihočeský kraj',
                   'Jihomoravský kraj',
                   'Karlovarský kraj',
                   'Královehradecký kraj',
                   'Liberecký kraj',
                   'Moravskoslezský kraj',
                   'Olomoucký kraj',
                   'Pardubický kraj',
                   'Plzeňský kraj',
                   'Středočeský kraj',
                   'Ústecký kraj,'
                   'Vysočina',
                   'Zlínský kraj']
    company_list = ['Toptrans',
                    'GLS',
                    'Spedquick Trebic',
                    'Geis',
                    'Pap Trutnov']
    transport_type_list = ['vlak',
                           'kamion',
                           'nákladní vozidlo']
    team_list = [fake.color_name() for x in range(4)]
    #id_list = [x for x in range(x1,Num)]


    fake_doprava = [{'Transit ID':x+1000,
                     'Date':fake.date_between(start_date='2022-01-01T00:00:00.000Z', end_date='2022-06-30T00:00:00.000Z'),
                     'Region':np.random.choice(region_list),
                     'Poslytovatelé dopravy':np.random.choice(company_list),
                     'Doprava':np.random.choice(transport_type_list),
                     'Team':np.random.choice(team_list)} for x in range(num)]
    return fake_doprava

df = pd.DataFrame(make_doprava(num=500))
df.head()