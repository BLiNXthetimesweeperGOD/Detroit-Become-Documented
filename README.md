# Detroit-Become-Documented
This repository is for documentation of the various file formats used in the PC version of Detroit: Become Human

You may use this information as you wish.

### File format list (with extensions)
```
idx - an index for the data contained within the dat/dXX files. Everything involving those files is generally handled here.
dat - stores data referenced by the idx file, referenced as package ID 0
dXX - stores data referenced by the idx file, referenced as package IDs 1-29
dds - textures, used in various points across the game (but not the only texture format)
bnk - embedded within packages stored inside of the dat/dXX packages, contains wem files
wem - wwise audio files (the header looks like WAV, but these aren't WAV files!)
mid - MIDI files (used for the piano in "The Painter". Only 4 exist and they're stored in QZIP containers.)
bk2 - Bink 2 Video files (some are encrypted and can't be ripped yet)
```

### Extensionless formats with file signatures
```
segs - contains segmented, ZLIB-compressed data in 64 kilobyte chunks, usually models/gameplay assets
QZIP - used for many different things (voice clips, segs containers, data containers...), is uncompressed in most cases.
```
