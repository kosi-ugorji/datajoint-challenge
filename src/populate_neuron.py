# Make dataset for neuron  
# problem: the spike times are often longer than the stimulus.
import numpy as np

def populate_neuron(sesh_list, NeuronSpikes):
    for sesh in sesh_list:
        stim_count = 0
        for stim in sesh['stimulations']:
            stim_count +=1
            neuron_count = 0
            for neuron_spike_times in stim["spikes"]:
                neuron_count +=1
                neuron_new = (neuron_spike_times)*stim['fps']
                adjusted_indices = [np.arange( index-4, index-1, dtype=int) for index in neuron_new if index < stim['n_frames'] and index >stim['stimulus_onset']]
                movie_mats = stim['movie'][:,:,adjusted_indices]
                mean_stim = np.mean(stim['movie'],2)
                # sta formula: 1/no_spikes*sum(stimulus*spike_count)
                summed_movie = np.sum(movie_mats-mean_stim,2)/len(neuron_spike_times) 
                item_to_add = {
                'stim_id': stim_count,
                'subject_name': sesh["subject_name"],
                'session_date': sesh["session_date"],
                'sample_number': sesh["sample_number"],
                "neuron_num": neuron_count,
                "spike_times": neuron_spike_times,
                "summed_movie": summed_movie}
                NeuronSpikes.insert1(item_to_add, skip_duplicates=True)