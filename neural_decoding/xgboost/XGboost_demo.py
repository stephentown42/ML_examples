""" Use XGBoost to classify task-related variables using neural activity 

The demo script prints to the console the accuracy in decoding the modality of stimuli (auditory or visual) presented to a subject from responses of a single neuron. The configuration file contains details of the specific neuron being shown here, and can be changed to any in the dataset (or in future integrated as part of an online dashboard).

Available recording sites are listed publicly at: https://public.tableau.com/app/profile/stephen.town3919/viz/ElectrodeDepths/Dashboard1

Also returned is a chart with two rows that show (top) the response of the neuron to auditory and visual stimuli as a function of time, and (bottom) the Gini importance values fitted by the model to each time bin. 

We are specifically interested in the ability to identify time periods of neural activity that are particularly informative about stimulus information.
"""

import json
import os
from pathlib import Path
import sys
from typing import List

from dotenv import load_dotenv
import h5py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xgboost as xgb

from sklearn.preprocessing import LabelEncoder  
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier

sys.path.insert(0, str(Path.cwd()))

from lib import utils
from lib import plot_utils as cplot
from analysis.xgboost import xgboost_preproc as pproc

# Load environmental settings for repository
load_dotenv()

def main():

    # Load config 
    with open('analysis/xgboost/XGBoost_config.json') as fp:
        config = json.load(fp)

    # Load data for unimodal trials
    trigger_df = pproc.get_trial_data(config['ferret'], config['region'], config['electrode'], config['depth'])
    trigger_df = trigger_df[trigger_df.modality != 'Audiovisual'].reset_index(drop=True)

    # Load times of spikes for each recording file
    spiketime_filepath = Path(os.getenv("local_home")) / config['spiketime_file']
    
    spikes = pproc.load_spike_data(
        filepath = str(spiketime_filepath), 
        rec_files = list(trigger_df.h5_file.unique()), 
        chan = utils.electrode_2_channel(config['electrode'], config['chan_map']))

    # Count spikes in time bins around times of stimulus presentation
    bins = cplot.create_bins((config['bin_start'], config['bin_end']), config['bin_width'])

    spike_counts = pproc.bin_spikes(trigger_df, spikes, bins)

    # Split the dataset
    le = LabelEncoder()
    trial_labels = le.fit_transform(trigger_df.modality)

    # Run in cross-validation
    kf = KFold(n_splits=config['k_folds'], shuffle=True, random_state=35)
    kf.get_n_splits(spike_counts)
    
    scores = []
    feature_importances = []

    for train_idx, test_idx in kf.split(spike_counts):
        
        X_train, X_test = spike_counts[train_idx], spike_counts[test_idx]
        y_train, y_test = trial_labels[train_idx], trial_labels[test_idx]

        xgb_cl = xgb.XGBClassifier(**config['xgb_params'])
        xgb_cl.fit(X_train, y_train)

        ypred = xgb_cl.predict(X_test)
        
        feature_importances.append(
            xgb_cl.feature_importances_
            )

        scores.append(
            accuracy_score(y_test, ypred)
        )

    print(scores)

    # Compare feature importances to underlying data_
    fig, ax = plt.subplots(2,1)

    for y in np.unique(y_train):
        ax[0].plot(
            bins['centers'], 
            np.mean(X_train[y_train == y, :], axis=0),
            label=str(y))

    ax[0].set_ylabel('Mean spike count')

    for fi in feature_importances:
        ax[1].plot(bins['centers'], fi, alpha=0.2)
    
    ax[1].set_xlabel('Time w.r.t. stimulus')
    ax[1].set_ylabel('Importance')

    plt.show()




if __name__ == '__main__':
    main()