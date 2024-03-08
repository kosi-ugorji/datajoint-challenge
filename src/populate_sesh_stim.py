def populate_sesh_stim(sesh_list, Session, Stimulation):
    for sesh in sesh_list:
        Session.insert1({'subject_name': sesh["subject_name"],'session_date': sesh["session_date"],'sample_number': sesh["sample_number"]}, skip_duplicates=True)
        stim_count = 0
        for stim in sesh['stimulations']:
            stim_count +=1
            stim_to_insert = {
                'stim_id': stim_count,
                'subject_name': sesh["subject_name"],
                'sample_number': sesh["sample_number"],
                'session_date': sesh["session_date"],
                **stim
            }
            del stim_to_insert["spikes"]
            Stimulation.insert1(stim_to_insert, skip_duplicates=True)
