
def calculate(model_gram,filament_price,filament_gram,model_time,kw_price,printer_power,paper_tape,sandpaper):
    #1 gram's calculate
    one_gram_filament=filament_price/filament_gram
    model_price=one_gram_filament*model_gram

    #Electric

    per_watt_price=kw_price*(1/1000)
    electric_price= printer_power*per_watt_price*model_time

    #Addons
    other_stuff=paper_tape+sandpaper

    print("Total cost:",round(model_price+electric_price+other_stuff,3))


calculate(223,150,1000,25,0.70,200,0.2,2)











