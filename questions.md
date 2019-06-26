# Questions

## What's `stdint.h`?

allow programmers to write more portable code by providing a set of typedefs that specify exact-width integer types, together with the defined minimum and maximum allowable values for each type 
like uint8_t, uint32_t, int32_t

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

to determine the rxsct size of my new data type

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

byte = 1 byte u  |   dword = 4 byte u  |  long = 4 byte   |  word = 2 byte u

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

BM in ascii

## What's the difference between `bfSize` and `biSize`?

bfsize The size, in bytes, of the bitmap file(whole bmp file)
bisize The number of bytes required by the structure.

## What does it mean if `biHeight` is negative?

If biHeight is negative, indicating a top-down DIB, biCompression must be either BI_RGB or BI_BITFIELDS. Top-down DIBs cannot be compressed.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in `copy.c`?

TODO

## Why is the third argument to `fread` always `1` in our code?

TODO

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

TODO

## What does `fseek` do?

TODO

## What is `SEEK_CUR`?

TODO
