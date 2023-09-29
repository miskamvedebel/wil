-- https://datalemur.com/questions/pizzas-topping-cost

WITH two_toppings AS (
SELECT distinct concat(pt1.topping_name, ','
  , pt2.topping_name, ','
  , pt3.topping_name) as pizza
  , pt1.ingredient_cost + pt2.ingredient_cost + pt3.ingredient_cost as total_cost
FROM pizza_toppings pt1
  cross join pizza_toppings pt2
  cross join pizza_toppings pt3
WHERE pt1.topping_name < pt2.topping_name 
  AND pt2.topping_name < pt3.topping_name)
SELECT * 
FROM two_toppings
ORDER BY 2 DESC, pizza ASC