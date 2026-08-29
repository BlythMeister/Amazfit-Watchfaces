# Amazfit Watchfaces

A collection of custom watchfaces for Amazfit devices. Each design is stored as a JSON configuration alongside its preview images and supporting assets.

## Watchfaces

| Design | Watch | Current Version | Description | Previews | Installation |
| --- | --- | --- | --- | --- | --- |
| [Overview - Icons](src/Bip%20Max%20-%20Overview%20-%20Icons) | Bip Max | V2 | The main overview design, combining time, weather, humidity, UV index, PAI, stand hours, activity data and device-status indicators. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20Icons/Preview.gif" width="180" alt="Overview Icons animated preview"> | Official - Search `1124003` on Zepp watch face store<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45504) |
| [Overview – TextOnly](src/Bip%20Max%20-%20Overview%20-%20TextOnly) | Bip Max | V2 | A text-focused variant of the overview layout, using a simpler presentation of the available watchface data. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20TextOnly/Preview.gif" width="180" alt="Overview TextOnly animated preview"> | Official - Search `1124185` on Zepp watch face store<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45505) |
| [Overview – Colourful](src/Bip%20Max%20-%20Overview%20-%20Colourful) | Bip Max | V2 | A colourful variant of the overview design with colour accents applied to the displayed values. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20Colourful/Preview.gif" width="180" alt="Overview Colourful animated preview"> | Official - Search `1124184` on Zepp watch face store<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45506) |
| [Overview – Bubbles](src/Bip%20Max%20-%20Overview%20-%20Bubbles) | Bip Max | V2 | A bubble-style variant of the overview design, with its own JSON configuration and supporting asset set. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20Bubbles/Preview.gif" width="180" alt="Overview Bubbles animated preview"> | Official - Search `1124205` on Zepp watch face store<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45508) |
| [Overview – SteamPunk](src/Bip%20Max%20-%20Overview%20-%20SteamPunk) | Bip Max | V1 | A steampunk variant of the overview design, with its own JSON configuration and supporting asset set. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20SteamPunk/Preview.gif" width="180" alt="Overview SteamPunk animated preview"> | Official - Search `1125417` on Zepp watch face store (Comming Soon)<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45549) |
| [Overview – Circuit](src/Bip%20Max%20-%20Overview%20-%20Circuit) | Bip Max | V1 | A circuit variant of the overview design, with its own JSON configuration and supporting asset set. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20Circuit/Preview.gif" width="180" alt="Overview Circuit animated preview"> | Official - Search `1125414` on Zepp watch face store (Comming Soon)<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45546) |
| [Overview – Silver](src/Bip%20Max%20-%20Overview%20-%20Silver) | Bip Max | V1 | A silver variant of the overview design, with its own JSON configuration and supporting asset set. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20Silver/Preview.gif" width="180" alt="Overview Silver animated preview"> | Official - Search `1125415` on Zepp watch face store (Comming Soon)<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45548) |
| [Overview – Gold](src/Bip%20Max%20-%20Overview%20-%20Gold) | Bip Max | V1 | A gold variant of the overview design, with its own JSON configuration and supporting asset set. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Bip%20Max%20-%20Overview%20-%20Gold/Preview.gif" width="180" alt="Overview Gold animated preview"> | Official - Search `1125416` on Zepp watch face store (Comming Soon)<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/bip/view/45547) |
| [Overview – TextOnly](src/Active%20Max%20-%20Overview%20-%20TextOnly) | Active Max | V1 | A text-focused variant of the overview layout, using a simpler presentation of the available watchface data. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Active%20Max%20-%20Overview%20-%20TextOnly/Preview.gif" width="180" alt="Overview TextOnly animated preview"> | Official - Search `1125431` on Zepp watch face store (Comming Soon)<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/active/view/2747) |
| [Overview – Colourful](src/Active%20Max%20-%20Overview%20-%20Colourful) | Active Max | V1 | A colourful variant of the overview design with colour accents applied to the displayed values. | <img src="https://raw.githubusercontent.com/BlythMeister/Amazfit-Watchfaces/master/src/Active%20Max%20-%20Overview%20-%20Colourful/Preview.gif" width="180" alt="Overview Colourful animated preview"> | Official - Search `1125429` on Zepp watch face store (Comming Soon)<br/><br/>Sideload - [amazfitwatchfaces.com](https://amazfitwatchfaces.com/active/view/2748) |


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

Each `assets/` directory contains the resources used by its watchface, including backgrounds, fonts and icons.

## Editing and Installation

The watchface JSON files can be edited with the [Watch face editor for Amazfit watches on ZeppOS](https://github.com/SashaCX75/Watch-face-editor-for-Amazfit-watch-on-ZeppOS).

## Contributing

Contributions are welcome. You can submit new designs, improve existing variants, add support for other Amazfit devices, or report issues and suggestions through GitHub Issues.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
