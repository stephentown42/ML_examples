""" Use Gradient-boosted trees to classify task-related variables using neural activity """

from pathlib import Path
import sys
from typing import List

import h5py
import numpy as np
import pandas as pd


sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib import utils


def get_trial_data(ferret:int, region:str, electrode:int, depth:float) -> pd.DataFrame:
    """ Get recording file, trigger time and metadata for every trial on which a 
    partiular recording site was tested 

    """

    query = f"""
        SELECT 
            rs.start_date,
            s.datetime,
            rf.h5_file,
            m.starttime,
            m.mcs AS mcs_triggertime,
            stim.modality,
            tt.response
        FROM task_switch.recording_sites rs
        INNER JOIN
            task_switch.sessions s
            ON rs.ferret = s.ferret
        INNER JOIN
            task_switch.recording_files rf
            ON rf.region = rs.region
            AND rf.session_dt = s.datetime
        INNER JOIN
            task_switch.mcs_trials_20230219 m
            ON s.datetime = m.session_dt
        INNER JOIN
            task_switch.trials t
            ON t.session_dt = m.session_dt
            AND t.starttime = m.starttime
        INNER JOIN
            task_switch.stimuli stim 
            ON t.stim_id = stim.id
        INNER JOIN
            task_switch.trial_types tt
            ON t.trialtype_id = tt.id
        WHERE
            rs.ferret = %s
            AND rs.region = %s
            AND rs.electrode = %s
            AND rs.depth = %s
            AND s.datetime BETWEEN
                rs.start_date
                AND rs.end_date
        ORDER BY
            s.datetime,
            m.mcs;
    """

    df = utils.query_postgres(query, [ferret, region, electrode, depth])

    if df.shape[0] == 0:
        raise ValueError(f"No data found for f{ferret}, {region}, EL{electrode:02d} at {depth} mm ")

    return df


def create_sim_data(nTrials:int=100, nConditions:int=2) -> pd.DataFrame:
    """ Create a simple simulation dataset with which to test """
    raise NotImplementedError()  # Would it be better to load a sample SKlearn dataset


def load_spike_data(filepath:str, rec_files:List[str], chan:int) -> dict:
    """ Load spike times from hdf5 file organised by recording session / channel 
    
    Args:
        spike_file: path to hdf5 file containing spike times for each neuron and each recording file
        rec_files: names of recording files during which a neuron was studied
        chan: channel identifier for neuron
    
    Returns:
        Dictionary containing arrays of spike times (values) for each recording file (keys)
    """

    chan = f"chan{chan:02d}"
    spikes = dict()

    with h5py.File(filepath,'r') as f:

        for file_ in rec_files: 

            spike_times = f[file_.replace('.h5','')][chan][:]

            # Convert from microsecond integer to time in seconds as floating point
            spike_times = spike_times.astype(np.float64) / 1e6

            # Assign arrays to dictionary
            spikes[file_] = spike_times

    return spikes


def bin_spikes(trigger_df:pd.DataFrame, spikes:dict, bins:dict) -> np.array:
    """ Bin spikes in time around trigger times 
    
    Args:
        trigger_df: dataframe with columns for...
            - recording_file 
            - trigger time within file "mcs_trigger"
        spikes: dictionary of spike times for one or more recording files
        bins: dictionary containing time bin information
    
    Returns:
        spike_count: numpy array containing the number of spikes in each time bin for each trigger. 

    """
    
    spike_count = np.empty( (trigger_df.shape[0], bins['n']))

    for idx, rowd in trigger_df.iterrows():

        spike_count[idx,:], _ = np.histogram(
            spikes[rowd.h5_file] - rowd.mcs_triggertime,
            bins = bins['n'],
            range = bins['time_range']
        )
    
    return spike_count


def main():
    pass


if __name__ == '__main__':
    main()