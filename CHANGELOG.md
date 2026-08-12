# Changelog

All notable changes to MBP's Image Padder are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-12

### Added
- Initial release.
- Batch padding of JPG, PNG and WEBP photos to a target aspect ratio with white borders.
- 7 aspect ratios: `1:1`, `3:2`, `4:3`, `5:4`, `1.91:1`, `2.4:1`, `16:9`.
- Vertical orientation toggle (inverts any ratio for portrait output).
- 5% border margin so the photo never touches the canvas edge.
- Auto-downscale of photos above ~6 MP (LANCZOS) to keep output size sane.
- EXIF metadata preserved on every padded file.
- Output saved as `<name>_padded.jpg` to the chosen folder (default `~/Desktop/Padded`).
- Small progress window with live counter and progress bar.
