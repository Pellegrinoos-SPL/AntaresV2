# AntaresV2
Our almost-passive flight computer

## What is Antares?

Antares is the name of our brand-new flight computer, mostly designed for modular rockets like Baine (we'll publish more things about it in the neext months)
Here we released the second version of Antares, skipping the first one because it was still a developing thing.
The improvements from the first version are a 62% mass reduction (from 103g to only 40g), a smaller size (from 16.2 cm to just 5.6cm), and a fastest processing.

## Assembly

The assembly of Antares V2 is very straight forward, only needing 
- some wires
- RP2040-Zero
- MPU6050
- 4x LR44 1.55v batteries
- 1x 3x14mm screw
- 2x 2.5x6 screws
- Hot glue
- 3D printed parts
- 9g servo motor (optional)

This doesn't look like a short list, but most of the parts are really cheap!

For the assembly, first print out all the parts.

After, solder all the circuits like in the image below:
![Circuits](https://raw.githubusercontent.com/Pellegrinoos-SPL/AntaresV2/main/images/Antares%20V2.png)

You'll notice that just 3 of the 4 batteries are really connected to the circuit. That's because you'll use the 4th one to get a 6v output required by a servo motor (optional) to work and deploy a parachute (We'll release the parts for the parachute in a future repository).

Lastly, just install micropython on the RP2040-Zero and copy and paste the code to get everything working.

The code uses a preinstalled neopixel on the RP2040-Zero connected on pin 16, but if you need to, feel free to add another one on a custom pin. Just rember to change the config file!

# Disclaimer

This software is provided for educational and hobbyist purposes only. It is your responsibility to ensure the safe operation of your model rocket.

### Use at Your Own Risk

Building and flying a model rocket inherently carries risks. This software is provided "as is" without warranty of any kind, expressed or implied. The authors and contributors shall not be held liable for any damages arising from the use of this software, including but not limited to property damage, personal injury, or death.

### Safety Precautions

- Always follow the National Association of Rocketry (NAR) Safety Code https://www.nar.org/safety-codes-2/.
- Double and triple-check all hardware connections before flight.
- Ensure your launch site is clear of hazards and bystanders.
- Inspect your rocket and parachute thoroughly before each flight.
- Never modify commercially available motors beyond manufacturer specifications.
- Only use approved launch stands and recovery systems.
- Parachute Deployment

The reliability of parachute deployment depends on various factors beyond the software's control. These include parachute quality, packing technique, and environmental conditions. It is your responsibility to ensure the parachute is properly packed and deployed during flight.

By using this software, you acknowledge and accept these terms and conditions.
