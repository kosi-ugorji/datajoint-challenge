import datajoint as dj
import numpy as np
import pickle
import organize_mouse_session, populate_neuron, populate_sesh_stim, visualize_sta
from data_creation import Mouse, Session, Stimulation, NeuronSpikes

schema = dj.schema('send')

@schema
class Mouse(dj.Manual):
    definition = """
    # Experimental animals
    subject_name                  : varchar(100)         # Unique subject name
    ---
    count                         : int                  # sessions count.
    """


# This defines a session database.
@schema
class Session(dj.Manual):
    definition = """
    # Each session
    -> Mouse
    sample_number               : int                         # the sample number
    session_date                : datetime                    # the session date

    ---
    session_date                : datetime                    # the session date
    """

# This represents a stimulation database.
@schema
class Stimulation(dj.Manual):
    definition = """
    # Each Session
    -> Session
    stim_id                    : int                          # stim id
    ---
    stimulus_onset             : int                          # stimulus onset
    fps                        : int                          # movie recording frequency in frames per second
    movie                      : longblob                     # movie
    n_frames                   : int                          # number of frames
    pixel_size                 : int                          # pixel size on the retina in um/pixel
    stim_height                : int                          # the height of the stimulus (movie) in pixels
    stim_width                 : int                          # the width of the stimulus (movie) in pixels
    x_block_size               : int                          # size of x (horizontal) blocks in pixels
    y_block_size               : int                          # size of y (vertical) blocks in pixels
    """

@schema
class NeuronSpikes(dj.Manual):
    
    definition = """
    # Each Session
    -> Stimulation
    neuron_num                    : int                          # stim id
    ---
    spike_times                   : blob                         # the neuron spike
    summed_movie                  :blob                          # spike triggered averaging output
    """

# Load the dataset from a file
    
with open('data/ret1_data.pkl', 'rb') as file:
    sesh_list = pickle.load(file)
big_list = organize_mouse_session(sesh_list)
Mouse.insert(big_list, skip_duplicates=True)
populate_sesh_stim(sesh_list, Session, Stimulation)
populate_neuron(sesh_list, NeuronSpikes)
