# KaiLab SIGNALFORGE — Engineering Architecture

## Rationale

The project combines the *actual needs* demonstrated by a long sequence of unusual assets: codec metadata frequently mismatched filenames; APNG delay semantics varied by decoder; OpenEXR preserved float channels; Unicode included variation selectors, Zalgo and bidi; PDF and EPS could carry executable instructions.

## Modules

1. `File ArrayBuffer` → signature classifier → bounded, format-specific metadata scanners (PNG, JPEG, WebP, GIF, BMP, TIFF/DNG, EXR, JXL, PDF, EPS). This is not a general-purpose full decoder or malware scanner.
2. `Canvas ImageData` → deterministic pattern generator → three browser-native codecs → match-size MSE/PSNR. The benchmark is for SDR canvas resamples, not native HDR data.
3. `Unicode scalar iterator` → combining/bidi/zero-width class counts → supplementary/standard variation selector decoding → UTF-8 text → zero-width INV1 binary decoder → export.
4. `Archive embedded data` → 34 separate labelled previews → original file metadata → archive exploration. Archive metadata and generated preview measurements are explicitly separate.
5. `Client-side session state` → JSON/CSV export; no remote persistence.

## Supported capabilities versus deliberate omissions

| Format | Detect | Metadata | Native preview | Limit |
|---|---|---|---|---|
| PNG/APNG | Yes | IHDR, chunks, frame delays | Yes; static poster for APNG upload | No full frame composition testing |
| JPEG | Yes | SOF, progressive/baseline, components/ICC | Yes | Does not validate the entropy-coded stream |
| WebP | Yes | Chunks, extended flags, dimensions | Yes | Animation timing not fully decoded |
| GIF/BMP | Yes | Dimensions, basic fields | Yes | No exhaustive frame index |
| OpenEXR | Yes | Channels, float precision, windows/compression | No, archive thumbnail | Full HDR decoder requires WASM or companion service |
| TIFF/DNG | Yes | Basic IFD/header info | No, archive thumbnail | First IFD can be only an embedded thumbnail; no demosaicing |
| JPEG XL | Yes | Codestream/container signature | Depends on browser | No bundled decoder |
| PDF | Yes | Visible uncompressed action markers | No | Partial scan, not a security verdict |
| EPS | Yes | DSC header/bounding box | No | Does not execute PostScript |

## Future research tracks

- Optional WASM OpenEXR/JPEG XL decoders *with deterministic channel layout and colour management*; report actual linear/HDR values and specify transfer functions.
- Proper per-frame APNG decoder, compositing/disposal trace, timing clamp comparisons, and a user-controlled **non-strobing** step viewer.
- Per-browser reproducibility export with encoder implementation, GPU/CPU information (consent-sensitive), throughput and memory usage.
- Multi-file batch evaluation with SHA-256 deduplication and numerical SSIM/LPIPS (additional libraries optional).
- Property-based fuzzing against read-only parsers and well-defined byte/time limits.
- Direct WebGPU shader-based signal generation, then check CPU ↔ GPU pixel discrepancy with colour-space correction.
- Optional WebAssembly Unicode and font-shaping tests to detect glyph overflow and text segmentation issues.

## Data handling

Import reads local files into browser memory. No network calls are present in app source. Data is not uploaded or persisted across reloads. Export only through explicit user action. Imported PDF/PS scripts are not executed. The original source files are not embedded in the app; archive samples are downsized previews only.
