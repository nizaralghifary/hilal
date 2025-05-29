import ephem
from datetime import datetime, timedelta

current_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

moon = ephem.Moon()
sun = ephem.Sun()

observer = ephem.Observer()
observer.lon = '106.816667'
observer.lat = '-6.2'
observer.elevation = 8
observer.horizon = '-0:34'  # Atmospheric refraction correction

previous_altitude = 0

while current_date <= end_date:
    observer.date = current_date

    sunset_time = observer.previous_setting(sun)

    observer.date = sunset_time
    moon.compute(observer)

    altitude = float(moon.alt) / 0.01745329252

    if altitude > 0 and previous_altitude <= 0:
        if altitude > 3:
            print(f"{current_date.year}-{current_date.month}-{current_date.day}: Masuk bulan baru. Ketinggian bulan: {altitude:.2f}°")
        else:
            print(f"{current_date.year}-{current_date.month}-{current_date.day}: Muhammadiyah masuk bulan baru, pemerintah tergantung rukyat. Ketinggian bulan: {altitude:.2f}°")

    previous_altitude = altitude
    current_date += timedelta(days=1)