# COM_CONT Format Specification

| Offset | Size | Type | Description |
|--------|------|------|-------------|
| 0x00 | 8 | ASCII | Signature: "COM_CONT" |
| 0x08 | 4 | uint32 (LE) | Version |
| 0x0C | 4 | uint32 (LE) | Size |
| 0x10 | 4 | uint32 (LE) | Reference Count |

## Reference Entry Format (9 bytes each)
| Offset | Size | Type | Description |
|--------|------|------|-------------|
| 0x00 | 4 | uint32 (LE) | Asset Type ID |
| 0x04 | 4 | uint32 (LE) | Asset ID |
| 0x08 | 1 | byte | Unknown data |

# DC_INFO Format Specification

| Offset | Size | Type | Description |
|--------|------|------|-------------|
| 0x00 | 8 | ASCII | Signature: "DC_INFO " (note the space) |
| 0x08 | 4 | uint32 (LE) | Version |
| 0x0C | 4 | uint32 (LE) | Size |
| 0x10 | 4 | uint32 (LE) | Unknown value |
| 0x14 | 4 | uint32 (LE) | Reference Count |

## Reference Entry Format (8 bytes each)
| Offset | Size | Type | Description |
|--------|------|------|-------------|
| 0x00 | 4 | uint32 (LE) | Asset Type ID |
| 0x04 | 4 | uint32 (LE) | Asset ID |
