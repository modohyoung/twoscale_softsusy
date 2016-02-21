# SOFTSUSY3.3.9 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
# B.C. Allanach and M.A. Bernhardt, Comput. Phys. Commun. 181 (2010) 232,
# arXiv:0903.1805
# B.C. Allanach, M. Hanussek and C.H. Kom, arXiv:1109.3735
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.9       # version number
Block MODSEL  # Select model
     1    1   # sugra
     4    1   # R-parity violating
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
    21    4.75000000e-03   # Mdown(2 GeV) MSbar
    22    2.40000000e-03   # Mup(2 GeV) MSbar
    23    1.04000000e-01   # Mstrange(2 GeV) MSbar
    24    1.27000000e+00   # Mcharm(Mcharm) MSbar
    11    5.10998902e-04   # Me(pole)
    13    1.05658357e-01   # Mmu(pole)
Block VCKMIN               # input CKM mixing matrix parameters
     1    2.27200000e-01   # lambda
     2    8.18000000e-01   # A
     3    2.21000000e-01   # rhobar
     4    3.40000000e-01   # etabar (no phases used in SOFTSUSY yet though)
Block MINPAR               # SUSY breaking input parameters
     3    1.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    1.25000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.58158268e+16   # MX scale
Block RVLAMLLEIN           # input LLE couplings at MSUSY
  1 2 1   1.00000000e-02   # lambda_{121}
  2 1 1  -1.00000000e-02   # lambda_{211}
# SOFTSUSY-specific non SLHA information:
# MIXING=1 Desired accuracy=1.00000000e-03 Achieved accuracy=6.46894592e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04979680e+01   # MW
        25     1.14772531e+02   # CP even neutral scalar
        35     3.50851659e+02   # CP even neutral scalar
        36     3.50851659e+02   # CP odd neutral scalar
        37     2.22529860e+02   # charged scalar
   1000021     1.14758589e+03   # ~g
   1000022     2.05312862e+02   # ~neutralino(1)
   1000023     3.86890379e+02   # ~neutralino(2)
   1000024     3.86906791e+02   # ~chargino(1)
   1000025    -6.41601396e+02   # ~neutralino(3)
   1000035     6.54975272e+02   # ~neutralino(4)
   1000037     6.55303717e+02   # ~chargino(2)
   1000011     2.29693194e+02   # charged scalar
   1000013     2.29698679e+02   # charged scalar
   1000015     3.60786412e+02   # charged scalar
   2000011     3.60791084e+02   # charged scalar
   2000013     3.61213186e+02   # charged scalar
   2000015     7.20410217e+02   # charged scalar
   1000012     3.51848030e+02   # CP even neutral scalar
   1000014     3.51851369e+02   # CP even neutral scalar
   1000016     7.15668791e+02   # CP even neutral scalar
   1000017     3.51848030e+02   # CP odd neutral scalar
   1000018     3.51851369e+02   # CP odd neutral scalar
   1000019     7.15668791e+02   # CP odd neutral scalar
   1000001     9.67141317e+02   # ~d_1
   1000003     1.00410475e+03   # ~d_2
   1000005     1.01148258e+03   # ~d_3
   2000001     1.01148619e+03   # ~d_4
   2000003     1.05572559e+03   # ~d_5
   2000005     1.05574421e+03   # ~d_6
   1000002     8.06773303e+02   # ~u_1
   1000004     1.00252433e+03   # ~u_2
   1000006     1.01478057e+03   # ~u_3
   2000002     1.01478624e+03   # ~u_4
   2000004     1.05289926e+03   # ~u_5
   2000006     1.05290278e+03   # ~u_6
        12     3.10410509e-42   # Mnu1 inverted hierarchy output
        14     2.42388582e-14   # Mnu2 inverted hierarchy output
        16     0.00000000e+00   # Mnu3 inverted hierarchy output
