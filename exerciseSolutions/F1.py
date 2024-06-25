# 4.	Create a new program called F1.py, it will explore some of the mathematics involved in managing a Formula 1 racing car.
#
# The task of this program (at first), is to answer a question:
# Q.  "During a race of 45 laps, what is the minimum fuel requirement?"
# You will need to know the fuel consumption found during the race qualifying, which is 2.25 kg for each lap.
# 5.	In this exercise, we will make a few more modifications to F1.py. First, we will add an extra fuel load, and then we are going to calculate the lap time based on the weight of fuel,
# which naturally decreases each lap.
#
# a.	In the previous exercise, we worked out the minimum fuel requirement for a 45 lap race and stored this in a variable named fuel_requirement.
# To fill the tank with the absolute minimum amount of fuel would be foolhardy, and not allow the drivers any margin for manoeuvre.
# Typically, a car will carry an extra 50% for contingency (multiply the minimum by 1.5). So what fuel will be carried by our fictional F1 car at the start of the race?
#
# Modify your F1.py program to calculate this.
#
# b.	You might think it odd that fuel is measured in kilograms rather than litres or gallons.  This is because the weight of fuel is critical to the way a Formula One car performs.
#
# The qualifying lap time was 80.45 seconds, but that was with only 5kg of fuel: each 10 kg of fuel increases the lap time by 0.35 seconds.
# What will be the lap time for the first lap with all the required fuel on board?

fuel_per_lap = 2.25
laps = 45

fuel_req = laps * fuel_per_lap
print("Minimum fuel requirement:", fuel_req)

fuel = fuel_req * 1.5
print("Full fuel load:", fuel,"kg")

q_lap_time = 80.45
t_lap_time = q_lap_time - (0.35/10) * 5
print("Theoretical lap time:", t_lap_time)

lap_one = t_lap_time + ((fuel/10)*0.35)
print("Lap one time:", lap_one,"seconds")
