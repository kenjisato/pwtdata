"""Module for downloading the Penn World Tables (PWT) data.
Module contains a set of functions that download the PWT data set.
"""
from os.path import abspath, join, split
import gzip
import pandas as pd


def get_path(f):
    return split(abspath(f))[0]


var_definitions = """\
Variable name:	Variable definition

----- Identifier variables -----
countrycode:	3-letter ISO country code
country:	    Country name
currency_unit:	Currency unit
year:		    Year

----- Real GDP, employment and population levels -----
rgdpe:  Expenditure-side real GDP at chained PPPs (in mil. 2017US$),,,
rgdpo:  Output-side real GDP at chained PPPs (in mil. 2017US$),,,
pop:    Population (in millions),,,
emp:    Number of persons engaged (in millions),,,
avh:    Average annual hours worked by persons engaged,,,
hc:     Human capital index, based on years of schooling and returns to education; see Human capital in PWT9.

----- Current price GDP, capital and TFP -----
ccon:   Real consumption of households and government, at current PPPs (in mil. 2017US$)
cda:    Real domestic absorption, (real consumption plus investment), at current PPPs (in mil. 2017US$)
cgdpe:  Expenditure-side real GDP at current PPPs (in mil. 2017US$)
cgdpo:  Output-side real GDP at current PPPs (in mil. 2017US$)
cn:     Capital stock at current PPPs (in mil. 2017US$)
ck:     Capital services levels at current PPPs (USA=1)
ctfp:   TFP level at current PPPs (USA=1)
cwtfp:  Welfare-relevant TFP levels at current PPPs (USA=1)

----- National accounts-based variables -----
rgdpna: Real GDP at constant 2017 national prices (in mil. 2017US$)
rconna: Real consumption at constant 2017 national prices (in mil. 2017US$)
rdana:  Real domestic absorption at constant 2017 national prices (in mil. 2017US$)
rnna:   Capital stock at constant 2017 national prices (in mil. 2017US$)
rkna:   Capital services at constant 2017 national prices (2017=1)
rtfpna: TFP at constant national prices (2017=1)
rwtfpna:Welfare-relevant TFP at constant national prices (2017=1)
labsh:  Share of labour compensation in GDP at current national prices
irr:    Real internal rate of return
delta:  Average depreciation rate of the capital stock

----- Exchange rates and GDP price levels -----
xr:     Exchange rate, national currency/USD (market+estimated)
pl_con  Price level of CCON (PPP/XR), price level of USA GDPo in 2017=1
pl_da   Price level of CDA (PPP/XR), price level of USA GDPo in 2017=1
pl_gdpo Price level of CGDPo (PPP/XR), price level of USA GDPo in 2017=1

----- Data information variables -----
i_cig:      0/1/2/3/4: relative price data for consumption, investment and government is extrapolated (0), benchmark (1), interpolated (2), ICP PPP timeseries: benchmark or interpolated (3) or  ICP PPP timeseries: extrapolated (4)
i_xm:       0/1/2: relative price data for exports and imports is extrapolated (0), benchmark (1) or interpolated (2)
i_xr:       0/1: the exchange rate is market-based (0) or estimated (1)
i_outlier:  0/1: the observation on pl_gdpe or pl_gdpo is not an outlier (0) or an outlier (1)
i_irr:      0/1/2/3: the observation for irr is not an outlier (0), may be biased due to a low capital share (1), hit the lower bound of 1 percent (2), or is an outlier (3)
cor_exp:    Correlation between expenditure shares of the country and the US (benchmark observations only)
statcap:    Statistical capacity indicator (source: World Bank, developing countries only)

----- Shares in CGDPo -----
csh_c:  Share of household consumption at current PPPs
csh_i:  Share of gross capital formation at current PPPs
csh_g:  Share of government consumption at current PPPs
csh_x:  Share of merchandise exports at current PPPs
csh_m:  Share of merchandise imports at current PPPs
csh_r:  Share of residual trade and GDP statistical discrepancy at current PPPs

----- Price levels, expenditure categories and capital -----
pl_c:   Price level of household consumption,  price level of USA GDPo in 2017=1
pl_i:   Price level of capital formation,  price level of USA GDPo in 2017=1
pl_g:   Price level of government consumption,  price level of USA GDPo in 2017=1
pl_x:   Price level of exports, price level of USA GDPo in 2017=1
pl_m:   Price level of imports, price level of USA GDPo in 2017=1
pl_n:   Price level of the capital stock, price level of USA in 2017=1
pl_k:   Price level of the capital services, price level of USA=1"""


def load(columns=None, description=False):
    with gzip.open(join(get_path(__file__), "data/pwt1001.dta.gz")) as fp:
        pwt_reader = pd.read_stata(fp, iterator=True)

    if columns is None:
            columns = pwt_reader.varlist

    if description:
        var_labels = pwt_reader.variable_labels()
        labels_df = pd.DataFrame([var_labels[var] for var in columns], 
                                 index=columns, columns=["Description"])
        return pwt_reader.read(columns=columns), labels_df
    else:
        return pwt_reader.read(columns=columns)
    
