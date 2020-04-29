shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill(food):
  total = 0
  for everyItem in food:
    if stock[everyItem] > 0:
        total += prices[everyItem]
        stock[everyItem] -= 1
  return total

compute_bill(shopping_list)