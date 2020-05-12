def unit_converter(units, total_cost, from_currency, to_currency):
  
  LITERS_PER_GALLON = 3.78541
  GALLONS_PER_LITER = 0.264172
  
  CAD_TO_USD = 0.76
  USD_TO_CAD = 1.31
  
  first = USD_TO_CAD
  second = LITERS_PER_GALLON
  
  if from_currency == "$" and to_currency == "C$":
    first = USD_TO_CAD
    second = LITERS_PER_GALLON
    
  elif from_currency == "C$" and to_currency == "$":
    first = CAD_TO_USD
    second = GALLONS_PER_LITER
    
  elif from_currency == "$" and to_currency == "$":
    first = 1 
    second = 1 
    
  elif from_currency == "C$" and to_currency == "C$":
    first = 1 
    second = 1 
    
  return ((total_cost*first)/(units*second))