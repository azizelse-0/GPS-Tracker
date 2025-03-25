# **GPS Tracker**  

A real-time GPS tracking system using an Arduino-compatible GPS module and Python for data processing and visualization. This project reads raw GPS data, extracts latitude and longitude, and continuously updates a map to visualize the tracked movement.  

## **Features**  
- Parses real-time GPS data from the serial port.  
- Extracts latitude and longitude from NMEA sentences.  
- Displays the GPS path on an interactive map.  
- Updates the map dynamically without opening a new tab each time.  
- Saves location data for historical tracking.  

## **Getting Started**  

### **Prerequisites**  
- **Arduino IDE** (For configuring the GPS module)  
- **Python 3.x** (For processing data and map visualization)  
- Required Python libraries:  
  ```sh
  pip install pyserial folium
  ```  

### **Hardware Requirements**  
- BN-280 GPS Module (or any NMEA-compatible GPS module)  
- Arduino Board (e.g., Arduino Uno)  
- USB cable for serial communication  

### **Installation & Usage**  

1. **Clone the Repository:**  
   ```sh
   git clone https://github.com/azizelse-0/GPS-Tracker.git
   cd GPS-Tracker
   ```

2. **Connect your GPS module to the Arduino and upload the given sketch.**  (don't forget to close Arduino IDE before running the script, as it will interfere with the program)
3. **Run the Python script to start tracking:**  
   ```sh
   python main.py
   ```
4. The script will parse GPS data and continuously update **gps_map.html** with the latest location.

## **How It Works**  
1. Reads raw NMEA data from the GPS module via the serial port.  
2. Extracts latitude and longitude from `$GNGGA` or `$GNRMC` sentences.  
3. Updates the **gps_map.html** file with the new position.  
4. Visualizes the GPS path using **Folium**.  

## **License**  
This project is licensed under the MIT License.  
