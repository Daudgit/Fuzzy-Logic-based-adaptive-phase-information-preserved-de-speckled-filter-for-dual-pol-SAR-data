# Copyright Name
**Fuzzy Logic based adaptive phase information preserved de-speckled filter for dual polarized SAR data**

## Patent Information
- Citation link: [SK Daud Hassan, Debanka Pal, Sriparna Banerjee, Sheli Sinha Chaudhuri, "Fuzzy Logic based adaptive phase information preserved de-speckled filter for dual polarized SAR data"](https://www.researchgate.net/publication/371607909_Fuzzy_Logic_based_adaptive_phase_information_preserved_de-speckled_filter_for_dual_polarized_SAR_data) (Registered)
- Diary number: 3869/2023-CO/SW
- Registration Number: SW-16607/2023

## Description
In the proposed method, a **fuzzy logic (FL) based adaptive weighted despeckling** approach is employed to handle uncertainties and process each pixel uniquely based on its properties. FL is chosen due to its capability to handle uncertainties effectively.

For the implementation of the FL-based despeckling strategy, a set of **125 novel fuzzy inference (FI) rules** has been designed. These rules serve as guidelines for the FL system to determine the appropriate weights for despeckling each pixel. The output of the FL system is the weight, which is the linguistic variable indicating the level of speckle noise to be removed.

To define the input linguistic variables, different combinations of scattering properties are considered. These scattering properties reflect the varied characteristics of land covers from which the electromagnetic waves are reflected back in SAR images.

By incorporating these input linguistic variables and utilizing the FL-based approach with the set of designed FI rules, the proposed method aims to adaptively assign weights to pixels based on their scattering properties. This adaptive weighting strategy takes into account the inter-pixel similarities in scattering properties, allowing for more effective speckle noise suppression while preserving important image features.

The use of FL in this method leverages its ability to handle uncertainties and perform unique processing for each pixel, enhancing the despeckling performance and potentially improving the interpretability and analysis of SAR images.

### The Novel 125 FI Rules designed in this work

- **VLFVD** - Very Low First Variable Difference
- **LFVD** - Low First Variable Difference
- **AFVD** - Average First Variable Difference
- **VHFVD** - Very High First Variable Difference
- **HFVD** - High First Variable Difference

- **VLSVD** - Very Low Second Variable Difference
- **LSVD** - Low Second Variable Difference
- **ASVD** - Average Second Variable Difference
- **VHSVD** - Very High Second Variable Difference
- **HSVD** - High Second Variable Difference

- **VLTVD** - Very Low Third Variable Difference
- **LTVD** - Low Third Variable Difference
- **ATVD** - Average Third Variable Difference
- **VHTVD** - Very High Third Variable Difference
- **HTVD** - High Third Variable Difference

- **VLW** - Very Low Weight
- **LW** - Low Weight
- **AW** - Average Weight
- **HW** - High Weight
- **VHW** - Very High Weight

| Rule | First linguistic variable | Second linguistic variable | Third linguistic variable | Output linguistic variable |
|------|--------------------------|---------------------------|--------------------------|----------------------------|
| 1    | VLFVD                    | VLSVD                     | VLTVD                    | VHW                        |
| 2    | VLFVD                    | VLSVD                     | LTVD                     | VHW                        |
| 3    | VLFVD                    | VLSVD                     | ATVD                     | VHW                        |
| 4    | VLFVD                    | VLSVD                     | HTVD                     | VHW                        |
| 5    | VLFVD                    | VLSVD                     | VHTVD                    | VHW                        |
| 6    | VLFVD                    | LSVD                      | VLTVD                    | VHW                        |
| 7    | VLFVD                    | LSVD                      | LTVD                     | VHW                        |
| 8    | VLFVD                    | LSVD                      | ATVD                     | VHW                        |
| 9    | VLFVD                    | LSVD                      | HTVD                     | HW                         |
| 10   | VLFVD                    | LSVD                      | VHTVD                    | HW                         |
| 11   | VLFVD                    | ASVD                      | VLTVD                    | VHW                        |
| 12   | VLFVD                    | ASVD                      | LTVD                     | HW                         |
| 13   | VLFVD                    | ASVD                      | ATVD                     | AW                         |
| 14   | VLFVD                    | ASVD                      | HTVD                     | AW                         |
| 15   | VLFVD                    | ASVD                      | VHTVD                    | LW                         |
| 16   | VLFVD                    | HSVD                      | VLTVD                    | VHW                        |
| 17   | VLFVD                    | HSVD                      | LTVD                     | AW                         |
| 18   | VLFVD                    | HSVD                      | ATVD                     | AW                         |
| 19   | VLFVD                    | HSVD                      | HTVD                     | LW                         |
| 20   | VLFVD                    | HSVD                      | VHTVD                    | LW                         |
| 21   | VLFVD                    | VHSVD                     | VLTVD                    | HW                         |
| 22   | VLFVD                    | VHSVD                     | LTVD                     | HW                         |
| 23   | VLFVD                    | VHSVD                     | ATVD                     | AW                         |
| 24   | VLFVD                    | VHSVD                     | HTVD                     | AW                         |
| 25   | VLFVD                    | VHSVD                     | VHTVD                    | AW                         |
| 26   | LFVD                     | VLSVD                     | VLTVD                    | VHW                        |
| 27   | LFVD                     | VLSVD                     | LTVD                     | VHW                        |
| 28   | LFVD                     | VLSVD                     | ATVD                     | VHW                        |
| 29   | LFVD                     | VLSVD                     | HTVD                     | VHW                        |
| 30   | LFVD                     | VLSVD                     | VHTVD                    | VHW                        |
| 31   | LFVD                     | LSVD                      | VLTVD                    | VHW                        |
| 32   | LFVD                     | LSVD                      | LTVD                     | VHW                        |
| 33   | LFVD                     | LSVD                      | ATVD                     | HW                         |
| 34   | LFVD                     | LSVD                      | HTVD                     | HW                         |
| 35   | LFVD                     | LSVD                      | VHTVD                    | AW                         |
| 36   | LFVD                     | ASVD                      | VLTVD                    | HW                         |
| 37   | LFVD                     | ASVD                      | LTVD                     | HW                         |
| 38   | LFVD                     | ASVD                      | ATVD                     | AW                         |
| 39   | LFVD                     | ASVD                      | HTVD                     | AW                         |
| 40   | LFVD                     | ASVD                      | VHTVD                    | AW                         |
| 41   | LFVD                     | HSVD                      | VLTVD                    | HW                         |
| 42   | LFVD                     | HSVD                      | LTVD                     | HW                         |
| 43   | LFVD                     | HSVD                      | ATVD                     | AW                         |
| 44   | LFVD                     | HSVD                      | HTVD                     | LW                         |
| 45   | LFVD                     | HSVD                      | VHTVD                    | LW                         |
| 46   | LFVD                     | VHSVD                     | VLTVD                    | HW                         |
| 47   | LFVD                     | VHSVD                     | LTVD                     | HW                         |
| 48   | LFVD                     | VHSVD                     | ATVD                     | AW                         |
| 49   | LFVD                     | VHSVD                     | HTVD                     | LW                         |
| 50   | LFVD                     | VHSVD                     | VHTVD                    | LW                         |
| 51   | AFVD                     | VLSVD                     | VLTVD                    | VHW                        |
| 52   | AFVD                     | VLSVD                     | LTVD                     | HW                         |
| 53   | AFVD                     | VLSVD                     | ATVD                     | HW                         |
| 54   | AFVD                     | VLSVD                     | HTVD                     | AW                         |
| 55   | AFVD                     | VLSVD                     | VHTVD                    | LW                         |
| 56   | AFVD                     | LSVD                      | VLTVD                    | HW                         |
| 57   | AFVD                     | LSVD                      | LTVD                     | HW                         |
| 58   | AFVD                     | LSVD                      | ATVD                     | HW                         |
| 59   | AFVD                     | LSVD                      | HTVD                     | AW                         |
| 60   | AFVD                     | LSVD                      | VHTVD                    | LW                         |
| 61   | AFVD                     | ASVD                      | VLTVD                    | HW                         |
| 62   | AFVD                     | ASVD                      | LTVD                     | HW                         |
| 63   | AFVD                     | ASVD                      | ATVD                     | AW                         |
| 64   | AFVD                     | ASVD                      | HTVD                     | AW                         |
| 65   | AFVD                     | ASVD                      | VHTVD                    | LW                         |
| 66   | AFVD                     | HSVD                      | VLTVD                    | AW                         |
| 67   | AFVD                     | HSVD                      | LTVD                     | AW                         |
| 68   | AFVD                     | HSVD                      | ATVD                     | AW                         |
| 69   | AFVD                     | HSVD                      | HTVD                     | LW                         |
| 70   | AFVD                     | HSVD                      | VHTVD                    | LW                         |
| 71   | AFVD                     | VHSVD                     | VLTVD                    | AW                         |
| 72   | AFVD                     | VHSVD                     | LTVD                     | AW                         |
| 73   | AFVD                     | VHSVD                     | ATVD                     | LW                         |
| 74   | AFVD                     | VHSVD                     | HTVD                     | LW                         |
| 75   | AFVD                     | VHSVD                     | VHTVD                    | LW                         |
| 76   | HFVD                     | VLSVD                     | VLTVD                    | HW                         |
| 77   | HFVD                     | VLSVD                     | LTVD                     | HW                         |
| 78   | HFVD                     | VLSVD                     | ATVD                     | AW                         |
| 79   | HFVD                     | VLSVD                     | HTVD                     | LW                         |
| 80   | HFVD                     | VLSVD                     | VHTVD                    | LW                         |
| 81   | HFVD                     | LSVD                      | VLTVD                    | HW                         |
| 82   | HFVD                     | LSVD                      | LTVD                     | HW                         |
| 83   | HFVD                     | LSVD                      | ATVD                     | AW                         |
| 84   | HFVD                     | LSVD                      | HTVD                     | LW                         |
| 85   | HFVD                     | LSVD                      | VHTVD                    | LW                         |
| 86   | HFVD                     | ASVD                      | VLTVD                    | AW                         |
| 87   | HFVD                     | ASVD                      | LTVD                     | AW                         |
| 88   | HFVD                     | ASVD                      | ATVD                     | LW                         |
| 89   | HFVD                     | ASVD                      | HTVD                     | LW                         |
| 90   | HFVD                     | ASVD                      | VHTVD                    | LW                         |
| 91   | HFVD                     | HSVD                      | VLTVD                    | AW                         |
| 92   | HFVD                     | HSVD                      | LTVD                     | LW                         |
| 93   | HFVD                     | HSVD                      | ATVD                     | LW                         |
| 94   | HFVD                     | HSVD                      | HTVD                     | LW                         |
| 95   | HFVD                     | HSVD                      | VHTVD                    | VLW                        |
| 96   | HFVD                     | VHSVD                     | VLTVD                    | AW                         |
| 97   | HFVD                     | VHSVD                     | LTVD                     | LW                         |
| 98   | HFVD                     | VHSVD                     | ATVD                     | LW                         |
| 99   | HFVD                     | VHSVD                     | HTVD                     | VLW                        |
| 100  | HFVD                     | VHSVD                     | VHTVD                    | VLW                        |
| 101  | VHFVD                    | VLSVD                     | VLTVD                    | HW                         |
| 102  | VHFVD                    | VLSVD                     | LTVD                     | HW                         |
| 103  | VHFVD                    | VLSVD                     | ATVD                     | AW                         |
| 104  | VHFVD                    | VLSVD                     | HTVD                     | AW                         |
| 105  | VHFVD                    | VLSVD                     | VHTVD                    | AW                         |
| 106  | VHFVD                    | LSVD                      | VLTVD                    | HW                         |
| 107  | VHFVD                    | LSVD                      | LTVD                     | HW                         |
| 108  | VHFVD                    | LSVD                      | ATVD                     | AW                         |
| 109  | VHFVD                    | LSVD                      | HTVD                     | LW                         |
| 110  | VHFVD                    | LSVD                      | VHTVD                    | LW                         |
| 111  | VHFVD                    | ASVD                      | VLTVD                    | AW                         |
| 112  | VHFVD                    | ASVD                      | LTVD                     | AW                         |
| 113  | VHFVD                    | ASVD                      | ATVD                     | AW                         |
| 114  | VHFVD                    | ASVD                      | HTVD                     | LW                         |
| 115  | VHFVD                    | ASVD                      | VHTVD                    | LW                         |
| 116  | VHFVD                    | HSVD                      | VLTVD                    | LW                         |
| 117  | VHFVD                    | HSVD                      | LTVD                     | LW                         |
| 118  | VHFVD                    | HSVD                      | ATVD                     | LW                         |
| 119  | VHFVD                    | HSVD                      | HTVD                     | VLW                        |
| 120  | VHFVD                    | HSVD                      | VHTVD                    | VLW                        |
| 121  | VHFVD                    | VHSVD                     | VLTVD                    | LW                         |
| 122  | VHFVD                    | VHSVD                     | LTVD                     | LW                         |
| 123  | VHFVD                    | VHSVD                     | ATVD                     | LW                         |
| 124  | VHFVD                    | VHSVD                     | HTVD                     | VLW                        |
| 125  | VHFVD                    | VHSVD                     | VHTVD                    | VLW                        |

## Implementation
Details of the Images
- __You Can Find the Detailed Code of this copyright in final.py__
- RGB1_original.jpg : It is the original Image SAR image
- RGB1_nosiy_0.5.jpg : it is the original image containing with noise
- RGB1_nosiy_0.5_gaussf.jpg : It is the resultant image after applying the filter to the noisy image
- Results Generated After the Execution of the code - membershipVSmship_ampl.png , membershipVSmship_lambda.png, membershipVSmship_phase.png, membershipVSwt.png .