Block RVNMIX  # neutrino-neutralino mixing matrix 
  1 1    0.00000000e+00   # N_{11}
  1 2    0.00000000e+00   # N_{12}
  1 3    1.00000000e+00   # N_{13}
  1 4    0.00000000e+00   # N_{14}
  1 5    0.00000000e+00   # N_{15}
  1 6    0.00000000e+00   # N_{16}
  1 7    0.00000000e+00   # N_{17}
  2 1    1.00000000e+00   # N_{21}
  2 2   -1.14404263e-14   # N_{22}
  2 3    0.00000000e+00   # N_{23}
  2 4   -1.28543283e-23   # N_{24}
  2 5   -3.86756461e-24   # N_{25}
  2 6   -1.84150384e-23   # N_{26}
  2 7   -2.34817849e-28   # N_{27}
  3 1    1.14404263e-14   # N_{31}
  3 2    1.00000000e+00   # N_{32}
  3 3    0.00000000e+00   # N_{33}
  3 4   -5.11541888e-10   # N_{34}
  3 5    5.31916784e-10   # N_{35}
  3 6   -2.48777367e-09   # N_{36}
  3 7    5.49513865e-12   # N_{37}
  4 1    2.25265296e-23   # N_{41}
  4 2    7.23556128e-10   # N_{42}
  4 3    0.00000000e+00   # N_{43}
  4 4    9.95875259e-01   # N_{44}
  4 5   -1.74464792e-02   # N_{45}
  4 6    8.22650965e-02   # N_{46}
  4 7   -3.40667536e-02   # N_{47}
  5 1   -1.05971751e-23   # N_{51}
  5 2   -9.83177804e-10   # N_{52}
  5 3    0.00000000e+00   # N_{53}
  5 4    3.75441341e-02   # N_{54}
  5 5    9.71535034e-01   # N_{55}
  5 6   -1.94911971e-01   # N_{56}
  5 7    1.29303675e-01   # N_{57}
  6 1    3.22077743e-23   # N_{61}
  6 2    1.70372262e-09   # N_{62}
  6 3    0.00000000e+00   # N_{63}
  6 4   -3.30394660e-02   # N_{64}
  6 5    4.81433810e-02   # N_{65}
  6 6    7.03490113e-01   # N_{66}
  6 7    7.08302385e-01   # N_{67}
  7 1   -2.99191309e-23   # N_{71}
  7 2   -1.52997248e-09   # N_{72}
  7 3    0.00000000e+00   # N_{73}
  7 4    7.57053573e-02   # N_{74}
  7 5   -2.31295296e-01   # N_{75}
  7 6   -6.78486137e-01   # N_{76}
  7 7    6.93128954e-01   # N_{77}
Block RVUMIX  # lepton-chargino mixing matrix U
  1 1   -1.00000000e+00   # U_{11}
  1 2   -3.08949317e-41   # U_{12}
  1 3    0.00000000e+00   # U_{13}
  1 4    5.85572938e-32   # U_{14}
  1 5   -1.07034912e-32   # U_{15}
  2 1    3.44237697e-41   # U_{21}
  2 2    1.00000000e+00   # U_{22}
  2 3    0.00000000e+00   # U_{23}
  2 4    3.56090709e-10   # U_{24}
  2 5   -4.15443825e-09   # U_{25}
  3 1    0.00000000e+00   # U_{31}
  3 2    0.00000000e+00   # U_{32}
  3 3    1.00000000e+00   # U_{33}
  3 4    0.00000000e+00   # U_{34}
  3 5    0.00000000e+00   # U_{35}
  4 1    5.92142841e-32   # U_{41}
  4 2   -1.50362290e-09   # U_{42}
  4 3    0.00000000e+00   # U_{43}
  4 4    9.60105549e-01   # U_{44}
  4 5   -2.79637863e-01   # U_{45}
  5 1    6.09835522e-33   # U_{51}
  5 2    3.88912278e-09   # U_{52}
  5 3    0.00000000e+00   # U_{53}
  5 4    2.79637863e-01   # U_{54}
  5 5    9.60105549e-01   # U_{55}
