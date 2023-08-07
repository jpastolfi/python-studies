weight = 41.5;
cost = 0;

# Ground Shipping

ground_shipping_flat = 20;
ground_shipping_cost = 0;

if weight <= 2:
  ground_shipping_cost = ground_shipping_flat + weight * 1.50
elif weight > 2 and weight <= 6:
  ground_shipping_cost = ground_shipping_flat + weight * 3
elif weight > 6 and weight <= 10:
  ground_shipping_cost = ground_shipping_flat + weight * 4
else:
  ground_shipping_cost = ground_shipping_flat + weight * 4.75

print("Ground Shipping would cost $", ground_shipping_cost);

# Premium Ground Shipping

premium_ground_shipping_cost = 125;

print("Premium Ground Shipping would cost $", premium_ground_shipping_cost);

# Drone Shipping

drone_shipping_cost = 0;

if weight <= 2:
  drone_shipping_cost = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_shipping_cost = weight * 9
elif weight > 6 and weight <= 10:
  drone_shipping_cost = weight * 12
else:
  drone_shipping_cost = weight * 14.25

print("Drone Shipping would cost $", drone_shipping_cost);