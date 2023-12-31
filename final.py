# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16aQy1ORtmGVhPg95iW1dWuQdnkG_KqDf
"""

#importing all the required libraries
from datetime import datetime
start_time = datetime.now()
import scipy.io as sio
import os
import numpy as np
from sklearn.feature_extraction import image
from matplotlib import pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from matplotlib import pyplot as plt
from skimage import io

wsize=5 #window size as 5
total=[]
size= 500 #work with 500*500 image patch
defuzz_values= np.zeros((size,size))
names_ea= ['/Stokes1_A new.mat','/Stokes1_phi new.mat','/lambda new.mat'] #these .mat files are related to ALOS PALSAR 1.1 satellite data
key=['a']
for i in range(len(names_ea)):
        total.append((sio.loadmat(os.getcwd()+names_ea[i])[key[0]][0:size,0:size]))
print(len(total))


mdiff_amplitude= np.amax(total[0][:,:])-np.amin(total[0][:,:]) #dynamic range for amplitude
mdiff_phase= np.amax(total[1][:,:])-np.amin(total[1][:,:]) #dynamic range for phase
mdiff_lambda= np.amax(total[2][:,:])-np.amin(total[2][:,:]) #dynamic range for lambda

mship_amplitude = ctrl.Antecedent(np.linspace(0,mdiff_amplitude,num=100,endpoint=True), 'mship_amplitude') #creating universe of discourse for amplitude
mship_phase = ctrl.Antecedent(np.linspace(0,mdiff_phase,num=100,endpoint=True), 'mship_phase') #creating universe of discourse for phase
mship_lambda = ctrl.Antecedent(np.linspace(0,mdiff_lambda,num=100,endpoint=True), 'mship_lambda') #creating universe of discourse for lambda
wt = ctrl.Consequent(np.linspace(0,1,num=100,endpoint=True), 'wt') ##creating universe of discourse for output weight

#To ensure the ouput dimension remain same
amplitude= np.pad(total[0][:,:],int(wsize//2),mode='median') 
phase= np.pad(total[1][:,:],int(wsize//2),mode='median')
lamb = np.pad(total[2][:,:],int(wsize//2),mode='median')

#dividing the amplitude , phase and lambda  into overlapping patches
amplitude= image.extract_patches_2d(amplitude, (wsize,wsize))
phase= image.extract_patches_2d(phase, (wsize,wsize))
lamb= image.extract_patches_2d(lamb, (wsize,wsize))

# The mathematical expression for a Gaussian function is given by
# μj(x) = exp{-0.5*[(x −cj) / σj]2}
# where
# j = {1, 2, 3, 4, 5},
# c is the center of the peak,
# σ = 0.5*(cj− cj−1) / √[−2*ln(†)], determines the width of the curve,
# † = crossing point of adjacent MFs (default for † is 0.5).
# To determine the centers, cj, you need to compute the sub-interval between each peak, (cj− cj−1), where the 5 fuzzy sets are uniformly distributed to cover the domain of e:
# n = number of MFs,
# range = b − a,
# partition = n − 1,
# sub-interval = range / partition.
# For example, if the universe of discourse for “ERROR” would be the interval [−5, 5], then the sub-interval = 10 / 4 = 2.5, and the centers would be {−5, −2.5, 0, 2.5, 5}.
# The standard deviation, σ = 0.5*(2.5) / √[−2*ln(0.5)] ≈ 1.06165.

#calculating the width of the gaussian curve
sd1= 0.5*mdiff_amplitude/(np.sqrt(-2*np.log(0.5))*4)
sd2= 0.5*mdiff_phase/(np.sqrt(-2*np.log(0.5))*4)
sd3= 0.5*mdiff_lambda/(np.sqrt(-2*np.log(0.5))*4)

sd4= 0.5*1/(np.sqrt(-2*np.log(0.5))*4)

"""

VLFVD   -> Very Low First Variable Difference [ VLDPD]
LFVD - Low First Variable Difference [LDPD]
AFVD = Average First variable DIfference [ADPD]
VHFVD - Very High FIrst Variable Difference [VHDPD]
HFVD - HIgh First Variable Difference [HDPD]

