#!/usr/bin/env python3
#
# Prometheus node_exporter textfile collector for Owon Programmable DC Power Supply
# (c) 2024, Andrew Dorokhin https://github.com/dorokhin
#
# You can find the latest version at:
# https://github.com/dorokhin/node-exporter-owon-psu-textfile-collector-script
#

from owon_psu import OwonPSU
from prometheus_client import CollectorRegistry, Counter, Gauge, Info, generate_latest  # noqa: E402
import os

registry = CollectorRegistry()
namespace = 'psu'


metrics = {
    'measured_voltage': Gauge(
        'measured_voltage',
        'Measured Voltage (Volts)',
        ['device'], namespace=namespace, registry=registry,
    ),
    'measured_current': Gauge(
        'measured_current',
        'Measured Current (Ampere)',
        ['device'], namespace=namespace, registry=registry,
    ),
    'device_info': Info(
        'device',
        'Device information',
        ['manufacturer', 'model', 'serial_num', 'firmware_version'], namespace=namespace, registry=registry,
    ),
}


def main():
    device_port = os.environ.get('OWON_PSU_PORT', '/dev/tty.usbserial-1440')
    with OwonPSU(device_port) as opsu:
        manufacturer, model, serial_num, firmware_version = opsu.read_identity().split(',')
        firmware_version = firmware_version.split(':')[1]
        metrics['device_info'].labels(
            manufacturer,
            model,
            serial_num,
            firmware_version,
        )

        metrics['measured_voltage'].labels(serial_num).set(opsu.measure_voltage())
        metrics['measured_current'].labels(serial_num).set(opsu.measure_current())


if __name__ == '__main__':
    main()
    print(generate_latest(registry).decode(), end="")
