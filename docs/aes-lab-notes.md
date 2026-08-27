# AES Lab Notes

The original material covers AES-128 concepts including key expansion, round keys, the inverse S-box, SubBytes, MixColumns, and the final AES round. This repository preserves those concepts as documentation because the submitted material did not provide a complete standalone AES implementation suitable for reuse.

## Key expansion
For AES-128, key expansion produces 176 bytes in total: 11 round keys × 16 bytes. The original 16-byte key is expanded into the round-key sequence used throughout encryption.

## Inverse S-box
The AES S-box is a one-to-one mapping, so every substituted byte has a unique inverse. For example, if the S-box maps `0x53` to `0xED`, then `InvSubBytes(0xED)` returns `0x53`.

## SubBytes and diffusion
SubBytes operates independently on each byte. Changing one input byte therefore changes only that byte immediately after SubBytes. Diffusion is introduced by later transformations such as ShiftRows and MixColumns.

## Final round
The final AES encryption round omits MixColumns. This is part of the AES design rather than a missing security step; the final round still performs ShiftRows, SubBytes, and AddRoundKey.

> **Educational note:** These notes document lab concepts; they are not a claim that a hand-written AES implementation is suitable for production cryptography.