VLSVD   -> Very Low Second Variable Difference [VLSDD]
LSVD - Low Second Variable Difference [LSDD]
ASVD = Average Second variable DIfference [ASDD]
VHSVD - Very High Second Variable Difference [VHSDD]
HSVD - HIgh Second Variable Difference [HSDD]

VLTVD   -> Very Low Third Variable Difference [VLSPD]
LTVD - Low Third Variable Difference [LSPD]
ATVD = Average Third variable DIfference [ASPD]
VHTVD - Very High Third Variable Difference [VHSPD]
HTVD - HIgh Third Variable Difference [HSPD]


VLW - Very Low Weight
LW - Low Weight
AW - Average Weight
HW - High Weight
VHW - VEry High Weight

"""
mship_amplitude['VLFVD'] = fuzz.gaussmf(mship_amplitude.universe, 0.01, sd1)
mship_amplitude['LFVD'] = fuzz.gaussmf(mship_amplitude.universe, 0.2, sd1)
mship_amplitude['AFVD'] = fuzz.gaussmf(mship_amplitude.universe, 0.4, sd1)
mship_amplitude['HFVD'] = fuzz.gaussmf(mship_amplitude.universe, 0.6, sd1)
mship_amplitude['VHFVD'] = fuzz.gaussmf(mship_amplitude.universe, 0.8, sd1)

mship_phase['VLSVD'] = fuzz.gaussmf(mship_phase.universe, 0.01, sd2)
mship_phase['LSVD'] = fuzz.gaussmf(mship_phase.universe, 0.2, sd2)
mship_phase['ASVD'] = fuzz.gaussmf(mship_phase.universe, 0.4, sd2)
mship_phase['HSVD'] = fuzz.gaussmf(mship_phase.universe, 0.6, sd2)
mship_phase['VHSVD'] = fuzz.gaussmf(mship_phase.universe, 0.8, sd2)

mship_lambda['VLTVD'] = fuzz.gaussmf(mship_lambda.universe, 0.01, sd3)
mship_lambda['LTVD'] = fuzz.gaussmf(mship_lambda.universe, 0.2, sd3)
mship_lambda['ATVD'] = fuzz.gaussmf(mship_lambda.universe, 0.4, sd3)
mship_lambda['HTVD'] = fuzz.gaussmf(mship_lambda.universe, 0.6, sd3)
mship_lambda['VHTVD'] = fuzz.gaussmf(mship_lambda.universe, 0.8, sd3)


wt['VLW'] = fuzz.gaussmf(wt.universe, 0.01, sd4)
wt['LW'] = fuzz.gaussmf(wt.universe, 0.2, sd4)
wt['AW'] = fuzz.gaussmf(wt.universe, 0.4, sd4)
wt['HW'] = fuzz.gaussmf(wt.universe, 0.6, sd4)
wt['VHW'] = fuzz.gaussmf(wt.universe, 0.8, sd4)

# You can see how these look with .view()
mship_amplitude['VLFVD'].view()


mship_phase['VLSVD'].view()


mship_lambda['VLTVD'].view()

wt['VLW'].view()


"""
    Design of fuzzy rules wrt to antecedent and consequent membership values