Block RVVMIX  # lepton-chargino mixing matrix V
  1 1   -1.00000000e+00   # V_{11}
  1 2    1.06948944e-81   # V_{12}
  1 3    0.00000000e+00   # V_{13}
  1 4    0.00000000e+00   # V_{14}
  1 5   -8.41404941e-53   # V_{15}
  2 1    1.69650515e-64   # V_{21}
  2 2    1.00000000e+00   # V_{22}
  2 3    0.00000000e+00   # V_{23}
  2 4    6.91471077e-13   # V_{24}
  2 5   -2.01627666e-12   # V_{25}
  3 1    0.00000000e+00   # V_{31}
  3 2    0.00000000e+00   # V_{32}
  3 3    1.00000000e+00   # V_{33}
  3 4    0.00000000e+00   # V_{34}
  3 5    0.00000000e+00   # V_{35}
  4 1    1.53438111e-53   # V_{41}
  4 2   -1.04756348e-12   # V_{42}
  4 3    0.00000000e+00   # V_{43}
  4 4    9.83231938e-01   # V_{44}
  4 5   -1.82359412e-01   # V_{45}
  5 1   -8.27296211e-53   # V_{51}
  5 2    1.85637135e-12   # V_{52}
  5 3    0.00000000e+00   # V_{53}
  5 4    1.82359412e-01   # V_{54}
  5 5    9.83231938e-01   # V_{55}
Block gauge Q= 8.76213736e+02  # SM gauge couplings
     1     3.62703303e-01   # g'(Q)MSSM DRbar
     2     6.42356574e-01   # g(Q)MSSM DRbar
     3     1.06432997e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.76213736e+02   # diagonal Up Yukawa matrix
  1  1     7.33201560e-06    # YU_{11}(Q)MSSM DRbar
  2  2     3.35859867e-03    # YU_{22}(Q)MSSM DRbar
  3  3     8.57849854e-01    # YU_{33}(Q)MSSM DRbar
Block yd Q= 8.76213736e+02   # diagonal down Yukawa matrix
  1  1     1.41240722e-04    # YD_{11}(Q)MSSM DRbar
  2  2     3.09248740e-03    # YD_{22}(Q)MSSM DRbar
  3  3     1.34892917e-01    # YD_{33}(Q)MSSM DRbar
Block ye Q= 8.76213736e+02   # diagonal lepton Yukawa matrix
  1  1     2.79085541e-05    # YE_{11}(Q)MSSM DRbar
  2  2     5.77060285e-03    # YE_{22}(Q)MSSM DRbar
  3  3     1.00322654e-01    # YE_{33}(Q)MSSM DRbar
Block hmix Q= 8.76213736e+02 # Higgs mixing parameters
     1     6.36154524e+02    # mu(Q)MSSM DRbar
     2     9.67531553e+00    # tan beta(Q)MSSM DRbar
     3     2.44501879e+02    # higgs vev(Q)MSSM DRbar
     4     5.31447394e+05    # mA^2(Q)MSSM DRbar
Block RVLAMLLE Q= 8.76213736e+02 # non-zero R-Parity violating LLE couplings 
  1 2 1    1.00000172e-02   # lambda_{121}
  1 2 2    3.66350606e-42   # lambda_{122}
  1 3 3    2.11372260e-41   # lambda_{133}
  2 1 1   -1.00000172e-02   # lambda_{211}
  2 1 2   -3.66350606e-42   # lambda_{212}
  2 3 3    2.98275731e-14   # lambda_{233}
  3 1 3   -2.11372260e-41   # lambda_{313}
  3 2 3   -2.98275731e-14   # lambda_{323}
Block RVLAMLQD Q= 8.76213736e+02 # non-zero R-Parity violating LQD couplings 
  1 1 1    2.97581771e-44   # lambda'_{111}
  1 1 2   -1.71624577e-48   # lambda'_{112}
  1 1 3    1.73542094e-45   # lambda'_{113}
  1 2 1   -7.83862141e-50   # lambda'_{121}
  1 2 2    6.51560079e-43   # lambda'_{122}
  1 2 3   -1.27763711e-44   # lambda'_{123}
  1 3 1    1.83781104e-48   # lambda'_{131}
  1 3 2   -2.96239750e-46   # lambda'_{132}
  1 3 3    2.84208418e-41   # lambda'_{133}
  2 1 1    4.19929372e-17   # lambda'_{211}
  2 1 2   -2.42186206e-21   # lambda'_{212}
  2 1 3    2.44892090e-18   # lambda'_{213}
  2 2 1   -1.10613877e-22   # lambda'_{221}
  2 2 2    9.19442122e-16   # lambda'_{222}
  2 2 3   -1.80292409e-17   # lambda'_{223}
  2 3 1    2.59340760e-21   # lambda'_{231}
  2 3 2   -4.18035589e-19   # lambda'_{232}
  2 3 3    4.01057707e-14   # lambda'_{233}
