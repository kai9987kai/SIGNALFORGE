# KaiLab / SIGNALFORGE — 1.0

A **self-contained, privacy-preserving browser laboratory** inspired by the formats, encoding puzzles, and unusual files analysed across the conversation.

## Quick start

1. Open `index.html` in Chrome, Edge, or Firefox. No server, installation, sign-in, or internet connection required.
2. **Mission Control:** explore the test corpus and jump between the research modules.
3. **Format Laboratory:** browse the 34 embedded source case previews or import local files. Byte signatures are read directly; imported files are not uploaded.
4. **Pixel Stress Forge:** generate deterministic static textures, export PNG/JPEG/WebP and perform codec comparisons.
5. **Unicode Forensics:** paste text or import a text document, select **Load sample** to verify variation-selector and zero-width decoding, export forensic results and clean text.
6. **Container Inspector:** drop binary files including EXR, EPS, TIFF/DNG, PDF, JXL, PNG/APNG, WebP or JPEG to see structural metadata without running code.
7. **Archive:** inspect all curated images and metadata, based on previous experiments.

## Ground-truth policy

- Archive metadata refers to the original source files analysed earlier. Images embedded here are **resized, static thumbnails only**.
- When comparing the archive thumbnails in the browser, results are measurements of those thumbnails, **not** the originally uploaded source files. Import the original file to benchmark it.
- JPEG and WebP `quality:0.8` are API encoder quality settings, **not perceptually equivalent rates**. Both compare against an identical 8-bit SDR canvas at a matched size.
- No HDR EXR/RAW converter or JPEG XL decoder is bundled. Native browser support for them is not claimed. Structural metadata is still inspected.
- PNG/APNG sample previews are static by design. High-rate strobe samples should **not autoplay**.
- PDF scanning is a partial, static byte inspection, not a full PDF security audit; compressed streams and obfuscation may hide actions. EPS/PostScript code is never run.
- Sanitised Unicode text is **lossy**: removing combining marks may modify meaningful accents. Always preserve the source file separately.

## Engineering notes

Technology: single file HTML, vanilla CSS, browser JavaScript, Canvas 2D, FileReader/File API, TextEncoder/TextDecoder and native image encoders. Zero external dependencies and zero network requests.

Original conversation included: JPEG/PNG/APNG/WebP/JPEG XL/EXR/DNG/EPS samples, CV design changes, Unicode Zalgo / bidi / variation-selector steganography, and an experimental Linux-running PDF. These are represented as functional tests and research archive notes. The app does **not** bundle personal CV details or the original 103 MiB EXR.

## Acceptance tests

- Load page offline and inspect all 34 embedded archive cases.
- Press Unicode > Load sample; confirm one variation-selector text payload and one `INV1` zero-width message: `meet at midnight`.
- Generate a Moire image and download PNG; reimport PNG and confirm its exact encoded dimensions.
- Open JPEGs with misleading filenames and verify SOF0 / SOF2 and actual width/height.
- Inspect PNG/APNG chunks, frames and timings; do not autoplay high-rate strobing examples.
- Open a PDF and confirm whether JavaScript/action markers were visible in uncompressed inspected segments, then validate with a dedicated PDF security tool if needed.
- Compare an imported static image as matched-size PNG, JPEG and WebP.
- Export entire session to JSON.

## Safety

Run untrusted files in a current browser. The app never evaluates imported JavaScript/PostScript or sends files to any server. It cannot guarantee that a malformed decoder input will not trigger a browser vulnerability; update the browser and isolate untrusted files when necessary.

## Project inspiration

Kai Piper / `kai9987kai`, original interactive image-format research conversation, October 2026.