"""
rule1 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['VLSVD'] &mship_lambda['VLTVD'], wt['VHW'])
rule2 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['VLSVD'] &mship_lambda['LTVD'], wt['VHW'])
rule3 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['VLSVD'] &mship_lambda['ATVD'], wt['VHW'])
rule4 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['VLSVD'] &mship_lambda['HTVD'], wt['VHW'])
rule5 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['VLSVD'] &mship_lambda['VHTVD'], wt['VHW'])

rule6 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['LSVD'] &mship_lambda['VLTVD'], wt['VHW'])
rule7 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['LSVD'] &mship_lambda['LTVD'], wt['VHW'])
rule8 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['LSVD'] &mship_lambda['ATVD'], wt['VHW'])
rule9 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['LSVD'] &mship_lambda['HTVD'], wt['HW'])
rule10 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['LSVD'] &mship_lambda['VHTVD'], wt['HW'])

rule11 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['ASVD'] &mship_lambda['VLTVD'], wt['VHW'])
rule12 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['ASVD'] &mship_lambda['LTVD'], wt['HW'])
rule13 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['ASVD'] &mship_lambda['ATVD'], wt['AW'])
rule14 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['ASVD'] &mship_lambda['HTVD'], wt['AW'])
rule15 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['ASVD'] &mship_lambda['VHTVD'], wt['LW'])

rule16 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['HSVD'] &mship_lambda['VLTVD'], wt['VHW'])
rule17 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['HSVD'] &mship_lambda['LTVD'], wt['AW'])
rule18 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['HSVD'] &mship_lambda['ATVD'], wt['AW'])
rule19 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['HSVD'] &mship_lambda['HTVD'], wt['LW'])
rule20 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['HSVD'] &mship_lambda['VHTVD'], wt['LW'])

rule21 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['VHSVD'] &mship_lambda['VLTVD'], wt['HW'])
rule22 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['VHSVD'] &mship_lambda['LTVD'], wt['HW'])
rule23 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['VHSVD'] &mship_lambda['ATVD'], wt['AW'])
rule24 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['VHSVD'] &mship_lambda['HTVD'], wt['AW'])
rule25 = ctrl.Rule(mship_amplitude['VLFVD'] &mship_phase['VHSVD'] &mship_lambda['VHTVD'], wt['AW'])



rule26 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['VLSVD'] &mship_lambda['VLTVD'], wt['VHW'])
rule27 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['VLSVD'] &mship_lambda['LTVD'], wt['VHW'])
rule28 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['VLSVD'] &mship_lambda['ATVD'], wt['VHW'])
rule29 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['VLSVD'] &mship_lambda['HTVD'], wt['HW'])
rule30 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['VLSVD'] &mship_lambda['VHTVD'], wt['AW'])

rule31 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['LSVD'] &mship_lambda['VLTVD'], wt['VHW'])
rule32 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['LSVD'] &mship_lambda['LTVD'], wt['HW'])
rule33 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['LSVD'] &mship_lambda['ATVD'], wt['HW'])
rule34 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['LSVD'] &mship_lambda['HTVD'], wt['HW'])
rule35 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['LSVD'] &mship_lambda['VHTVD'], wt['AW'])

rule36 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['ASVD'] &mship_lambda['VLTVD'], wt['HW'])
rule37 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['ASVD'] &mship_lambda['LTVD'], wt['HW'])
rule38 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['ASVD'] &mship_lambda['ATVD'], wt['AW'])
rule39 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['ASVD'] &mship_lambda['HTVD'], wt['AW'])
rule40 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['ASVD'] &mship_lambda['VHTVD'], wt['AW'])

rule41 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['HSVD'] &mship_lambda['VLTVD'], wt['HW'])
rule42 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['HSVD'] &mship_lambda['LTVD'], wt['HW'])
rule43 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['HSVD'] &mship_lambda['ATVD'], wt['AW'])
rule44 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['HSVD'] &mship_lambda['HTVD'], wt['LW'])
rule45 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['HSVD'] &mship_lambda['VHTVD'], wt['LW'])

rule46 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['VHSVD'] &mship_lambda['VLTVD'], wt['HW'])
rule47 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['VHSVD'] &mship_lambda['LTVD'], wt['HW'])
rule48 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['VHSVD'] &mship_lambda['ATVD'], wt['AW'])
rule49 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['VHSVD'] &mship_lambda['HTVD'], wt['LW'])
rule50 = ctrl.Rule(mship_amplitude['LFVD'] &mship_phase['VHSVD'] &mship_lambda['VHTVD'], wt['LW'])



rule51 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['VLSVD'] &mship_lambda['VLTVD'], wt['VHW'])
rule52 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['VLSVD'] &mship_lambda['LTVD'], wt['HW'])
rule53 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['VLSVD'] &mship_lambda['ATVD'], wt['HW'])
rule54 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['VLSVD'] &mship_lambda['HTVD'], wt['AW'])
rule55 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['VLSVD'] &mship_lambda['VHTVD'], wt['LW'])

rule56 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['LSVD'] &mship_lambda['VLTVD'], wt['HW'])
rule57 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['LSVD'] &mship_lambda['LTVD'], wt['HW'])
rule58 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['LSVD'] &mship_lambda['ATVD'], wt['HW'])
rule59 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['LSVD'] &mship_lambda['HTVD'], wt['AW'])
rule60 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['LSVD'] &mship_lambda['VHTVD'], wt['LW'])

rule61 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['ASVD'] &mship_lambda['VLTVD'], wt['HW'])
rule62 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['ASVD'] &mship_lambda['LTVD'], wt['HW'])
rule63 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['ASVD'] &mship_lambda['ATVD'], wt['AW'])
rule64 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['ASVD'] &mship_lambda['HTVD'], wt['AW'])
rule65 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['ASVD'] &mship_lambda['VHTVD'], wt['LW'])

rule66 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['HSVD'] &mship_lambda['VLTVD'], wt['AW'])
rule67 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['HSVD'] &mship_lambda['LTVD'], wt['AW'])
rule68 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['HSVD'] &mship_lambda['ATVD'], wt['AW'])
rule69 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['HSVD'] &mship_lambda['HTVD'], wt['LW'])
rule70 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['HSVD'] &mship_lambda['VHTVD'], wt['LW'])

rule71 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['VHSVD'] &mship_lambda['VLTVD'], wt['AW'])
rule72 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['VHSVD'] &mship_lambda['LTVD'], wt['AW'])
rule73 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['VHSVD'] &mship_lambda['ATVD'], wt['LW'])
rule74 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['VHSVD'] &mship_lambda['HTVD'], wt['LW'])
rule75 = ctrl.Rule(mship_amplitude['AFVD'] &mship_phase['VHSVD'] &mship_lambda['VHTVD'], wt['LW'])



rule76 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['VLSVD'] &mship_lambda['VLTVD'], wt['HW'])
rule77 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['VLSVD'] &mship_lambda['LTVD'], wt['HW'])
rule78 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['VLSVD'] &mship_lambda['ATVD'], wt['AW'])
rule79 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['VLSVD'] &mship_lambda['HTVD'], wt['LW'])
rule80 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['VLSVD'] &mship_lambda['VHTVD'], wt['LW'])

rule81 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['LSVD'] &mship_lambda['VLTVD'], wt['HW'])
rule82 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['LSVD'] &mship_lambda['LTVD'], wt['HW'])
rule83 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['LSVD'] &mship_lambda['ATVD'], wt['AW'])
rule84 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['LSVD'] &mship_lambda['HTVD'], wt['LW'])
rule85 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['LSVD'] &mship_lambda['VHTVD'], wt['LW'])

rule86 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['ASVD'] &mship_lambda['VLTVD'], wt['AW'])
rule87 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['ASVD'] &mship_lambda['LTVD'], wt['AW'])
rule88 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['ASVD'] &mship_lambda['ATVD'], wt['LW'])
rule89 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['ASVD'] &mship_lambda['HTVD'], wt['LW'])
rule90 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['ASVD'] &mship_lambda['VHTVD'], wt['LW'])

rule91 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['HSVD'] &mship_lambda['VLTVD'], wt['AW'])
rule92 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['HSVD'] &mship_lambda['LTVD'], wt['LW'])
rule93 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['HSVD'] &mship_lambda['ATVD'], wt['LW'])
rule94 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['HSVD'] &mship_lambda['HTVD'], wt['LW'])
rule95 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['HSVD'] &mship_lambda['VHTVD'], wt['VLW'])

rule96 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['VHSVD'] &mship_lambda['VLTVD'], wt['AW'])
rule97 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['VHSVD'] &mship_lambda['LTVD'], wt['LW'])
rule98 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['VHSVD'] &mship_lambda['ATVD'], wt['LW'])
rule99 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['VHSVD'] &mship_lambda['HTVD'], wt['VLW'])
rule100 = ctrl.Rule(mship_amplitude['HFVD'] &mship_phase['VHSVD'] &mship_lambda['VHTVD'], wt['VLW'])



rule101 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['VLSVD'] &mship_lambda['VLTVD'], wt['HW'])
rule102 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['VLSVD'] &mship_lambda['LTVD'], wt['HW'])
rule103 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['VLSVD'] &mship_lambda['ATVD'], wt['AW'])
rule104 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['VLSVD'] &mship_lambda['HTVD'], wt['AW'])
rule105 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['VLSVD'] &mship_lambda['VHTVD'], wt['AW'])

rule106 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['LSVD'] &mship_lambda['VLTVD'], wt['HW'])
rule107 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['LSVD'] &mship_lambda['LTVD'], wt['HW'])
rule108 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['LSVD'] &mship_lambda['ATVD'], wt['AW'])
rule109 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['LSVD'] &mship_lambda['HTVD'], wt['LW'])
rule110 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['LSVD'] &mship_lambda['VHTVD'], wt['LW'])

rule111 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['ASVD'] &mship_lambda['VLTVD'], wt['AW'])
rule112 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['ASVD'] &mship_lambda['LTVD'], wt['AW'])
rule113 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['ASVD'] &mship_lambda['ATVD'], wt['AW'])
rule114 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['ASVD'] &mship_lambda['HTVD'], wt['LW'])
rule115 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['ASVD'] &mship_lambda['VHTVD'], wt['LW'])

rule116 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['HSVD'] &mship_lambda['VLTVD'], wt['LW'])
rule117 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['HSVD'] &mship_lambda['LTVD'], wt['LW'])
rule118 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['HSVD'] &mship_lambda['ATVD'], wt['LW'])
rule119 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['HSVD'] &mship_lambda['HTVD'], wt['VLW'])
rule120 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['HSVD'] &mship_lambda['VHTVD'], wt['VLW'])

rule121 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['VHSVD'] &mship_lambda['VLTVD'], wt['LW'])
rule122 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['VHSVD'] &mship_lambda['LTVD'], wt['LW'])
rule123 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['VHSVD'] &mship_lambda['ATVD'], wt['LW'])
rule124 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['VHSVD'] &mship_lambda['HTVD'], wt['VLW'])
rule125 = ctrl.Rule(mship_amplitude['VHFVD'] &mship_phase['VHSVD'] &mship_lambda['VHTVD'], wt['VLW'])




# rule23.view()
r_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
                                   rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
                                   rule20, rule21,rule22, rule23, rule24, rule25,
                             rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35,
                                   rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44,
                                   rule45, rule46,rule47, rule48, rule49, rule50,
                             rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60,
                                   rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69,
                                   rule70, rule71,rule72, rule73, rule74, rule75,
                             rule76, rule77, rule78, rule79, rule80, rule81, rule82, rule83, rule84, rule85,
                                   rule86, rule87, rule88, rule89, rule90, rule91, rule92, rule93, rule94,
                                   rule95, rule96,rule97, rule98, rule99, rule100,
                             rule101, rule102, rule103, rule104, rule105, rule106, rule107, rule108, rule109, rule110,
                                   rule111, rule112, rule113, rule114, rule115, rule116, rule117, rule118, rule119,
                                   rule120, rule121,rule122, rule123, rule124, rule125])
e=['very low','low','medium','high','very high']
a=['very small','small','average','large','very large']
r=['very large weight','largeweight','averageweight','small weight']

"""
    Method of defuzzification
