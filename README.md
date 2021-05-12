# `pwtdata`

This module contains Penn World Table 10.0. No more than that.

You're looking at a fork of https://github.com/spring-haru/pwtdata.git by Tetsu Haruyama. 

The original module is already very useful but I wanted a little more. This fork reads data from the Stata dataset distributed at https://www.rug.nl/ggdc/productivity/pwt/ to be able to use variable labels.

### How to Install
```
$ pip install git+https://github.com/kenjisato/pwtdata.git
```
or
```
git clone https://github.com/kenjisato/pwtdata.git
cd pwtdata
pip install .
```

### How to Use

Import data and learn what variables are contained.

```
>>> import pwtdata
>>> print(pwtdata.var_defitions)
Variable name:  Variable definition

----- Identifier variables -----
countrycode:    3-letter ISO country code
country:            Country name
currency_unit:  Currency unit
year:               Year

----- Real GDP, employment and population levels -----
rgdpe:  Expenditure-side real GDP at chained PPPs (in mil. 2017US$),,,
rgdpo:  Output-side real GDP at chained PPPs (in mil. 2017US$),,,\

...
...
```

Then, select columns you need and convert them into a pandas dataframe.

```
>>> pwt = pwtdata.load(["country", "year", "rgdpo"])
>>> pwt[pwt.year > 2017]
            country  year          rgdpo
68            Aruba  2018    3444.658691
69            Aruba  2019    3467.299561
138          Angola  2018  233805.062500
139          Angola  2019  227855.718750
208        Anguilla  2018     150.344666
...             ...   ...            ...
12669  South Africa  2019  734094.375000
12738        Zambia  2018   55459.121094
12739        Zambia  2019   56783.714844
12808      Zimbabwe  2018   43420.898438
12809      Zimbabwe  2019   40826.570312

[2196 rows x 3 columns]
```

If you'd like to refer to labels programatically, pass `description=True` to `load()` function.

```
>>> pwt, desc = pwtdata.load(["country", "year", "rgdpo"], description=True)
>>> desc
                                               Description
country                                       Country name
year                                                  Year
rgdpo    Output-side real GDP at chained PPPs (in mil. ...
```

### Reference

- Feenstra, Robert C., Robert Inklaar and Marcel P. Timmer (2015), "The Next Generation of the Penn World Table" American Economic Review, 105(10), 3150-3182, available for download at www.ggdc.net/pwt
