# KaiLab SIGNALFORGE

**An offline, browser-based research laboratory for image formats, procedural graphics, compression benchmarking, Unicode steganography and binary-file inspection.**


KaiLab SIGNALFORGE is a self-contained experimental workbench developed to investigate unusual file formats, digital rendering behaviour, hidden Unicode messages and compression artefacts.

The project was inspired by a collection of experiments involving JPEG, PNG, APNG, WebP, JPEG XL, OpenEXR, DNG, EPS, interactive PDFs and Unicode rendering stress tests.

**Its central principle:** a file's name, its actual encoding and the way software displays it are not necessarily the same.

## Features

### Image Format Laboratory

- Detect image formats using file signatures.
- Inspect actual dimensions, colour modes and encoding metadata.
- Investigate animated PNG frame timing.
- Compare files with misleading names or extensions.
- Examine histograms and pixel statistics.
- Import local images without uploading them.

### Procedural Signal Generator

Generate reproducible graphics for testing rendering and compression:

- Moiré interference patterns
- Frequency chirps
- Colour gradients
- Radial waves
- Diagonal colour bands
- Checkerboards
- Pseudorandom noise

Adjust resolution, spatial frequency, contrast and random seed. Export generated images as PNG, JPEG or WebP.

### Compression Benchmarking

Compare the file size and reconstruction accuracy of browser-generated PNG, JPEG and WebP images.

The benchmark calculates mean squared error and peak signal-to-noise ratio (PSNR), using an identical SDR canvas as the reference.

Results depend on the browser's encoders, and equivalent quality settings do not necessarily imply equivalent visual quality.

### Unicode Forensics

Analyse complex Unicode strings and detect:

- Combining diacritics and Zalgo text
- Zero-width characters
- Bidirectional text controls
- Variation-selector encoding
- Private-use characters
- Hidden UTF-8 messages
- Supported zero-width binary payloads

The built-in demonstrations include variation-selector steganography and a zero-width message encoding the phrase `meet at midnight`.

Users can export decoded messages, sanitised text and JSON forensic reports.

### Binary Inspector

Inspect file structures without executing embedded scripts.

| Format | Supported inspection |
|---|---|
| PNG / APNG | Headers, chunks, dimensions, frame timing |
| JPEG | SOF markers, dimensions, encoding type |
| WebP | RIFF structure, chunks and metadata |
| GIF / BMP | Basic file signatures and dimensions |
| OpenEXR | Channels, compression, precision and windows |
| TIFF / DNG | Header and selected IFD properties |
| JPEG XL | Signature and container identification |
| EPS | Bounding boxes and document metadata |
| PDF | Version and visible action-related markers |

Some formats support structural inspection only. Full OpenEXR decoding, RAW demosaicing, PDF emulation and complete JPEG XL decoding are not included.

### Research Archive

Includes 34 documented experimental image and graphics cases collected during development.

The archive stores static, reduced-size previews alongside recorded metadata. These previews are not substitutes for the original source files.

## Getting Started

**Requirements:** a modern browser with JavaScript, Canvas 2D and File API support.

1. Open `KaiLab_SignalForge.html` in Chrome, Edge or Firefox.
2. Select a research module from the sidebar.
3. Import an image, generate a procedural pattern or paste Unicode text.
4. Inspect the resulting measurements.
5. Export the results when needed.

The application is designed to work offline. No account, API key, backend service or external JavaScript library is required.

## Project Structure

The editable project includes:

- `index.html` — standalone compiled application
- `source.html` — HTML and CSS template
- `app.js` — JavaScript application and inspection logic
- `archive_manifest.json` — experimental dataset metadata
- `build.py` — application packaging script
- `PROJECT_ARCHITECTURE.md` — engineering architecture
- `tests/smoke_test.py` — browser integration tests
- `screenshots/` — desktop and mobile screenshots

## Building From Source

Run `python build.py` inside the source directory.

This rebuilds the standalone HTML and complete project ZIP from the template, JavaScript and archive manifest.

The prebuilt application does not require Python.

## Testing

Optional automated browser tests use Python Playwright and Chromium.

Install Playwright with `python -m pip install playwright`, install Chromium with `python -m playwright install chromium`, then run `python tests/smoke_test.py`.

The suite checks archive loading, Unicode decoding, procedural image generation, compression benchmarking and responsive navigation.

## Privacy and Security

- Local files remain in the browser's processing environment.
- The application does not upload files to a remote server.
- Imported PostScript or PDF JavaScript is not executed.
- Unicode sanitisation can remove meaningful characters and should not replace original source data.
- Static PDF inspection cannot guarantee that a document is safe.
- Malformed files may still expose vulnerabilities in underlying browser decoders.

## Research Roadmap

- [ ] Add WebAssembly OpenEXR and JPEG XL decoders.
- [ ] Develop a frame-accurate APNG analysis system.
- [ ] Integrate WebGPU-accelerated procedural rendering.
- [ ] Implement SSIM and additional image-quality metrics.
- [ ] Introduce automated image-format compatibility testing.
- [ ] Add batch processing and SHA-256 duplicate detection.
- [ ] Expand Unicode security and font-shaping experiments.
- [ ] Build cross-browser performance comparison tools.
- [ ] Introduce property-based fuzz testing of binary parsers.

## Author

**Kai Piper — kai9987kai**

Developed as an experimental research workbench combining digital graphics, browser engineering, file-format analysis and Unicode forensics.

**Version:** 1.0  
**Initial development:** October 2026  
**Platform:** Web browser  
**Architecture:** Offline, client-side JavaScript

## Licence

No open-source licence has yet been declared. A `LICENSE` file should be added before publishing specific reuse and redistribution permissions.
