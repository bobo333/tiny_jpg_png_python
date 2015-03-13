**March 4, 2015**

# Jpeg and Png Compressor

## Installation

TinyJPG limits free compressions to 500 images per month. For this reason, [acquire a new API Key](https://tinypng.com/developers) and replace `[API KEY HERE]` in `tinyjpg.py`. 

## Usage

1. Make sure there are no image files in the `originals` or `compressed` directories.
2. Copy image files to be compressed into `originals` directory.
3. Run `python tinyjpg.py`
4. Compressed images will be saved, with the same name as the original uncompressed file, to `compressed` directory.
5. Run `./calculated_saved` to run a tool for outputting the percent reduction in file size before and after compression.

*Note: This currently only works for `.jpg` and `.png` files, as the api from TinyJPG/TinyPNG only works for those file types at this time.*

