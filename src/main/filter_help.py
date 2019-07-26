reviews = {'Excellent', 'Good', 'Okay', 'Mediocre', 'Poor'}

def filter_by_facilities(filter_facilities_form, searching):
    filter_facilities_form.is_valid()
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

def filter_by_disability_access(disability_access_form, searching):
    disability_access_form.is_valid()
    # checkbox boolean
    ramp = disability_access_form.cleaned_data['ramp']
    travelator = disability_access_form.cleaned_data['travelator']
    elevator = disability_access_form.cleaned_data['elevator']

    #special case: all false return list as normal
    change_list = False
    i = 0
    while (i < 1):
        if (ramp == True):
            change_list = True
            break
        if (travelator == True):
            change_list = True
            break
        if (elevator == True):
            change_list = True
            break
        i += 1

    if (not change_list):
        return searching
  
    # filtering when there is atleast 1 true
    filtered = []
    for s in searching:
        if (ramp == True and s.ramp == True):
            filtered.append(s)
            continue
        if (travelator == True and  s.travelator == True):
            filtered.append(s)
            continue
        if (elevator == True and s.elevator == True):
            filtered.append(s)
            continue
    return filtered

def filter_by_property_type(property_type_form, searching):
    property_type_form.is_valid()
    # checkbox boolean
    apartment = property_type_form.cleaned_data['apartment']
    hotel = property_type_form.cleaned_data['hotel']
    resort = property_type_form.cleaned_data['resort']
    house = property_type_form.cleaned_data['house']
    townhouse = property_type_form.cleaned_data['townhouse']

    #special case: all false return list as normal
    change_list = False
    i = 0
    while (i < 1):
        if (apartment == True):
            change_list = True
            break
        if (hotel == True):
            change_list = True
            break
        if (resort == True):
            change_list = True
            break
        if (house == True):
            change_list = True
            break
        if (townhouse == True):
            change_list = True
            break
        i += 1

    if (not change_list):
        return searching
  
    # filtering when there is atleast 1 true
    filtered = []
    for s in searching:
        if (apartment == True and s.apartment == True):
            filtered.append(s)
            continue
        if (hotel == True and  s.hotel == True):
            filtered.append(s)
            continue
        if (resort == True and s.resort == True):
            filtered.append(s)
            continue
        if (house == True and s.house == True):
            filtered.append(s)
            continue
        if (townhouse == True and s.townhouse == True):
            filtered.append(s)
            continue
    return filtered

def filter_by_amenities(amenities_form, searching):
    amenities_form.is_valid()
    # checkbox boolean
    kitchen = amenities_form.cleaned_data['kitchen']
    airconditioning = amenities_form.cleaned_data['airconditioning']
    tv = amenities_form.cleaned_data['tv']
    bathroom = amenities_form.cleaned_data['bathroom']

    #special case: all false return list as normal
    change_list = False
    i = 0
    while (i < 1):
        if (kitchen == True):
            change_list = True
            break
        if (airconditioning == True):
            change_list = True
            break
        if (tv == True):
            change_list = True
            break
        if (bathroom == True):
            change_list = True
            break
        i += 1

    if (not change_list):
        return searching
  
    # filtering when there is atleast 1 true
    filtered = []
    for s in searching:
        if (kitchen == True and s.kitchen == True):
            filtered.append(s)
            continue
        if (airconditioning == True and  s.airconditioning == True):
            filtered.append(s)
            continue
        if (tv == True and s.tv == True):
            filtered.append(s)
            continue
        if (bathroom == True and s.bathroom == True):
            filtered.append(s)
            continue
    return filtered
