class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance
    def MeterCentimeter(self):
        print(self.__distance * 100, "Centimeters")
    def MeterKilometer(self):
        print(self.__distance / 1000, "Kilometers")
    def MeterInches(self):
        print(self.__distance * 39.37, "Inches")

Measure = DistanceConversion(float(input("Enter the measurement in Meters: ")))
Measure.MeterCentimeter()
Measure.MeterKilometer()
Measure.MeterInches()
