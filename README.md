# Amazfit Watchfaces

A collection of custom watchfaces for Amazfit smartwatches, featuring modern designs with comprehensive data visualization and health metrics.

## Overview

This repository contains carefully crafted watchface designs optimized for Amazfit devices. Each watchface is meticulously configured with weather information, activity metrics, health indicators, and time display functionality.

## Watchfaces Included

### Bip Max

#### Overview
A feature-rich watchface designed for the Amazfit Bip Max, providing a comprehensive overview of your daily metrics and environmental data.

**Features:**
- Current weather temperature and conditions
- Humidity and UV index display
- PAI (Personal Activity Intelligence) score and progress
- Stand hours tracking with target goals
- Health status indicators (Bluetooth, Alarm, Do Not Disturb, Lock status)
- Clean, readable typography with Rajdhani font family
- High-contrast white text for visibility

**Preview:**
![Overview Preview](https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/bip%20max/Overview/Preview.png)

![Overview Animation](https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/bip%20max/Overview/Preview.gif)

**Display Layout:**
- **Top Section:** Humidity, Weather temperature, UV Index
- **Middle Section:** Time and status icons
- **Bottom Section:** PAI progress (left), Stand hours (center), Activity targets (right)

#### Overview - Text Only
A simplified text-focused variant of the Overview watchface, emphasizing legibility with minimal visual elements.

**Features:**
- Clean text-based interface for maximum readability
- All essential metrics in text format
- Minimalist design approach
- Monochrome white text on dark background
- Optimized for users who prefer simplicity over graphical elements

**Preview:**
![Overview Text Only Preview](https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/bip%20max/Overview-TextOnly/Preview.png)

![Overview Text Only Animation](https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/bip%20max/Overview-TextOnly/Preview.gif)

#### Overview - Colourful
A vibrant text-based variant of the Overview watchface that maintains the simplicity and readability of the Text Only version while adding colorful data visualization.

**Features:**
- Clean text-based interface with color-coded metrics
- Color-enhanced data values for better visual distinction
- Minimalist design with visual personality
- Each metric displayed in its own distinctive color
- Optimized for users who want clarity with visual flair

**Preview:**
![Overview Colourful Preview](https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/bip%20max/Overview-Colourful/Preview.png)

![Overview Colourful Animation](https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/bip%20max/Overview-Colourful/Preview.gif)

---

## Project Structure

```
Amazfit-Watchfaces/
├── README.md
├── LICENSE
├── .gitignore
└── src/
    └── bip max/
        ├── Overview/
        │   ├── Overview.json          # Watchface configuration
        │   ├── Preview.png            # Static preview image
        │   ├── Preview.gif            # Animated preview
        │   └── assets/                # Additional resources
        ├── Overview-TextOnly/
        │   ├── Overview-TextOnly.json  # Watchface configuration
        │   ├── Preview.png             # Static preview image
        │   ├── Preview.gif             # Animated preview
        │   └── assets/                 # Additional resources
        └── Overview-Colourful/
            ├── Overview-Colourful.json # Watchface configuration
            ├── Preview.png             # Static preview image
            ├── Preview.gif             # Animated preview
            └── assets/                 # Additional resources
```

## Technical Details

### Watchface Configuration

Each watchface is defined by a JSON configuration file that specifies:

- **Device Information:** Device name, watchface ID, and version
- **Screen Elements:** Layout and positioning of all display components
- **Typography:** Font families, sizes, colors, and alignment
- **Metrics Display:** Configuration for health data, weather, and activity tracking
- **Visual Assets:** References to icons and images

### Supported Devices

- **Amazfit Bip Max:** Full support with optimized 432×514 resolution

## Installation

To install these watchfaces on your Amazfit device:

1. Connect your smartwatch to your computer
2. Use the official Amazfit app or Zepp app for watchface management
3. Import the desired watchface configuration from the `src/` directory
4. Sync with your device

## Customization

Each watchface JSON configuration can be modified to:
- Change colors and visual styling
- Adjust element positioning and size
- Enable/disable specific metrics
- Modify fonts and text sizes
- Customize health indicator thresholds

For detailed customization, refer to the Amazfit watchface development documentation.

## Features

### Health & Activity Metrics
- **PAI Score:** Personal Activity Intelligence tracking with visual progress
- **Stand Hours:** Daily standing activity monitoring
- **Humidity:** Current environmental humidity levels
- **UV Index:** Sun exposure and UV protection information

### Device Status Indicators
- Bluetooth connection status
- Alarm active indicator
- Do Not Disturb mode
- Screen lock status

### Weather Integration
- Current temperature display
- Weather condition visualization
- Automatic weather updates

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to:
- Submit new watchface designs
- Propose improvements to existing watchfaces
- Report issues or suggest features
- Create variants for other Amazfit devices

## Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/BlythMeister/Amazfit-Watchfaces).

## Acknowledgments

Built with attention to detail for Amazfit smartwatch users who want customizable, data-rich watchfaces.

---

**Last Updated:** August 20, 2026
