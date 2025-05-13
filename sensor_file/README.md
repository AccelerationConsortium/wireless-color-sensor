## This directory contains the files stored on the LCM demo sensor Pico W.

## File Structure Overview

This directory contains both development/test scripts and the core files required to run the LCM demo on the Pico W color sensor package.

### Test Scripts
- `as7341_LED.py`  
- `as7341_test.py`  
These two scripts are intended for development and testing purposes only. They were used during the prototyping phase to verify individual hardware components.

### Core Demo Files
- `main.py`  
  This is the main execution script that runs on the Pico W. It coordinates wireless communication, sensor readings, and response handling for the demo.
  
- `my_secrets.py`  
  This file stores Wi-Fi credentials and other sensitive configuration variables required for network access.
  
- `lib/`  
  This directory contains supporting libraries and modules required by `main.py`. It typically includes drivers and utility functions for handling hardware interactions and network communication.

Only `main.py`, `my_secrets.py`, and the contents of the `lib/` folder are necessary for running the actual LCM demo. The test files can be removed or ignored in a production setup.