Block RVLAMUDD Q= 8.76213736e+02 # non-zero R-Parity violating UDD couplings 
Block RVTLLE Q= 8.76213736e+02 # non-zero R-Parity violating LLE soft terms 
  1 2 1   -1.20341704e-05   # T_{121}
  1 2 2   -2.53124789e-39   # T_{122}
  1 3 3   -1.88258414e-38   # T_{133}
  2 1 1    1.20341704e-05   # T_{211}
  2 1 2    2.53124789e-39   # T_{212}
  2 3 3   -2.65662368e-11   # T_{233}
  3 1 3    1.88258414e-38   # T_{313}
  3 2 3    2.65662368e-11   # T_{323}
Block RVTLQD Q= 8.76213736e+02 # non-zero R-Parity violating LQD soft terms 
  1 1 1   -5.92088853e-41   # T'_{111}
  1 1 2   -1.04504125e-44   # T'_{112}
  1 1 3    1.05995169e-41   # T'_{113}
  1 2 1   -4.77304441e-46   # T'_{121}
  1 2 2   -1.29628985e-39   # T'_{122}
  1 2 3   -7.80353840e-41   # T'_{123}
  1 3 1    1.12506732e-44   # T'_{131}
  1 3 2   -1.81351838e-42   # T'_{132}
  1 3 3   -5.39877932e-38   # T'_{133}
  2 1 1   -8.35524852e-14   # T'_{211}
  2 1 2   -1.47469611e-17   # T'_{212}
  2 1 3    1.49573680e-14   # T'_{213}
  2 2 1   -6.73541836e-19   # T'_{221}
  2 2 2   -1.82925650e-12   # T'_{222}
  2 2 3   -1.10118599e-13   # T'_{223}
  2 3 1    1.58762386e-17   # T'_{231}
  2 3 2   -2.55912245e-15   # T'_{232}
  2 3 3   -7.61847741e-11   # T'_{233}
Block RVTUDD Q= 8.76213736e+02 # non-zero R-Parity violating UDD soft terms 
Block RVKAPPA Q= 8.76213736e+02 # R-Parity violating kappa 
     1    1.34033125e-37   # kappa_{1}
     2    1.89139428e-10   # kappa_{2}
     3    0.00000000e+00   # kappa_{3}
Block RVD Q= 8.76213736e+02 # R-Parity violating D 
     1   -6.82798507e-35   # D_{1}
     2   -9.63546064e-08   # D_{2}
     3    0.00000000e+00   # D_{3}
Block RVSNVEV Q= 8.76213736e+02 # sneutrino VEVs D 
     1   -7.14727975e-31   # SneutrinoVev_{1}
     2   -1.97520053e-07   # SneutrinoVev_{2}
     3    0.00000000e+00   # SneutrinoVev_{3}
Block RVM2LH1 Q= 8.76213736e+02 # M2LH1 
     1    1.22486040e-34   # M2LH1_{1}
     2    1.72848394e-07   # M2LH1_{2}
     3    0.00000000e+00   # M2LH1_{3}
Block UPMNS Q= 9.11876000e+01 # neutrino mixing matrix (inverted  hierarchy)
  1  1     1.00000000e+00   # UPMNS_{11} matrix element
  1  2     1.14404263e-14   # UPMNS_{12} matrix element
  1  3     0.00000000e+00   # UPMNS_{13} matrix element
  2  1    -1.14404263e-14   # UPMNS_{21} matrix element
  2  2     1.00000000e+00   # UPMNS_{22} matrix element
  2  3     0.00000000e+00   # UPMNS_{23} matrix element
  3  1     0.00000000e+00   # UPMNS_{31} matrix element
  3  2     0.00000000e+00   # UPMNS_{32} matrix element
  3  3     1.00000000e+00   # UPMNS_{33} matrix element
Block msq2 Q= 8.76213736e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     1.03725326e+06    # (m^_Q^2)_{11}
  1  2     3.57031776e+01    # (m^_Q^2)_{12}
  1  3    -8.44018360e+02    # (m^_Q^2)_{13}
  2  1     3.57031776e+01    # (m^_Q^2)_{21}
  2  2     1.03699453e+06    # (m^_Q^2)_{22}
  2  3     6.21382861e+03    # (m^_Q^2)_{23}
  3  1    -8.44018360e+02    # (m^_Q^2)_{31}
  3  2     6.21382861e+03    # (m^_Q^2)_{32}
  3  3     8.82900368e+05    # (m^_Q^2)_{33}
