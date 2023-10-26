# test bench scripts

these are scripts for the gear on my test bench:

- owon xdm1241 multimeter
  uses a usb serial port connection for scpi
- owon dge2070 arbitrary waveform generator
  uses usbtmc connection for scpi

## how to use

first, set up a virtual python environment within the
`test-bench` directory:

```sh
python -m venv ./python
```

then install the following packages within the environment:

```sh
./python/bin/pip install pyvisa
./python/bin/pip install pyvisa-py
./python/bin/pip install pyusb
./python/bin/pip install python-usbtmc
./python/bin/pip install psutil
./python/bin/pip install zeroconf
```

then run `./discover-devices.py` in order to find the
connection strings used for your specific devices, you
can then add your devices to the `connections.py` file
to enable the scripts to find them.