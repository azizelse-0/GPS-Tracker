import serial
import folium
import webbrowser
import os
import time
import re

SERIAL_PORT = "COM4"
BAUD_RATE = 9600
MAP_FILE = os.path.expanduser("~/Desktop/gps_map.html")

location_history = []

def parse_nmea(sentence):
    match = re.match(r"^\$(GNRMC|GNGGA),[^,]*,A,(\d{2})(\d{2}\.\d+),([NS]),(\d{3})(\d{2}\.\d+),([EW])", sentence)
    if not match:
        return None

    lat_deg, lat_min, lat_dir = int(match[2]), float(match[3]), match[4]
    lon_deg, lon_min, lon_dir = int(match[5]), float(match[6]), match[7]

    latitude = lat_deg + (lat_min / 60)
    longitude = lon_deg + (lon_min / 60)

    if lat_dir == "S":
        latitude = -latitude
    if lon_dir == "W":
        longitude = -longitude

    return latitude, longitude

def update_map():
    if not location_history:
        return

    gps_map = folium.Map(location=location_history[-1], zoom_start=18)

    for lat, lon in location_history:
        folium.Marker([lat, lon], popup=f"{lat}, {lon}").add_to(gps_map)

    folium.PolyLine(location_history, color="blue", weight=3, opacity=0.7).add_to(gps_map)

    gps_map.save(MAP_FILE)

def main():
    print("Connecting to GPS module...")
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)

    if not os.path.exists(MAP_FILE):
        update_map()
    webbrowser.open(MAP_FILE, new=2)

    try:
        while True:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if not line:
                continue
            
            print("Raw GPS Data:", line)

            coords = parse_nmea(line)
            if coords:
                lat, lon = coords
                print(f"Extracted Coordinates: Latitude = {lat}, Longitude = {lon}")

                location_history.append((lat, lon))
                update_map()

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