Block msl2 Q= 8.76213736e+02 # super MNS slepton mass^2 matrix - DRbar
  1  1     1.24785482e+05    # (m^_L^2)_{11}
  1  2     1.64745481e-27    # (m^_L^2)_{12}
  1  3     0.00000000e+00    # (m^_L^2)_{13}
  2  1     1.64745481e-27    # (m^_L^2)_{21}
  2  2     1.24783158e+05    # (m^_L^2)_{22}
  2  3     0.00000000e+00    # (m^_L^2)_{23}
  3  1     0.00000000e+00    # (m^_L^2)_{31}
  3  2     0.00000000e+00    # (m^_L^2)_{32}
  3  3     1.24090340e+05    # (m^_L^2)_{33}
Block msd2 Q= 8.76213736e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     9.52925752e+05    # (m^_d^2)_{11}
  1  2    -2.55951327e-06    # (m^_d^2)_{12}
  1  3     2.65161522e-03    # (m^_d^2)_{13}
  2  1    -2.55951327e-06    # (m^_d^2)_{21}
  2  2     9.52920457e+05    # (m^_d^2)_{22}
  2  3    -4.27431531e-01    # (m^_d^2)_{23}
  3  1     2.65161522e-03    # (m^_d^2)_{31}
  3  2    -4.27431531e-01    # (m^_d^2)_{32}
  3  3     9.43293443e+05    # (m^_d^2)_{33}
Block msu2 Q= 8.76213736e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     9.61892856e+05    # (m^_u^2)_{11}
  1  2    -1.29262219e-08    # (m^_u^2)_{12}
  1  3    -1.17218942e-05    # (m^_u^2)_{13}
  2  1    -1.29262219e-08    # (m^_u^2)_{21}
  2  2     9.61887432e+05    # (m^_u^2)_{22}
  2  3    -5.70513865e-02    # (m^_u^2)_{23}
  3  1    -1.17218942e-05    # (m^_u^2)_{31}
  3  2    -5.70513865e-02    # (m^_u^2)_{32}
  3  3     6.55113358e+05    # (m^_u^2)_{33}
Block mse2 Q= 8.76213736e+02 # super MNS slepton mass^2 matrix - DRbar
  1  1     4.91947923e+04    # (m^_e^2)_{11}
  1  2     1.62614694e-29    # (m^_e^2)_{12}
  1  3     0.00000000e+00    # (m^_e^2)_{13}
  2  1     1.62614694e-29    # (m^_e^2)_{21}
  2  2     4.92029628e+04    # (m^_e^2)_{22}
  2  3     0.00000000e+00    # (m^_e^2)_{23}
  3  1     0.00000000e+00    # (m^_e^2)_{31}
  3  2     0.00000000e+00    # (m^_e^2)_{32}
  3  3     4.77770034e+04    # (m^_e^2)_{33}
Block tu Q= 8.76213736e+02   # super CKM trilinear matrix - DRbar
  1  1    -8.38413722e-03    # (T^_u)_{11}
  1  2    -1.80783693e-08    # (T^_u)_{12}
  1  3    -8.04529386e-08    # (T^_u)_{13}
  2  1    -8.28122695e-06    # (T^_u)_{21}
  2  2    -3.84057976e+00    # (T^_u)_{22}
  2  3    -3.91220638e-04    # (T^_u)_{23}
  3  1    -1.11190945e-02    # (T^_u)_{31}
  3  2    -1.18013324e-01    # (T^_u)_{32}
  3  3    -7.60417010e+02    # (T^_u)_{33}
Block td Q= 8.76213736e+02   # super CKM trilinear matrix - DRbar
  1  1    -1.97013107e-01    # (T^_d)_{11}
  1  2    -2.91243663e-06    # (T^_d)_{12}
  1  3     6.92176731e-05    # (T^_d)_{13}
  2  1    -6.37680099e-05    # (T^_d)_{21}
  2  2    -4.31318089e+00    # (T^_d)_{22}
  2  3    -1.11576188e-02    # (T^_d)_{23}
  3  1     6.59786938e-02    # (T^_d)_{31}
  3  2    -4.85748942e-01    # (T^_d)_{32}
  3  3    -1.76002138e+02    # (T^_d)_{33}
