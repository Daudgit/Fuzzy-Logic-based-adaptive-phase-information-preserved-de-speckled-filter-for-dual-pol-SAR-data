# Copyright Name
**Fuzzy Logic based adaptive phase information preserved de-speckled filter for dual polarized SAR data**

## Patent Information
- Citation link: [SK Daud Hassan, Debanka Pal , Sriparna Banerjee, Sheli Sinha Chaudhuri, "Fuzzy Logic based adaptive phase information preserved de-speckled filter for dual polarized SAR data"](https://www.researchgate.net/publication/371607909_Fuzzy_Logic_based_adaptive_phase_information_preserved_de-speckled_filter_for_dual_polarized_SAR_data) (Registered)
- Diary number: 3869/2023-CO/SW
- Registration Number: SW-16607/2023

## Description
In the proposed method, a fuzzy logic (FL) based adaptive weighted despeckling approach is employed to handle uncertainties and process each pixel uniquely based on its properties. FL is chosen due to its capability to handle uncertainties effectively.

For the implementation of the FL-based despeckling strategy, a set of 125 novel fuzzy inference (FI) rules has been designed. These rules serve as guidelines for the FL system to determine the appropriate weights for despeckling each pixel. The output of the FL system is the weight, which is the linguistic variable indicating the level of speckle noise to be removed.

To define the input linguistic variables, different combinations of scattering properties are considered. These scattering properties reflect the varied characteristics of land covers from which the electromagnetic waves are reflected back in SAR images.
By incorporating these input linguistic variables and utilizing the FL-based approach with the set of designed FI rules, the proposed method aims to adaptively assign weights to pixels based on their scattering properties. This adaptive weighting strategy takes into account the inter-pixel similarities in scattering properties, allowing for more effective speckle noise suppression while preserving important image features.

The use of FL in this method leverages its ability to handle uncertainties and perform unique processing for each pixel, enhancing the despeckling performance and potentially improving the interpretability and analysis of SAR images.


### The Novel 125 FI rules designed in this work
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
