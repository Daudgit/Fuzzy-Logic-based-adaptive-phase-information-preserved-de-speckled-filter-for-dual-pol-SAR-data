# Copyright Name
**Fuzzy Logic based adaptive phase information preserved de-speckled filter for dual polarized SAR data**

## Patent Information
- Diary number: 3869/2023-CO/SW
- Registration Number: SW-16607/2023
- Citation link: [SK Daud Hassan, Debanka Pal , Sriparna Banerjee, Sheli Sinha Chaudhuri, "Fuzzy Logic based adaptive phase information preserved de-speckled filter for dual polarized SAR data"](https://www.researchgate.net/publication/371607909_Fuzzy_Logic_based_adaptive_phase_information_preserved_de-speckled_filter_for_dual_polarized_SAR_data) (Registered)

## Description
In the proposed method, a fuzzy logic (FL) based adaptive weighted despeckling approach is employed to handle uncertainties and process each pixel uniquely based on its properties. FL is chosen due to its capability to handle uncertainties effectively.

For the implementation of the FL-based despeckling strategy, a set of 125 novel fuzzy inference (FI) rules has been designed. These rules serve as guidelines for the FL system to determine the appropriate weights for despeckling each pixel. The output of the FL system is the weight, which is the linguistic variable indicating the level of speckle noise to be removed.

To define the input linguistic variables, different combinations of scattering properties are considered. These scattering properties reflect the varied characteristics of land covers from which the electromagnetic waves are reflected back in SAR images.Table 1 provides the scattering parameters (PAR) considered in this work, while Table 2 presents the combinations of scattering parameters used as input linguistic variables in the FI rules.
By incorporating these input linguistic variables and utilizing the FL-based approach with the set of designed FI rules, the proposed method aims to adaptively assign weights to pixels based on their scattering properties. This adaptive weighting strategy takes into account the inter-pixel similarities in scattering properties, allowing for more effective speckle noise suppression while preserving important image features.

The use of FL in this method leverages its ability to handle uncertainties and perform unique processing for each pixel, enhancing the despeckling performance and potentially improving the interpretability and analysis of SAR images.
TABLE I. 	SCATTERING PARAMETERS CONSIDERED FOR THIS WORK
PAR 1 	PAR 2	PAR 3	PAR 4 	PAR 5	PAR 6
ZDR_11_21
(Z_1_2)	ZDR_21_11
(Z_2_1)	Entropy
(EN)	Anisotropy
(AN)	Alpha
(AL)	Delta
(DL)

TABLE II. 	DIFFERENT COMBINATIONS OF SCATTERING PARAMETERS CONSIDERED IN THIS WORK 
COM	PARAMETERS	COM	PARAMETERS
123	Z_1_2	Z_2_1	EN	124	Z_1_2	Z_2_1	AN
125	Z_1_2	Z_2_1	AL	126	Z_1_2	Z_2_1	DL
134	Z_1_2	EN	AN	135	Z_1_2	EN	AL
136	Z_1_2	EN	DL	145	Z_1_2	AN	AL
146	Z_1_2	AN	DL	156	Z_1_2	AL	DL
234	Z_2_1	EN	AN	235	Z_2_1	EN	AL
236	Z_2_1	EN	DL	245	Z_2_1	AN	AL
246	Z_2_1	AN	DL	256	Z_2_1	AL	DL
345	EN	AN	AL	346	EN	AN	DL
356	EN	AL	DL	456	AN	AL	DL
All these scattering parameters are extracted using POLSARpro software where the details of these parameters are also given. 
I have designed the FI rules considering three input linguistic variables namely, First linguistic variable, Second linguistic variable and Third linguistic variable as input linguistic variables and weight as output linguistic variable. 
The input linguistic variables can be any of these combinations. Both qualitative and quantitative results are generated for each of these combinations using four different fully polarized ALOS PALSAR data. Novel 125 FI rules designed in this work for performing despeckling are given in Table 3 and pseudo-code of the proposed despeckling strategy is given in Fig.1.
Table III – List of 125 Rules
Rule	First linguistic variable	Second linguistic variable	Third linguistic variable	Output linguistic variable	Rule	First linguistic variable	Second linguistic variable	Third linguistic variable	Output linguistic variable
1	VLFVD	VLSVD	VLTVD	VHW	62	AFVD	ASVD	LTVD	HW
2	VLFVD	VLSVD	LTVD	VHW	63	AFVD	ASVD	ATVD	AW
3	VLFVD	VLSVD	ATVD	VHW	64	AFVD	ASVD	HTVD	AW
4	VLFVD	VLSVD	HTVD	VHW	65	AFVD	ASVD	VHTVD	LW
5	VLFVD	VLSVD	VHTVD	VHW	66	AFVD	HSVD	VLTVD	AW
6	VLFVD	LSVD	VLTVD	VHW	67	AFVD	HSVD	LTVD	AW
7	VLFVD	LSVD	LTVD	VHW	68	AFVD	HSVD	ATVD	AW
8	VLFVD	LSVD	ATVD	VHW	69	AFVD	HSVD	HTVD	LW
9	VLFVD	LSVD	HTVD	HW	70	AFVD	HSVD	VHTVD	LW
10	VLFVD	LSVD	VHTVD	HW	62	AFVD	ASVD	LTVD	HW
11	VLFVD	ASVD	VLTVD	VHW	63	AFVD	ASVD	ATVD	AW
12	VLFVD	ASVD	LTVD	HW	64	AFVD	ASVD	HTVD	AW
13	VLFVD	ASVD	ATVD	AW	65	AFVD	ASVD	VHTVD	LW
14	VLFVD	ASVD	HTVD	AW	66	AFVD	HSVD	VLTVD	AW
15	VLFVD	ASVD	VHTVD	LW	67	AFVD	HSVD	LTVD	AW
16	VLFVD	HSVD	VLTVD	VHW	68	AFVD	HSVD	ATVD	AW
17	VLFVD	HSVD	LTVD	AW	69	AFVD	HSVD	HTVD	LW
18	VLFVD	HSVD	ATVD	AW	70	AFVD	HSVD	VHTVD	LW
19	VLFVD	HSVD	HTVD	LW	71	AFVD	VHSVD	VLTVD	AW
20	VLFVD	HSVD	VHTVD	LW	72	AFVD	VHSVD	LTVD	AW
21	VLFVD	VHSVD	VLTVD	HW	73	AFVD	VHSVD	ATVD	LW
22	VLFVD	VHSVD	LTVD	HW	74	AFVD	VHSVD	HTVD	LW
23	VLFVD	VHSVD	ATVD	AW	75	AFVD	VHSVD	VHTVD	LW
24	VLFVD	VHSVD	HTVD	AW	76	HFVD	VLSVD	VLTVD	HW
25	VLFVD	VHSVD	VHTVD	AW	77	HFVD	VLSVD	LTVD	HW
26	LFVD	VLSVD	VLTVD	VHW	78	HFVD	VLSVD	ATVD	AW
27	LFVD	VLSVD	LTVD	VHW	79	HFVD	VLSVD	HTVD	LW
28	LFVD	VLSVD	ATVD	VHW	80	HFVD	VLSVD	VHTVD	LW
29	LFVD	VLSVD	HTVD	VHW	81	HFVD	LSVD	VLTVD	HW
30	LFVD	VLSVD	VHTVD	VHW	82	HFVD	LSVD	LTVD	HW
31	LFVD	LSVD	VLTVD	VHW	83	HFVD	LSVD	ATVD	AW
32	LFVD	LSVD	LTVD	VHW	84	HFVD	LSVD	HTVD	LW
33	LFVD	LSVD	ATVD	HW	85	HFVD	LSVD	VHTVD	LW
34	LFVD	LSVD	HTVD	HW	86	HFVD	ASVD	VLTVD	AW
35	LFVD	LSVD	VHTVD	AW	87	HFVD	ASVD	LTVD	AW
36	LFVD	ASVD	VLTVD	HW	88	HFVD	ASVD	ATVD	LW
37	LFVD	ASVD	LTVD	HW	89	HFVD	ASVD	HTVD	LW
38	LFVD	ASVD	ATVD	AW	90	HFVD	ASVD	VHTVD	LW
39	LFVD	ASVD	HTVD	AW	91	HFVD	HSVD	VLTVD	AW
40	LFVD	ASVD	VHTVD	AW	92	HFVD	HSVD	LTVD	LW
41	LFVD	HSVD	VLTVD	HW	93	HFVD	HSVD	ATVD	LW
42	LFVD	HSVD	LTVD	HW	94	HFVD	HSVD	HTVD	LW
43	LFVD	HSVD	ATVD	AW	95	HFVD	HSVD	VHTVD	VLW
44	LFVD	HSVD	HTVD	LW	96	HFVD	VHSVD	VLTVD	AW
45	LFVD	HSVD	VHTVD	LW	97	HFVD	VHSVD	LTVD	LW
46	LFVD	VHSVD	VLTVD	HW	98	HFVD	VHSVD	ATVD	LW
47	LFVD	VHSVD	LTVD	HW	99	HFVD	VHSVD	HTVD	VLW
48	LFVD	VHSVD	ATVD	AW	100	HFVD	VHSVD	VHTVD	VLW
49	LFVD	VHSVD	HTVD	LW	101	VHFVD	VLSVD	VLTVD	HW
50	LFVD	VHSVD	VHTVD	LW	102	VHFVD	VLSVD	LTVD	HW
51	AFVD	VLSVD	VLTVD	VHW	103	VHFVD	VLSVD	ATVD	AW
52	AFVD	VLSVD	LTVD	HW	104	VHFVD	VLSVD	HTVD	AW
53	AFVD	VLSVD	ATVD	HW	105	VHFVD	VLSVD	VHTVD	AW
54	AFVD	VLSVD	HTVD	AW	106	VHFVD	LSVD	VLTVD	HW
55	AFVD	VLSVD	VHTVD	LW	107	VHFVD	LSVD	LTVD	HW
56	AFVD	LSVD	VLTVD	HW	108	VHFVD	LSVD	ATVD	AW
57	AFVD	LSVD	LTVD	HW	109	VHFVD	LSVD	HTVD	LW
58	AFVD	LSVD	ATVD	HW	110	VHFVD	LSVD	VHTVD	LW
59	AFVD	LSVD	HTVD	AW	103	VHFVD	VLSVD	ATVD	AW
60	AFVD	LSVD	VHTVD	LW	104	VHFVD	VLSVD	HTVD	AW
61	AFVD	ASVD	VLTVD	HW	105	VHFVD	VLSVD	VHTVD	AW
106	VHFVD	LSVD	VLTVD	HW	116	VHFVD	HSVD	VLTVD	LW
107	VHFVD	LSVD	LTVD	HW	117	VHFVD	HSVD	LTVD	LW
108	VHFVD	LSVD	ATVD	AW	118	VHFVD	HSVD	ATVD	LW
109	VHFVD	LSVD	HTVD	LW	119	VHFVD	HSVD	HTVD	VLW
110	VHFVD	LSVD	VHTVD	LW	120	VHFVD	HSVD	VHTVD	VLW
111	VHFVD	ASVD	VLTVD	AW	121	VHFVD	VHSVD	VLTVD	LW
112	VHFVD	ASVD	LTVD	AW	122	VHFVD	VHSVD	LTVD	LW
113	VHFVD	ASVD	ATVD	AW	123	VHFVD	VHSVD	ATVD	LW
114	VHFVD	ASVD	HTVD	LW	124	VHFVD	VHSVD	HTVD	VLW
115	VHFVD	ASVD	VHTVD	LW	125	VHFVD	VHSVD	VHTVD	VLW

*Note: Linguistic values corresponding to First Linguistic variable {Very Low First Variable Difference (VLFVD), Low First Variable Difference (LFVD), Average First Variable Difference (AFVD), High First Variable Difference (HFVD) and Very High First Variable Difference (VHFVD)}. Similar notations are followed for other linguistic variables also. 


