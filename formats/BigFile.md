# BigFile.idx/dat/dXX
This is the main container format that you'll see when you first install the game. It has a relatively simple structure:

## Header Format

| Offset | Size | Type | Description |
|--------|------|------|-------------|
| 0x00 | 0x65 | Binary | Header data |
| 0x65 | 4 | uint32 (BE) | Number of entries |

## Entry Format
Each entry is 28 bytes and follows this structure:

| Offset | Size | Type | Description |
|--------|------|------|-------------|
| 0x00 | 4 | uint32 (BE) | Asset Type ID |
| 0x04 | 4 | uint32 (BE) | Asset Count (unused) |
| 0x08 | 4 | uint32 (BE) | Asset ID |
| 0x0C | 4 | uint32 (BE) | Offset in data file |
| 0x10 | 4 | uint32 (BE) | Size of the asset |
| 0x14 | 4 | uint32 (BE) | Alternative Size (purpose unclear?) |
| 0x18 | 4 | uint32 (BE) | Package ID (determines which data file to use) |
