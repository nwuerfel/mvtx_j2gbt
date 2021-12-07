What's a markdown?

MVTX Encoder for AI Engine development

This is some script to take the JSON output of the simulations for the sPHENIX
AI engine and encode the MVTX hits into GBT packets expected at the input to
FELIX

The current plan (Dec 2021) is to fan out GBT data packets from the input of
FELIX to the AI Engine

The ALPIDE detector defines the encoding scheme for hits -> GBT packets in local
RUs, but the current simulation outputs a JSON file containing MVTX and INTT
hits, without ALPIDE encoding/ GBT packet info.

ALPIDE contains a 512 X 1024 pixels with a periphery circuit which includes the
readout and control functions. The periphery is referenced at the bottom with
pixel columns numbered 0 to 1023 from left to right. The pixel rows are numbered
from 0 to 511 from the top of the detector.

9 ALPIDE detectors are mounted on "staves" which each supply a readout unit(RU). 
Each RU has 3 GBT outputs and 8 RUs feed each FELIX board - 24 connections?










ITS DATA WORD FORMAT 80 bits:
[79 : 72]           | [71 : 0]
 RU\_GBT\_WORD\_ID  |  Cable data for one cable or other data 

GBT Data Word 80 bits with RU\_GBT\_WORD\_ID and 9 ALPIDE data bytes:
 [79 : 72]  | [71 : 64]  | [63 : 56]  | [55 : 48]  | [47 : 40]  | [39 : 32]  | [31 : 24] | [23 : 16]  | [15 : 8]  | [7 : 0]
 ID         | DW[8]      | DW[7]      | DW[6]      | DW[5]      | DW[4]      | DW[3]     | DW[2]      | DW[1]     | DW[0]

 here the DW[n] data words are filled LSB to MSB -> DW[0] is first to arrive...
