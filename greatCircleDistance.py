distance = [14209.77, 10437.78, 11776.04, 12169.73, 8959.52, 11581.72, 18580.34, 17766.56, 17198.30, 13402.11, 16353.61, 2158.32, 9583.26, 14054.82, 12285.36, 16760.07, 16246.46, 18398.15, 12638.95, 13852.65]
velocity = [0]*20
for i in range(len(distance)):
	velocity[i] = round((distance[i]*2*1000)/(3*10**8),2)
print(velocity)
