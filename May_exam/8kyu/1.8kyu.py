def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    elif human_years == 2:
        return [2, 24, 24]
    
    cat_perspective = 24
    dog_perspective = 24

    for year in range(3, human_years + 1):

        cat_perspective += 4
        dog_perspective += 5
        
    return [human_years, cat_perspective, dog_perspective]

print(human_years_cat_years_dog_years(1))