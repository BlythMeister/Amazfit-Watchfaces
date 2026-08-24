# Amazfit Watchfaces

A collection of custom watchfaces for the **Amazfit Bip Max**. Each design is stored as a JSON configuration alongside its preview images and supporting assets.

## Watchfaces

| Watch | Design | Description | Previews | Installation |
| --- | --- | --- | --- | --- |
| Bip Max | [Overview](src/Bip%20Max%20-%20Overview) | The main overview design, combining time, weather, humidity, UV index, PAI, stand hours, activity data and device-status indicators. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview/Preview.gif" width="180" alt="Overview animated preview"> | Official - Search `1124003` on Zepp watch face store<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45504) |
| Bip Max | [Overview – TextOnly](src/Bip%20Max%20-%20Overview%20-%20TextOnly) | A text-focused variant of the overview layout, using a simpler presentation of the available watchface data. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20TextOnly/Preview.gif" width="180" alt="Overview TextOnly animated preview"> | Official - Search `1124185` on Zepp watch face store<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45505) |
| Bip Max | [Overview – Colourful](src/Bip%20Max%20-%20Overview%20-%20Colourful) | A colourful variant of the overview design with colour accents applied to the displayed values. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20Colourful/Preview.gif" width="180" alt="Overview Colourful animated preview"> | Official - Search `1124184` on Zepp watch face store<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45506) |
| Bip Max | [Overview – Bubbles](src/Bip%20Max%20-%20Overview%20-%20Bubbles) | A bubble-style variant of the overview design, with its own JSON configuration and supporting asset set. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20Bubbles/Preview.gif" width="180" alt="Overview Bubbles animated preview"> | Official - Search `1124205` on Zepp watch face store<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45508) |
| Bip Max | [Overview – SteamPunk](src/Bip%20Max%20-%20Overview%20-%20SteamPunk) | A steampunk variant of the overview design, with its own JSON configuration and supporting asset set. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20SteamPunk/Preview.gif" width="180" alt="Overview SteamPunk animated preview"> | TBC |
| Bip Max | [Overview – Circuit](src/Bip%20Max%20-%20Overview%20-%20Circuit) | A circuit variant of the overview design, with its own JSON configuration and supporting asset set. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20Circuit/Preview.gif" width="180" alt="Overview Circuit animated preview"> | TBC |

The previews above are intentionally displayed at a reduced width. Open an image or design directory to view the full-size files and additional assets.

## Repository Structure

```text
Amazfit-Watchfaces/
├── .github/
│   └── FUNDING.yml
├── .gitignore
├── LICENSE
├── README.md
└── src/
    └── {DEVICE} - {Name}/
        ├── {DEVICE} - {Name}.json
        ├── Preview.png
        ├── Preview.gif
        └── assets/
```

Each `assets/` directory contains the resources used by its watchface, including backgrounds, fonts and icons. The configurations target the **432 × 514** Bip Max display and use the Rajdhani SemiBold font included in the repository.

## Editing and Installation

The watchface JSON files can be edited with the [Watch face editor for Amazfit watches on ZeppOS](https://github.com/SashaCX75/Watch-face-editor-for-Amazfit-watch-on-ZeppOS).

## Contributing

Contributions are welcome. You can submit new designs, improve existing variants, add support for other Amazfit devices, or report issues and suggestions through GitHub Issues.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
