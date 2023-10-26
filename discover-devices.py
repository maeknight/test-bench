#!./python/bin/python
"""
list all devices discoverable by pyvisa
"""
import pyvisa

def main():
    rm = pyvisa.ResourceManager('@py')

    for resource in rm.list_resources():
        try:
            device = rm.open_resource(resource)
            device.baud_rate = 115200
            
            info = device.query("*idn?").strip().split(',');
            
            print("{} {} (s/n {}):".format(info[0], info[1], info[2]))
            print("    {}".format(resource))
        except:
            pass

if __name__ == '__main__':
    main();
