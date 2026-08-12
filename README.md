<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Python][python-shield]](https://www.python.org/downloads/release/python-3119/)
[![Platform][platform-shield]](#)
[![License][license-shield]][license-url]
[![Version][version-shield]](#)

<br />
<div align="center">
  <h1 align="center">MBP's Image Padder</h1>
  <p align="center">
    Batch-pad photos to any target aspect ratio with white borders — a lightweight, single-file tkinter tool.
    <br />
    <a href="#getting-started"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Usage</a>
    ·
    <a href="https://github.com/mbpitaly/image-padder/issues/new?labels=bug&template=bug_report.md">Report Bug</a>
    ·
    <a href="https://github.com/mbpitaly/image-padder/issues/new?labels=enhancement&template=feature_request.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#building-from-source">Building From Source</a></li>
    <li><a href="#project-layout">Project Layout</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

MBP's Image Padder is a single-file tkinter GUI that pads a batch of photos to a target aspect ratio with clean white borders — ideal for print, social platforms, and templates that demand a specific frame.

It was built by Matteo Barni (2026) to make batch aspect-ratio padding fast and autonomous: pick your photos, choose a ratio, start, done.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FEATURES -->
## Features

- **Batch processing** — pad hundreds of photos in one pass
- **7 aspect ratios** — `1:1`, `3:2`, `4:3`, `5:4`, `1.91:1`, `2.4:1`, and `16:9`
- **Vertical orientation toggle** — invert any ratio for portrait output
- **5% border margin** — the photo never touches the canvas edge
- **Auto-downscale above ~6 MP** — huge photos are resized (LANCZOS) to keep output size sane
- **EXIF preserved** — original metadata is written back to every padded file
- **Smart output naming** — saves each result as `<name>_padded.jpg` to the folder you choose (default `~/Desktop/Padded`)
- **Small progress window** — live counter + progress bar, then auto-closes

### Built With

- [Python 3.11](https://www.python.org/) + [tkinter/ttk](https://docs.python.org/3/library/tkinter.html)
- [Pillow](https://pypi.org/project/pillow/) — image padding, resize and EXIF handling
- [PyInstaller](https://pyinstaller.org/) — standalone exe packaging

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- **Windows 10/11** (tkinter comes with the official Python installer; the packaged exe needs nothing)

### Installation

**Option A — installer (Windows)**

Download `MBPs_Image_Padder_Setup.exe` from the [Releases](https://github.com/mbpitaly/image-padder/releases) page and run it. Everything is bundled — no extra installs, ever.

**Option B — from source**

```sh
# 1. Clone
git clone https://github.com/mbpitaly/image-padder.git
cd image-padder

# 2. Install the only runtime dependency
python -m pip install pillow

# 3. Run
python padder.pyw
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage

1. Launch `MBPs_Image_Padder.exe`.
2. Select one or more photos (JPG, PNG or WEBP) in the file picker.
3. In the settings popup, choose an **Aspect Ratio** and optionally tick **Vertical** to invert it.
4. Set the output folder (default `~/Desktop/Padded`).
5. Hit **Start Padding** — a small progress window tracks the batch and auto-closes when done.

Every finished file is written as `<name>_padded.jpg` into the chosen folder.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- BUILDING -->
## Building From Source

```
# Python 3.11
python -m pip install pyinstaller pillow
python -m PyInstaller --onefile --windowed \
  --icon icon.ico \
  --name MBPs_Image_Padder \
  padder.pyw
```

Notes:
- `--onefile --windowed` produces a single, double-clickable exe with no console window.
- The icon must always be passed via `--icon`, or PyInstaller silently embeds its generic icon.

A CI workflow (`.github/workflows/build.yml`) builds the exe automatically on version tags.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LAYOUT -->
## Project Layout

```
image-padder/
├── MBPs_Image_Padder.exe    # prebuilt Windows binary (PyInstaller onefile)
├── padder.pyw               # full source (single file)
├── icon.ico                 # app icon
├── .github/
│   ├── ISSUE_TEMPLATE/      # bug report + feature request templates
│   └── workflows/build.yml  # Windows exe build on tag
├── CHANGELOG.md
├── SECURITY.md
├── LICENSE                  # MIT
├── requirements.txt
└── README.md
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please use the [issue templates](https://github.com/mbpitaly/image-padder/issues/new/choose) for bugs and feature requests, and check [CHANGELOG.md](CHANGELOG.md) before opening PRs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [Pillow](https://python-pillow.org/) — image processing
- [Best-README-Template](https://github.com/othneildrew/Best-README-Template) — README structure
- [Img Shields](https://shields.io/) — badges

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS -->
[python-shield]: https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white
[platform-shield]: https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white
[license-shield]: https://img.shields.io/badge/License-MIT-green?style=for-the-badge
[license-url]: LICENSE
[version-shield]: https://img.shields.io/badge/Release-v1.0.0-purple?style=for-the-badge
