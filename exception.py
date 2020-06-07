import pandas as pd
def retrieve_relation_val(person_id,family_df,first_val,second_val):
    relation_val = []
    Family_name = ''
    for i in range(0,len(family_df['Person'])):
        if family_df['Person'][i] == person_id:
            person_row = i
            break
    column_name = family_df.columns.values
    counter = 0
    for j in family_df.loc[person_row]:
        if j == first_val:
            Family_name = column_name[counter]
            break
        counter +=1
    if Family_name == '':
        return relation_val,Family_name
    for i in range(0,len(family_df[Family_name])):
        if family_df[Family_name][i] == second_val:
                relation_val.append(family_df['Person'][i])
    return relation_val,Family_name             


def familyTreeApi(person_id):
        print("person_id is ",person_id)
        family_df = pd.read_csv(r'C:\Users\Sri\Desktop\Simform_coding\FAMILY TABLE - Sheet1.csv')
        family_tree = {'message': 'Success'}
        """
        Retrieving Parents
        """
        parent_val,Parent_Family_name = retrieve_relation_val(person_id,family_df,'C','P')
        if Parent_Family_name == '':
            family_tree['Parent'] = 'No value Found'
        else:
            family_tree['Parent'] = parent_val
        """
        Retrieving Grandparents
        """
        grand_parent_family_list = []
        if Parent_Family_name != '':
            grand_parent = []
            for i in parent_val:
                grand_parent_val,parent_family = retrieve_relation_val(i,family_df,'C','P')
                if parent_family == '' and len(grand_parent) == 0:
                    family_tree['Grandparent'] = 'No value Found'
                else:
                    grand_parent.extend(grand_parent_val)
                    grand_parent_family_list.append(parent_family)
                    family_tree['Grandparent'] = grand_parent
        else:
            family_tree['Grandparent'] = 'No value Found'
        """
        Retrieving Sibling
        """
        if Parent_Family_name != '':     
            sibling = []
            for i in range(0,len(family_df[Parent_Family_name])):
                if family_df[Parent_Family_name][i] == 'C' and family_df['Person'][i]!= person_id:
                        sibling.append(family_df['Person'][i])
            family_tree['Sibling'] = sibling
        else:
            family_tree['Sibling'] = 'No value Found'
        """
        Retrieving Children"""
        children_val,Family_name = retrieve_relation_val(person_id,family_df,'P','C')
        if Family_name != '':
            family_tree['Children'] = children_val
        else:
            family_tree['Children'] = 'No value Found'
        """
        Retrieving Cousin"
        """
        if len(grand_parent_family_list) != 0:
            parents_sibling = []
            cousin = []
            for par_fam in grand_parent_family_list:
                for i in range(0,len(family_df[par_fam])):
                    if family_df[par_fam][i] == 'C' and family_df['Person'][i] not in parent_val:
                        parents_sibling.append(family_df['Person'][i])
            for i in parents_sibling:
                children_val,Family_name = retrieve_relation_val(i,family_df,'P','C')
                if Family_name == '' and len(cousin) == 0:
                    family_tree['Cousin'] = 'No value Found'
                else:
                    cousin.extend(children_val)
                    family_tree['Cousin'] = cousin
        else:
            family_tree['Cousin'] = 'No value Found'
        return family_tree
val = familyTreeApi('P3')
print(val)
    



