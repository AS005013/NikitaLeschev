from gpio import *
from time import *

def main():
	pinMode(1, IN)
	pinMode(2, OUT)
	pinMode(3, OUT)
	while True:
		div = (analogRead(1)/1023)*200 - 100
		if  div < 20:
			digitalWrite(2, HIGH)
			digitalWrite(3, LOW)
		elif div > 25:
			digitalWrite(2, LOW)
			digitalWrite(3, HIGH)
		else:
			digitalWrite(2, LOW)
			digitalWrite(3, LOW)
			

if __name__ == "__main__":
	main()
