# fetch by subject-name, session-date, neruon_num and display sta plot

import matplotlib.pyplot as plt

def visualize_sta(NeuronSpikes, subj_name, sesh_date, neuron_num):
    summed_movie = (NeuronSpikes & f'subject_name = "{subj_name}"' & f'session_date = "{sesh_date}"' & f'neuron_num = {neuron_num}').fetch('summed_movie')[0]

    plt.figure()
    for i in range(summed_movie.shape[-1]):
        plt.subplot(1, summed_movie.shape[-1],i+1)
        plt.imshow(summed_movie[:,:,i])
    plt.show()
