facilities = {'Free Parking', 'Pool', 'Gym', 'Spa'}
property_type = {'House', 'Apartment', 'Hote', 'Townhouse', 'Resort'}
amenities = {'Kitchen', 'Air conditioning', 'TV', 'Bathroom'}
disability_access = {'Elevator', 'Ramp', 'Travelator'}
reviews = {'Excellent', 'Good', 'Okay', 'Mediocre', 'Poor'}

def filter_by_facilities(filter_facilities_form, searching):
    # checkbox boolean
    free_parking = filter_facilities_form.cleaned_data['free_parking']
    pool = filter_facilities_form.cleaned_data['pool']
    gym = filter_facilities_form.cleaned_data['gym']
    spa = filter_facilities_form.cleaned_data['spa']

    #special case: all false return list as normal
    change_list = False
    i = 0
    while (i < 1):
        if (free_parking == True):
            change_list = True
            break
        if (pool == True):
            change_list = True
            break
        if (gym == True):
            change_list = True
            break
        if (spa == True):
            change_list = True
            break
        i += 1

    if (not change_list):
        return searching
  
    # filtering when there is atleast 1 true
    filtered = []
    for s in searching:
        if (free_parking == True and s.free_parking == True):
            filtered.append(s)
            continue
        if (pool == True and  s.pool == True):
            filtered.append(s)
            continue
        if (gym == True and s.gym == True):
            filtered.append(s)
            continue
        if (spa == True and s.spa == True):
            filtered.append(s)
            continue

    return filtered