Block te Q= 8.76213736e+02   # super CKM trilinear matrix - DRbar
  1  1    -8.30075527e-03    # (T^_e)_{11}
  1  2    -1.15884030e-34    # (T^_e)_{12}
  1  3     0.00000000e+00    # (T^_e)_{13}
  2  1     1.21622965e-27    # (T^_e)_{21}
  2  2    -1.71626962e+00    # (T^_e)_{22}
  2  3     0.00000000e+00    # (T^_e)_{23}
  3  1     0.00000000e+00    # (T^_e)_{31}
  3  2     0.00000000e+00    # (T^_e)_{32}
  3  3    -2.96761645e+01    # (T^_e)_{33}
Block VCKM Q= 8.76213736e+02 # DRbar CKM mixing matrix
  1  1     9.73840718e-01    # CKM_{11} matrix element
  1  2     2.27197409e-01    # CKM_{12} matrix element
  1  3     3.94887480e-03    # CKM_{13} matrix element
  2  1    -2.27161573e-01    # CKM_{21} matrix element
  2  2     9.72961270e-01    # CKM_{22} matrix element
  2  3     4.17610673e-02    # CKM_{23} matrix element
  3  1     5.64590404e-03    # CKM_{31} matrix element
  3  2    -4.15656603e-02    # CKM_{32} matrix element
  3  3     9.99119822e-01    # CKM_{33} matrix element
Block msoft Q= 8.76213736e+02 # MSSM DRbar SUSY breaking parameters
     1     2.10407598e+02     # M_1(Q)
     2     3.89203113e+02     # M_2(Q)
     3     1.11363928e+03     # M_3(Q)
    21     1.08622200e+05     # mH1^2(Q)
    22    -3.80266659e+05     # mH2^2(Q)
Block USQMIX  # super CKM squark mass^2 matrix
  1  1     2.22396189e-05   # (USQMIX)_{11}
  1  2     2.35497488e-04   # (USQMIX)_{12}
  1  3     4.29688170e-01   # (USQMIX)_{13}
  1  4     1.33119995e-10   # (USQMIX)_{14}
  1  5     6.46363795e-07   # (USQMIX)_{15}
  1  6     9.02977309e-01   # (USQMIX)_{16}
  2  1     1.63628297e-04   # (USQMIX)_{21}
  2  2     1.73193948e-03   # (USQMIX)_{22}
  2  3     9.02975790e-01   # (USQMIX)_{23}
  2  4     1.03878231e-08   # (USQMIX)_{24}
  2  5     5.03791098e-05   # (USQMIX)_{25}
  2  6    -4.29687903e-01   # (USQMIX)_{26}
  3  1     1.60899364e-07   # (USQMIX)_{31}
  3  2     8.86186535e-03   # (USQMIX)_{32}
  3  3    -6.05230743e-05   # (USQMIX)_{33}
  3  4     2.48090528e-08   # (USQMIX)_{34}
  3  5     9.99960731e-01   # (USQMIX)_{35}
  3  6     2.57733609e-05   # (USQMIX)_{36}
  4  1     1.93464335e-05   # (USQMIX)_{41}
  4  2     1.31432362e-10   # (USQMIX)_{42}
  4  3    -1.24796339e-08   # (USQMIX)_{43}
  4  4     1.00000000e+00   # (USQMIX)_{44}
  4  5    -2.48151971e-08   # (USQMIX)_{45}
  4  6     5.31459515e-09   # (USQMIX)_{46}
  5  1     1.87875984e-01   # (USQMIX)_{51}
  5  2     9.82152635e-01   # (USQMIX)_{52}
  5  3    -1.66453368e-03   # (USQMIX)_{53}
  5  4    -3.63509891e-06   # (USQMIX)_{54}
  5  5    -8.70419088e-03   # (USQMIX)_{55}
  5  6     5.31312675e-04   # (USQMIX)_{56}
  6  1     9.82192744e-01   # (USQMIX)_{61}
  6  2    -1.87868607e-01   # (USQMIX)_{62}
  6  3     1.58235155e-04   # (USQMIX)_{63}
  6  4    -1.90018584e-05   # (USQMIX)_{64}
  6  5     1.66478452e-03   # (USQMIX)_{65}
  6  6    -5.04928055e-05   # (USQMIX)_{66}
