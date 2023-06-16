print("PR KONVERSI SUHU")

print("===FAHRENHEIT TO KELVIN===")
fahrenheit = float(input('Masukan suhu dalam fahrenheit : '))
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

kelvin = (5/9) * (fahrenheit - 32) + 273.15
print("suhu dalam kelvin adalah", kelvin, "Kelvin")

print("===KELVIN TO FAHRENHEIT===")
kelvin = float(input('Masukan suhu dalam kelvin : '))
print("suhu dalam kelvin adalah",kelvin, "Kelvin")

fahrenheit = (9/5) * (kelvin - 273.15) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")