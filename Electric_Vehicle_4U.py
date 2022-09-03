from operator import attrgetter

scores = []
prices = []
topSpeeds = []
topRange = []
battCap = []
chargTime = []

def FindBest():
		for i in range(0,len(EVs)): 
			prices.append(EVs[i].Price)
			battCap.append(EVs[i].Battery_capicity)
			topRange.append(EVs[i].Range)
			chargTime.append(EVs[i].Charging_time)
			topSpeeds.append(EVs[i].Top_speed)
					
		prices.sort(reverse=True)
		battCap.sort()
		topRange.sort()
		chargTime.sort()
		topSpeeds.sort()
		
		for i in range(0,len(EVs)):
			for rs in prices:
				if rs == EVs[i].Price:
					EVs[i].Score += prices.index(rs)
					break
			for bc in battCap:
				if bc == EVs[i].Battery_capicity:
					EVs[i].Score += battCap.index(bc)
					break
			for tr in topRange:
				if tr == EVs[i].Range:
					EVs[i].Score += topRange.index(tr)
					break
			for ct in chargTime:
				if ct == EVs[i].Charging_time:
					EVs[i].Score += chargTime.index(ct)
					break
			for ts in topSpeeds:
				if ts == EVs[i].Top_speed:
					EVs[i].Score += topSpeeds.index(ts)
					break
			
			scores.append(EVs[i].Score)
			

def bestEV(arg):
		best = max(EVs, key=attrgetter('Score'))
		worst = min(EVs, key=attrgetter('Score'))
		if arg == "b":
			return f"The best EV (With Price Considered) is \"{best.Name}\"\n"
		else:
			return f"The worst EV (With Price Considered) is \"{worst.Name}\"\n"

class Electric_Vehicle:
	Objects = []
	def __init__(self, name, price, battary_capicity, top_range, charging_Time, top_speed):
		self.Objects.append(self)
		self.Name = name
		self.Price = price
		self.Battery_capicity = battary_capicity
		self.Range = top_range
		self.Charging_time = charging_Time
		self.Top_speed = top_speed
		self.Score = 0
	
		
	def compareWith(self,other):
		if self.Price > other.Price:
			print(f"{other.Name} is cheaper")
		elif self.Price == other.Price:
			print(f"Both {self.Name} and {other.Name} comes at same price")
		else:
			print(f"{self.Name} is cheaper")
		
EVs = Electric_Vehicle.Objects

Ola_s1 = Electric_Vehicle("Ola S1", 97706, 2.98, 121, 5, 90)
TVS_iQube_Electric = Electric_Vehicle("TVS iQube Electric", 92986, 3.04, 75, 5, 78)
Ather_450X = Electric_Vehicle("Ather 450X", 140121, 2.23, 70, 5.45, 80)
Hero_Electric_Photon = Electric_Vehicle("Hero Electric Photon", 80940, 1.87, 108, 5, 45)
Bajaj_Chetak = Electric_Vehicle("Bajaj Chetak", 142297, 3, 90, 5, 70)
Okinawa_Ridge_Plus = Electric_Vehicle("Okinawa Ridge Plus", 69783, 1.75, 120, 3, 55)
Simple_One = Electric_Vehicle("Simple One", 110000, 4.8, 300, 3, 105)
Bounce_Infinity_E1 = Electric_Vehicle("Bounce Infinity E1", 69783, 1.9, 85, 5, 65)
Ampere_V48 = Electric_Vehicle("Ampere V48", 37390, 1.15, 60, 5, 25)
Hero_Electric_Optima_CX = Electric_Vehicle("Hero Electric Optima CX", 62190, 1.5, 82, 5, 45)


FindBest()
while True:
	print(bestEV(input("\n\nType \"b\" to get best EV or type \"w\" to get worst EV\n>>>_")))
