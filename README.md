# Owon Programmable DC Power Supply textfile collector script for Prometheus node_exporter

## Usage
These script are to be used with the Node Exporter textfile collector.

Export `OWON_PSU_PORT` environment variable
```bash
OWON_PSU_PORT=/dev/tty.usbserial-1440
```

## Example output
```
# HELP psu_measured_voltage Measured Voltage (Volts)
# TYPE psu_measured_voltage gauge
psu_measured_voltage{device="22472129"} 12.033
# HELP psu_measured_current Measured Current (Amper)
# TYPE psu_measured_current gauge
psu_measured_current{device="22472129"} 1.129
# HELP psu_device_info Device information
# TYPE psu_device_info gauge
psu_device_info{firmware_version="V4.1.0",manufacturer="OWON",model="SPE3051",serial_num="22472129"} 1.0
```

For more information see: https://github.com/prometheus/node_exporter#textfile-collector