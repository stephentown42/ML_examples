# Single Unit Analysis

The questions here relate to the functional properties of individual neurons. When in a trial is a unit most active? How is activity modulated by different experimental conditions? 

On the technical side, how do we relate behavior and task to neural activity? Do we bin spike rates in some window and try a generalized linear model (GLM) or some other non-linear machine learning approach to predict spike counts?


## Channels of interest

Electrodes on which interesting activity is observed and may be interesting to persue

### PFC

#### 1602
Channel 01, 03

#### F1605
Channel 09, 11, 14 - Config 06

#### F1607
02 May 2017: Looks like interesting activity but very similar across several electrodes... is this just how those probes work?


#### F1613

Config 39, C12
Config 43: C06, C14
Config 44: C05, C10



### Auditory Cortex

* F1518: Nice examples on many channels (not hugely stable, may need some investigation of extraction thresholds)


## Notes:

The PSTHs are somewhat variable still, even after debugging certain issues. We may want to find a way to identify when signals get lost, as sound driven responses are often observed, then lost, then reappear again. Stability can last many weeks, suggesting that either the units are dropping in/out, or that there's an issue with the extraction process.

