def human_years_cat_years_dog_years(human_years):
   cat = 0
   dog = 0
   counter = 1
   for i in range(human_years):
        if counter == 1:
            cat+=15
            dog+=15
            counter+=1
            continue
        if counter == 2:
            cat += 9
            dog += 9
            counter+= 1
            continue
        cat +=4
        dog+=5
        return [human_years,cat,dog]
    
print(human_years_cat_years_dog_years(1))