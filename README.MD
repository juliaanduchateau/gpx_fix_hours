# Pyhton fix for gpx timestamp offset
---
This script can add/subtract an hour offset to the timestamps in a gpx file.

Example: When I extract the gpx file from my Amazfit Bip watch with the Gadgetbridge app, all the entries are lagging by one hour.

## Usage
```
$ python gpx_fix_hours.py FILENAME [-o OUTPUT_FILENAME] [-t TIME_OFFSET]
```

- output filename default: output.gpx
- time offset default: +1