Block DSQMIX  # super CKM squark mass^2 matrix
  1  1     4.59227583e-03   # (DSQMIX)_{11}
  1  2    -3.38097509e-02   # (DSQMIX)_{12}
  1  3     9.74057641e-01   # (DSQMIX)_{13}
  1  4     9.71568071e-07   # (DSQMIX)_{14}
  1  5    -1.56625492e-04   # (DSQMIX)_{15}
  1  6     2.23712985e-01   # (DSQMIX)_{16}
  2  1    -1.78772863e-03   # (DSQMIX)_{21}
  2  2     1.31632373e-02   # (DSQMIX)_{22}
  2  3    -2.23381460e-01   # (DSQMIX)_{23}
  2  4    -2.43265464e-06   # (DSQMIX)_{24}
  2  5     3.92324006e-04   # (DSQMIX)_{25}
  2  6     9.74640499e-01   # (DSQMIX)_{26}
  3  1     1.97143892e-06   # (DSQMIX)_{31}
  3  2     4.52100757e-03   # (DSQMIX)_{32}
  3  3     4.02970897e-04   # (DSQMIX)_{33}
  3  4     5.56448359e-06   # (DSQMIX)_{34}
  3  5     9.99989630e-01   # (DSQMIX)_{35}
  3  6    -3.71225358e-04   # (DSQMIX)_{36}
  4  1     2.07151409e-04   # (DSQMIX)_{41}
  4  2     6.48164385e-08   # (DSQMIX)_{42}
  4  3    -2.50185442e-06   # (DSQMIX)_{43}
  4  4     9.99999979e-01   # (DSQMIX)_{44}
  4  5    -5.56337916e-06   # (DSQMIX)_{45}
  4  6     2.30387169e-06   # (DSQMIX)_{46}
  5  1    -1.38067399e-01   # (DSQMIX)_{51}
  5  2     9.89735676e-01   # (DSQMIX)_{52}
  5  3     3.62250769e-02   # (DSQMIX)_{53}
  5  4     2.86145982e-05   # (DSQMIX)_{54}
  5  5    -4.49094811e-03   # (DSQMIX)_{55}
  5  6    -5.31599093e-03   # (DSQMIX)_{56}
  6  1     9.90410554e-01   # (DSQMIX)_{61}
  6  2     1.38153837e-01   # (DSQMIX)_{62}
  6  3     1.30264257e-04   # (DSQMIX)_{63}
  6  4    -2.05177017e-04   # (DSQMIX)_{64}
  6  5    -6.26612017e-04   # (DSQMIX)_{65}
  6  6    -1.91070245e-05   # (DSQMIX)_{66}
Block RVLMIX  # charged higgs-slepton mixing matrix 
  1 1    0.00000000e+00   # C_{11}
  1 2    0.00000000e+00   # C_{12}
  1 3    0.00000000e+00   # C_{13}
  1 4    0.00000000e+00   # C_{14}
  1 5    1.45642822e-01   # C_{15}
  1 6    0.00000000e+00   # C_{16}
  1 7    0.00000000e+00   # C_{17}
  1 8    9.89337237e-01   # C_{18}
  2 1   -1.44508121e-38   # C_{21}
  2 2    2.07845980e-37   # C_{22}
  2 3    4.22700132e-05   # C_{23}
  2 4   -1.61424475e-31   # C_{24}
  2 5    0.00000000e+00   # C_{25}
  2 6    9.99999999e-01   # C_{26}
  2 7   -1.50416261e-29   # C_{27}
  2 8    0.00000000e+00   # C_{28}
  3 1   -8.26535810e-13   # C_{31}
  3 2    1.18881425e-11   # C_{32}
  3 3    6.35860687e-34   # C_{33}
  3 4    8.74029171e-03   # C_{34}
  3 5    0.00000000e+00   # C_{35}
  3 6    1.50424624e-29   # C_{36}
  3 7    9.99961803e-01   # C_{37}
  3 8    0.00000000e+00   # C_{38}
  4 1    8.60391205e-36   # C_{41}
  4 2    4.06369450e-36   # C_{42}
  4 3    9.99999999e-01   # C_{43}
  4 4    1.65684350e-32   # C_{44}
  4 5    0.00000000e+00   # C_{45}
  4 6   -4.22700132e-05   # C_{46}
  4 7   -1.44834088e-34   # C_{47}
  4 8    0.00000000e+00   # C_{48}
  5 1    2.37754137e-12   # C_{51}
  5 2    1.08395455e-12   # C_{52}
  5 3   -1.65678020e-32   # C_{53}
  5 4    9.99961803e-01   # C_{54}
  5 5    0.00000000e+00   # C_{55}
  5 6    2.99508098e-32   # C_{56}
  5 7   -8.74029171e-03   # C_{57}
  5 8    0.00000000e+00   # C_{58}
  6 1    0.00000000e+00   # C_{61}
  6 2    0.00000000e+00   # C_{62}
  6 3    0.00000000e+00   # C_{63}
  6 4    0.00000000e+00   # C_{64}
  6 5    9.89337237e-01   # C_{65}
  6 6    0.00000000e+00   # C_{66}
  6 7    0.00000000e+00   # C_{67}
  6 8   -1.45642822e-01   # C_{68}
  7 1    9.94700954e-01   # C_{71}
  7 2    1.02810561e-01   # C_{72}
  7 3   -8.97611048e-36   # C_{73}
  7 4   -2.47978679e-12   # C_{74}
  7 5    0.00000000e+00   # C_{75}
  7 6   -6.62119727e-39   # C_{76}
  7 7   -3.78411036e-13   # C_{77}
  7 8    0.00000000e+00   # C_{78}
