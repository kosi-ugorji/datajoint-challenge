import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import visualize_sta
from data_creation import NeuronSpikes


subj_name = "KO (pax6)";
sesh_date = "2008-05-16";
neuron_num = 1;
visualize_sta(NeuronSpikes, subj_name, sesh_date, neuron_num)

