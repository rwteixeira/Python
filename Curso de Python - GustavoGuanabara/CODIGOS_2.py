# Esse código utiliza uma função definida em 'temperature.py'
import temperature
temperature.TEMPERATURE_SCALES
('fahrenheit', 'kelvin', 'celsius')
temp = float(input("Temperatura: "))
escala = "fahrenheit"
# temperature.convert_to_celsius(120, "fahrenheit")

print(temperature.convert_to_celsius(temp, escala))
if escala == "fahrenheit":
    print("fahrenheit")
elif escala == "kelvin":
    print("kelvin")
else:
    print("Sem conversão!")