"""

defuzz=[]
for i in range(amplitude.shape[0]):
  diff_amplitude= np.abs(amplitude[i,:,:]-amplitude[i,wsize//2,wsize//2])
  diff_phase= np.abs(phase[i,:,:]-phase[i,wsize//2,wsize//2])
  diff_lambda= np.abs(lamb[i,:,:]-lamb[i,wsize//2,wsize//2])
  r_all = ctrl.ControlSystemSimulation(r_ctrl)
  r_all.input['mship_amplitude'] = diff_amplitude#pixel of amplitude
  r_all.input['mship_phase'] = diff_phase#pixel of phase
  r_all.input['mship_lambda'] = diff_lambda#pixel of lambda
  r_all.compute()
  # Crunch the numbers
      # defuzz[i]=r_all.output['wt']
  defuzz.append(r_all.output['wt'])
  #         # print (r_all.output['randomness'])
  # randomness.view(sim=r_all)

#filter noisy image based on defuzzified values
pau_rgb= plt.imread(os.getcwd()+'/RGB1_nosiy_0.5.jpg')[0:size,0:size] #pauli image is generated using polsarpro
pau_rpatches= np.pad(pau_rgb,int(wsize//2),mode='median')
#pau_gpatches= np.pad(pau_rgb[:,:,1],int(wsize//2),mode='median')
#pau_bpatches= np.pad(pau_rgb[:,:,2],int(wsize//2),mode='median')
plt.imshow(pau_rgb,cmap=plt.cm.gray)
pau_rpatches= image.extract_patches_2d(pau_rpatches, (wsize,wsize))
#pau_gpatches= image.extract_patches_2d(pau_gpatches, (wsize,wsize))
#pau_bpatches= image.extract_patches_2d(pau_bpatches, (wsize,wsize))


for i in range(pau_rpatches.shape[0]):
  wavg_r= np.sum(defuzz[i]*pau_rpatches[i]/wsize**2)
  #wavg_g= np.sum(defuzz[i]*pau_gpatches[i]/wsize**2)
  #wavg_b= np.sum(defuzz[i]*pau_bpatches[i]/wsize**2)
  if wavg_r!=0:
    std= np.std(defuzz[i]*pau_rpatches[i])
    enls= (wavg_r/std)**2
    sx2= ((enls*std**2)-wavg_r**2)/(enls+1)
    xcap= wavg_r + (sx2*(pau_rpatches[i,wsize//2,wsize//2]-wavg_r)/(sx2+(wavg_r**2/enls)))
    pau_rpatches[i,wsize//2,wsize//2] = xcap
  # if wavg_g!=0:
  #   std= np.std(defuzz[i]*pau_gpatches[i])
  #   enls= (wavg_g/std)**2
  #   sx2= ((enls*std**2)-wavg_g**2)/(enls+1)
  #   xcap= wavg_g + (sx2*(pau_rpatches[i,wsize//2,wsize//2]-wavg_g)/(sx2+(wavg_g**2/enls)))
  #   pau_gpatches[i,wsize//2,wsize//2] = xcap
  # if wavg_b!=0:
  #   std= np.std(defuzz[i]*pau_bpatches[i])
  #   enls= (wavg_b/std)**2
  #   sx2= ((enls*std**2)-wavg_b**2)/(enls+1)
  #   xcap= wavg_b + (sx2*(pau_rpatches[i,wsize//2,wsize//2]-wavg_b)/(sx2+(wavg_b**2/enls)))
  #   pau_bpatches[i,wsize//2,wsize//2] = xcap

final= pau_rpatches[:,wsize//2,wsize//2].reshape(size,size)
# final_g= pau_gpatches[:,wsize//2,wsize//2].reshape(size,size)
# final_b= pau_bpatches[:,wsize//2,wsize//2].reshape(size,size)
# merged= np.dstack((final_r,final_g,final_b))
plt.imshow(final,cmap=plt.cm.gray)

io.imsave(os.getcwd()+'/RGB1_nosiy_0.5_gaussf.jpg',final)


time_elapsed = datetime.now() - start_time
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

# patch_size=[32,64,128,256,500]
# time=[6,24,106,430,1606]

# plt.grid()
# plt.plot(patch_size,time,'go--', label='line 1', linewidth=2)
# plt.xlabel('Patch Size')
# plt.ylabel('Time Taken (in s)')

