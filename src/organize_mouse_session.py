# Make it so that each mouse appears only once.

def organize_mouse_session(sesh_list):
    '''
    This function finds the count of a particular mouse to aid in populating the mouse database
    Input: sesh_list - This is the data given 
    Output: big_list- This is the organized list of dictionaries containing two key-value pairs: subject_name and count. 
    '''
    big_list = []

    unique_mice = []
    for dict_item in sesh_list:

        subj_name = dict_item["subject_name"] 
        if subj_name not in unique_mice:
            big_dict = {}
            big_dict["subject_name"] = subj_name
            big_dict["count"] = 1
            big_list.append(big_dict)
            unique_mice.append(subj_name)
        else:
            big_dict["count"] +=1

    return big_list