Testing in progress. Forked 

# solaredge-modbus-hass
A custom platform component/sensor for reading SolarEdge Modbus TCP into Home Assistant https://home-assistant.io/

# Benefits compared to Home Assistant built in Modbus component

When reading multiple registers with HA default Modbus, it will do one reading per register.

SolarEdge that use a sunspec implementation (https://www.solaredge.com/sites/default/files/sunspec-implementation-technical-note.pdf) send values in one register and the scale factor in another.

This means that for example 20 watts can be represented using a value of 20000 and a scale factor or -3 so that 20000 * 10^-3 = 20

The problem that occur if reading lots of registers with one reading each, is that the SolarEdge inverter can actually change the scale factor between two of the readings done by Home Assistant, such as you first get 20000 in the value, then before the next reading is complete the sun can quickly make your inverter produce more energy changing both value and the scale factor so when HA read the scale factor it could become -2 instead, then when calculating the final result you'll end up with a factor 10 or more incorrect value.

This component reads all registers every reading to make sure it can't get out of sync!

# How to install

Though HACS:


Or manual install:
Copy custom_components/solaredge_modbus to your hass data directory (where your configuration.yaml lives). It should go into the same directory structure (YOUR_CONFIG_DIRECTORY/custom_components/solaredge_modbus)

See sample-configuration.yaml for information how to configure, and how to extract attributes into custom template sensors.

# Enable readings from external RS485 meter

Just add "read_meter1: true" to the configuration block. For now it only supports one external meter for getting values such as current (own) power consumption, grid power, etc.... so you can calculate your own consumption from the solar panels and import/export for example. Thanks to [awulf](https://github.com/awulf) for contributing with code and testing for this feature.

