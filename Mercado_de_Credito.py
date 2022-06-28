# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15WFVjJxe14cFYg4HIRwJtH2VQ5DjBgw1
"""

import numpy as np
import pandas as pd
import datetime as dt

!pip install ipeadatapy
import ipeadatapy as ip

!pip install python-bcb
from bcb import sgs

from matplotlib import pyplot as plt 
import seaborn as sns

juros = sgs.get({'Juro': 20714,
                 'Spread' : 20783,
                 'Inadimplência' : 21082})

juros_long = pd.melt(juros.reset_index(),
                     id_vars = 'Date',
                     value_vars = juros.columns,
                     var_name = 'variable',
                     value_name = 'values')

g = sns.FacetGrid(juros_long, col = 'variable',
                  col_wrap= 2,
                  hue= 'variable',
                  sharey= False,
                  height= 4,
                  aspect = 2)

g.map_dataframe(sns.lineplot,
                x = 'Date',
                y = 'values').set(xlabel = "",
                                  ylabel = '%' )
                
plt.annotate('Fonte:elaboração do autor com dados do BCB/SGS ',
             xy = (1.0, -0.13),
             xycoords = 'axes fraction',
             ha = 'right',
             va = "center", 
             fontsize=10)