Block RVHMIX  # CP-even neutral scalar mixing matrix 
  1 1    1.05903111e-01   # curlyN_{11}
  1 2    9.94376453e-01   # curlyN_{12}
  1 3   -2.05775582e-34   # curlyN_{13}
  1 4   -5.79909453e-11   # curlyN_{14}
  1 5    0.00000000e+00   # curlyN_{15}
  2 1    0.00000000e+00   # curlyN_{21}
  2 2    0.00000000e+00   # curlyN_{22}
  2 3    0.00000000e+00   # curlyN_{23}
  2 4    0.00000000e+00   # curlyN_{24}
  2 5    1.00000000e+00   # curlyN_{25}
  3 1    8.76052300e-12   # curlyN_{31}
  3 2    5.73858909e-11   # curlyN_{32}
  3 3   -1.65807772e-32   # curlyN_{33}
  3 4    1.00000000e+00   # curlyN_{34}
  3 5    0.00000000e+00   # curlyN_{35}
  4 1    3.37321436e-35   # curlyN_{41}
  4 2    2.03346774e-34   # curlyN_{42}
  4 3    1.00000000e+00   # curlyN_{43}
  4 4    1.65807772e-32   # curlyN_{44}
  4 5    0.00000000e+00   # curlyN_{45}
  5 1    9.94376453e-01   # curlyN_{51}
  5 2   -1.05903111e-01   # curlyN_{52}
  5 3   -1.20073932e-35   # curlyN_{53}
  5 4   -2.63391339e-12   # curlyN_{54}
  5 5    0.00000000e+00   # curlyN_{55}
Block RVAMIX  # CP-odd neutral scalar mixing matrix 
  1 1    0.00000000e+00   # curlyN~_{11}
  1 2    0.00000000e+00   # curlyN~_{12}
  1 3    0.00000000e+00   # curlyN~_{13}
  1 4    0.00000000e+00   # curlyN~_{14}
  1 5    1.00000000e+00   # curlyN~_{15}
  2 1   -6.56283190e-12   # curlyN~_{21}
  2 2    5.68210195e-11   # curlyN~_{22}
  2 3   -1.65807772e-32   # curlyN~_{23}
  2 4    1.00000000e+00   # curlyN~_{24}
  2 5    0.00000000e+00   # curlyN~_{25}
  3 1   -2.16942412e-35   # curlyN~_{31}
  3 2    2.09882019e-34   # curlyN~_{32}
  3 3    1.00000000e+00   # curlyN~_{33}
  3 4    1.65807772e-32   # curlyN~_{34}
  3 5    0.00000000e+00   # curlyN~_{35}
  4 1    9.94700737e-01   # curlyN~_{41}
  4 2    1.02812660e-01   # curlyN~_{42}
  4 3    7.49176089e-40   # curlyN~_{43}
  4 4    6.86133601e-13   # curlyN~_{44}
  4 5    0.00000000e+00   # curlyN~_{45}