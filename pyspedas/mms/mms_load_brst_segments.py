
import os
import logging
import numpy as np
from scipy.io import readsav
from pytplot import store_data, options

from pyspedas import time_double
from pyspedas.utilities.download import download
from pyspedas.mms.mms_config import CONFIG

logging.captureWarnings(True)
logging.basicConfig(format='%(asctime)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

def mms_load_brst_segments(trange=None):
    '''
    This function loads the burst segment intervals
    
    Parameters:
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']

    Returns:
        Tuple containing (start_times, end_times)

    '''

    if trange == None:
        logging.error('Error; no trange specified.')
        return None

    tr = time_double(trange)

    save_file = os.path.join(CONFIG['local_data_dir'], 'mms_brst_intervals.sav')
    brst_file = download(remote_file='http://www.spedas.org/mms/mms_brst_intervals.sav',
        local_file=save_file)

    try:
        intervals = readsav(save_file)
    except FileNotFoundError:
        logging.error('Error loading burst intervals sav file: ' + save_file)
        return None

    unix_start = intervals['brst_intervals'].start_times[0]
    unix_end = intervals['brst_intervals'].end_times[0]

    sorted_idxs = np.argsort(unix_start)
    unix_start = unix_start[sorted_idxs]
    unix_end = unix_end[sorted_idxs]

    times_in_range = (unix_start >= tr[0]-300.0) & (unix_start <= tr[1]+300.0)

    unix_start = unix_start[times_in_range]
    unix_end = unix_end[times_in_range]

    # +10 second offset added; there appears to be an extra 10
    # seconds of data, consistently, not included in the range here
    unix_end = [end_time+10.0 for end_time in unix_end]

    bar_x = []
    bar_y = []

    for start_time, end_time in zip(unix_start, unix_end):
        if end_time >= tr[0] and start_time <= tr[1]:
            bar_x.extend([start_time, start_time, end_time, end_time])
            bar_y.extend([np.nan, 0., 0., np.nan])

    return (unix_start, unix_end)
