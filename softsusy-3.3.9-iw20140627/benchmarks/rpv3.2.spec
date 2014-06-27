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
     1    1.37500000e+02   # m0
     2    5.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.52879690e+16   # MX scale
Block RVLAMUDDIN          # input LQD couplings at MSUSY
  1 2 3   1.00000000e-04   # lambda''_{123}
  1 3 2  -1.00000000e-04   # lambda''_{132}
# SOFTSUSY-specific non SLHA information:
# MIXING=1 Desired accuracy=1.00000000e-03 Achieved accuracy=2.73916159e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.05094246e+01   # MW
        25     1.15397727e+02   # CP even neutral scalar
        35     3.86474873e+02   # CP even neutral scalar
        36     3.86474873e+02   # CP odd neutral scalar
        37     2.44656370e+02   # charged scalar
   1000021     1.25249571e+03   # ~g
   1000022     2.27135125e+02   # ~neutralino(1)
   1000023     4.28319255e+02   # ~neutralino(2)
   1000024     4.28364437e+02   # ~chargino(1)
   1000025    -6.97935456e+02   # ~neutralino(3)
   1000035     7.10632421e+02   # ~neutralino(4)
   1000037     7.10917472e+02   # ~chargino(2)
   1000011     2.51771131e+02   # charged scalar
   1000013     2.51793397e+02   # charged scalar
   1000015     3.95689622e+02   # charged scalar
   2000011     3.95725823e+02   # charged scalar
   2000013     3.95729369e+02   # charged scalar
   2000015     7.85515239e+02   # charged scalar
   1000012     3.87569152e+02   # CP even neutral scalar
   1000014     3.87572783e+02   # CP even neutral scalar
   1000016     7.81158395e+02   # CP even neutral scalar
   1000017     3.87569152e+02   # CP odd neutral scalar
   1000018     3.87572783e+02   # CP odd neutral scalar
   1000019     7.81158395e+02   # CP odd neutral scalar
   1000001     1.05575317e+03   # ~d_1
   1000003     1.09482127e+03   # ~d_2
   1000005     1.10302438e+03   # ~d_3
   2000001     1.10302812e+03   # ~d_4
   2000003     1.15179297e+03   # ~d_5
   2000005     1.15181360e+03   # ~d_6
   1000002     8.84190965e+02   # ~u_1
   1000004     1.08710553e+03   # ~u_2
   1000006     1.10687835e+03   # ~u_3
   2000002     1.10688394e+03   # ~u_4
   2000004     1.14921847e+03   # ~u_5
   2000006     1.14922286e+03   # ~u_6
        12     0.00000000e+00   # Mnu1 inverted hierarchy output
        14     0.00000000e+00   # Mnu2 inverted hierarchy output
        16     0.00000000e+00   # Mnu3 inverted hierarchy output
Block RVNMIX  # neutrino-neutralino mixing matrix 
  1 1    0.00000000e+00   # N_{11}
  1 2    0.00000000e+00   # N_{12}
  1 3    0.00000000e+00   # N_{13}
  1 4    0.00000000e+00   # N_{14}
  1 5    0.00000000e+00   # N_{15}
  1 6    0.00000000e+00   # N_{16}
  1 7    0.00000000e+00   # N_{17}
  2 1    0.00000000e+00   # N_{21}
  2 2    0.00000000e+00   # N_{22}
  2 3    0.00000000e+00   # N_{23}
  2 4    0.00000000e+00   # N_{24}
  2 5    0.00000000e+00   # N_{25}
  2 6    0.00000000e+00   # N_{26}
  2 7    0.00000000e+00   # N_{27}
  3 1    0.00000000e+00   # N_{31}
  3 2    0.00000000e+00   # N_{32}
  3 3    0.00000000e+00   # N_{33}
  3 4    0.00000000e+00   # N_{34}
  3 5    0.00000000e+00   # N_{35}
  3 6    0.00000000e+00   # N_{36}
  3 7    0.00000000e+00   # N_{37}
  4 1    0.00000000e+00   # N_{41}
  4 2    0.00000000e+00   # N_{42}
  4 3    0.00000000e+00   # N_{43}
  4 4    0.00000000e+00   # N_{44}
  4 5    0.00000000e+00   # N_{45}
  4 6    0.00000000e+00   # N_{46}
  4 7    0.00000000e+00   # N_{47}
  5 1    0.00000000e+00   # N_{51}
  5 2    0.00000000e+00   # N_{52}
  5 3    0.00000000e+00   # N_{53}
  5 4    0.00000000e+00   # N_{54}
  5 5    0.00000000e+00   # N_{55}
  5 6    0.00000000e+00   # N_{56}
  5 7    0.00000000e+00   # N_{57}
  6 1    0.00000000e+00   # N_{61}
  6 2    0.00000000e+00   # N_{62}
  6 3    0.00000000e+00   # N_{63}
  6 4    0.00000000e+00   # N_{64}
  6 5    0.00000000e+00   # N_{65}
  6 6    0.00000000e+00   # N_{66}
  6 7    0.00000000e+00   # N_{67}
  7 1    0.00000000e+00   # N_{71}
  7 2    0.00000000e+00   # N_{72}
  7 3    0.00000000e+00   # N_{73}
  7 4    0.00000000e+00   # N_{74}
  7 5    0.00000000e+00   # N_{75}
  7 6    0.00000000e+00   # N_{76}
  7 7    0.00000000e+00   # N_{77}
Block RVUMIX  # lepton-chargino mixing matrix U
  1 1    1.00000000e+00   # U_{11}
  1 2    0.00000000e+00   # U_{12}
  1 3    0.00000000e+00   # U_{13}
  1 4    0.00000000e+00   # U_{14}
  1 5    0.00000000e+00   # U_{15}
  2 1    0.00000000e+00   # U_{21}
  2 2    1.00000000e+00   # U_{22}
  2 3    0.00000000e+00   # U_{23}
  2 4    0.00000000e+00   # U_{24}
  2 5    0.00000000e+00   # U_{25}
  3 1    0.00000000e+00   # U_{31}
  3 2    0.00000000e+00   # U_{32}
  3 3    1.00000000e+00   # U_{33}
  3 4    0.00000000e+00   # U_{34}
  3 5    0.00000000e+00   # U_{35}
  4 1    0.00000000e+00   # U_{41}
  4 2    0.00000000e+00   # U_{42}
  4 3    0.00000000e+00   # U_{43}
  4 4   -9.64732233e-01   # U_{44}
  4 5    2.63233201e-01   # U_{45}
  5 1    0.00000000e+00   # U_{51}
  5 2    0.00000000e+00   # U_{52}
  5 3    0.00000000e+00   # U_{53}
  5 4   -2.63233201e-01   # U_{54}
  5 5   -9.64732233e-01   # U_{55}
Block RVVMIX  # lepton-chargino mixing matrix V
  1 1    1.00000000e+00   # V_{11}
  1 2    0.00000000e+00   # V_{12}
  1 3    0.00000000e+00   # V_{13}
  1 4    0.00000000e+00   # V_{14}
  1 5    0.00000000e+00   # V_{15}
  2 1    0.00000000e+00   # V_{21}
  2 2    1.00000000e+00   # V_{22}
  2 3    0.00000000e+00   # V_{23}
  2 4    0.00000000e+00   # V_{24}
  2 5    0.00000000e+00   # V_{25}
  3 1    0.00000000e+00   # V_{31}
  3 2    0.00000000e+00   # V_{32}
  3 3    1.00000000e+00   # V_{33}
  3 4    0.00000000e+00   # V_{34}
  3 5    0.00000000e+00   # V_{35}
  4 1    0.00000000e+00   # V_{41}
  4 2    0.00000000e+00   # V_{42}
  4 3    0.00000000e+00   # V_{43}
  4 4   -9.84752396e-01   # V_{44}
  4 5    1.73961832e-01   # V_{45}
  5 1    0.00000000e+00   # V_{51}
  5 2    0.00000000e+00   # V_{52}
  5 3    0.00000000e+00   # V_{53}
  5 4   -1.73961832e-01   # V_{54}
  5 5   -9.84752396e-01   # V_{55}
Block gauge Q= 9.55780048e+02  # SM gauge couplings
     1     3.62891621e-01   # g'(Q)MSSM DRbar
     2     6.41875132e-01   # g(Q)MSSM DRbar
     3     1.05977261e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.55780048e+02   # diagonal Up Yukawa matrix
  1  1     7.31062073e-06    # YU_{11}(Q)MSSM DRbar
  2  2     3.34879838e-03    # YU_{22}(Q)MSSM DRbar
  3  3     8.54640020e-01    # YU_{33}(Q)MSSM DRbar
Block yd Q= 9.55780048e+02   # diagonal down Yukawa matrix
  1  1     1.40687409e-04    # YD_{11}(Q)MSSM DRbar
  2  2     3.08037441e-03    # YD_{22}(Q)MSSM DRbar
  3  3     1.34276862e-01    # YD_{33}(Q)MSSM DRbar
Block ye Q= 9.55780048e+02   # diagonal lepton Yukawa matrix
  1  1     2.78733251e-05    # YE_{11}(Q)MSSM DRbar
  2  2     5.76332788e-03    # YE_{22}(Q)MSSM DRbar
  3  3     1.00247608e-01    # YE_{33}(Q)MSSM DRbar
Block hmix Q= 9.55780048e+02 # Higgs mixing parameters
     1     6.92550338e+02    # mu(Q)MSSM DRbar
     2     9.66513558e+00    # tan beta(Q)MSSM DRbar
     3     2.44434433e+02    # higgs vev(Q)MSSM DRbar
     4     6.32788282e+05    # mA^2(Q)MSSM DRbar
Block RVLAMLLE Q= 9.55780048e+02 # non-zero R-Parity violating LLE couplings 
Block RVLAMLQD Q= 9.55780048e+02 # non-zero R-Parity violating LQD couplings 
Block RVLAMUDD Q= 9.55780048e+02 # non-zero R-Parity violating UDD couplings 
  1 1 2   -6.04140124e-21   # lambda''_{112}
  1 1 3   -5.97871210e-24   # lambda''_{113}
  1 2 1    6.04140124e-21   # lambda''_{121}
  1 2 3    9.99999857e-05   # lambda''_{123}
  1 3 1    5.97871210e-24   # lambda''_{131}
  1 3 2   -9.99999857e-05   # lambda''_{132}
  2 1 2   -9.92697152e-27   # lambda''_{212}
  2 1 3   -9.66907315e-30   # lambda''_{213}
  2 2 1    9.92697152e-27   # lambda''_{221}
  2 2 3   -5.51435794e-16   # lambda''_{223}
  2 3 1    9.66907315e-30   # lambda''_{231}
  2 3 2    5.51435794e-16   # lambda''_{232}
  3 1 2    2.30361725e-25   # lambda''_{312}
  3 1 3    2.24367685e-28   # lambda''_{313}
  3 2 1   -2.30361725e-25   # lambda''_{321}
  3 2 3    1.29252684e-14   # lambda''_{323}
  3 3 1   -2.24367685e-28   # lambda''_{331}
  3 3 2   -1.29252684e-14   # lambda''_{332}
Block RVTLLE Q= 9.55780048e+02 # non-zero R-Parity violating LLE soft terms 
Block RVTLQD Q= 9.55780048e+02 # non-zero R-Parity violating LQD soft terms 
Block RVTUDD Q= 9.55780048e+02 # non-zero R-Parity violating UDD soft terms 
  1 1 2   -4.08210589e-17   # T''_{112}
  1 1 3   -4.01102992e-20   # T''_{113}
  1 2 1    4.08210589e-17   # T''_{121}
  1 2 3    3.42507579e-08   # T''_{123}
  1 3 1    4.01102992e-20   # T''_{131}
  1 3 2   -3.42507579e-08   # T''_{132}
  2 1 2    1.33212011e-22   # T''_{212}
  2 1 3    1.29655501e-25   # T''_{213}
  2 2 1   -1.33212011e-22   # T''_{221}
  2 2 3    1.07826412e-12   # T''_{223}
  2 3 1   -1.29655501e-25   # T''_{231}
  2 3 2   -1.07826412e-12   # T''_{232}
  3 1 2   -3.08270769e-21   # T''_{312}
  3 1 3   -3.00015922e-24   # T''_{313}
  3 2 1    3.08270769e-21   # T''_{321}
  3 2 3   -2.51753155e-11   # T''_{323}
  3 3 1    3.00015922e-24   # T''_{331}
  3 3 2    2.51753155e-11   # T''_{332}
Block RVKAPPA Q= 9.55780048e+02 # R-Parity violating kappa 
     1    0.00000000e+00   # kappa_{1}
     2    0.00000000e+00   # kappa_{2}
     3    0.00000000e+00   # kappa_{3}
Block RVD Q= 9.55780048e+02 # R-Parity violating D 
     1    0.00000000e+00   # D_{1}
     2    0.00000000e+00   # D_{2}
     3    0.00000000e+00   # D_{3}
Block RVSNVEV Q= 9.55780048e+02 # sneutrino VEVs D 
     1    0.00000000e+00   # SneutrinoVev_{1}
     2    0.00000000e+00   # SneutrinoVev_{2}
     3    0.00000000e+00   # SneutrinoVev_{3}
Block RVM2LH1 Q= 9.55780048e+02 # M2LH1 
     1    0.00000000e+00   # M2LH1_{1}
     2    0.00000000e+00   # M2LH1_{2}
     3    0.00000000e+00   # M2LH1_{3}
Block UPMNS Q= 9.11876000e+01 # neutrino mixing matrix (inverted  hierarchy)
  1  1     0.00000000e+00   # UPMNS_{11} matrix element
  1  2     0.00000000e+00   # UPMNS_{12} matrix element
  1  3     0.00000000e+00   # UPMNS_{13} matrix element
  2  1     0.00000000e+00   # UPMNS_{21} matrix element
  2  2     0.00000000e+00   # UPMNS_{22} matrix element
  2  3     0.00000000e+00   # UPMNS_{23} matrix element
  3  1     0.00000000e+00   # UPMNS_{31} matrix element
  3  2     0.00000000e+00   # UPMNS_{32} matrix element
  3  3     0.00000000e+00   # UPMNS_{33} matrix element
Block msq2 Q= 9.55780048e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     1.23574819e+06    # (m^_Q^2)_{11}
  1  2     4.23671374e+01    # (m^_Q^2)_{12}
  1  3    -1.00189543e+03    # (m^_Q^2)_{13}
  2  1     4.23671374e+01    # (m^_Q^2)_{21}
  2  2     1.23544117e+06    # (m^_Q^2)_{22}
  2  3     7.37615203e+03    # (m^_Q^2)_{23}
  3  1    -1.00189543e+03    # (m^_Q^2)_{31}
  3  2     7.37615203e+03    # (m^_Q^2)_{32}
  3  3     1.05248694e+06    # (m^_Q^2)_{33}
Block msl2 Q= 9.55780048e+02 # super MNS slepton mass^2 matrix - DRbar
  1  1     1.50467154e+05    # (m^_L^2)_{11}
  1  2     0.00000000e+00    # (m^_L^2)_{12}
  1  3     0.00000000e+00    # (m^_L^2)_{13}
  2  1     0.00000000e+00    # (m^_L^2)_{21}
  2  2     1.50464368e+05    # (m^_L^2)_{22}
  2  3     0.00000000e+00    # (m^_L^2)_{23}
  3  1     0.00000000e+00    # (m^_L^2)_{31}
  3  2     0.00000000e+00    # (m^_L^2)_{32}
  3  3     1.49625487e+05    # (m^_L^2)_{33}
Block msd2 Q= 9.55780048e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     1.13396923e+06    # (m^_d^2)_{11}
  1  2    -3.00150636e-06    # (m^_d^2)_{12}
  1  3     3.10663131e-03    # (m^_d^2)_{13}
  2  1    -3.00150636e-06    # (m^_d^2)_{21}
  2  2     1.13396296e+06    # (m^_d^2)_{22}
  2  3    -5.00778854e-01    # (m^_d^2)_{23}
  3  1     3.10663131e-03    # (m^_d^2)_{31}
  3  2    -5.00778854e-01    # (m^_d^2)_{32}
  3  3     1.12258142e+06    # (m^_d^2)_{33}
Block msu2 Q= 9.55780048e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     1.14483491e+06    # (m^_u^2)_{11}
  1  2     1.55827756e-03    # (m^_u^2)_{12}
  1  3    -5.27720567e-05    # (m^_u^2)_{13}
  2  1     1.55827756e-03    # (m^_u^2)_{21}
  2  2     1.14482848e+06    # (m^_u^2)_{22}
  2  3    -6.63798796e-02    # (m^_u^2)_{23}
  3  1    -5.27720567e-05    # (m^_u^2)_{31}
  3  2    -6.63798796e-02    # (m^_u^2)_{32}
  3  3     7.80568350e+05    # (m^_u^2)_{33}
Block mse2 Q= 9.55780048e+02 # super MNS slepton mass^2 matrix - DRbar
  1  1     5.94825289e+04    # (m^_e^2)_{11}
  1  2     0.00000000e+00    # (m^_e^2)_{12}
  1  3     0.00000000e+00    # (m^_e^2)_{13}
  2  1     0.00000000e+00    # (m^_e^2)_{21}
  2  2     5.94768488e+04    # (m^_e^2)_{22}
  2  3     0.00000000e+00    # (m^_e^2)_{23}
  3  1     0.00000000e+00    # (m^_e^2)_{31}
  3  2     0.00000000e+00    # (m^_e^2)_{32}
  3  3     5.77661894e+04    # (m^_e^2)_{33}
Block tu Q= 9.55780048e+02   # super CKM trilinear matrix - DRbar
  1  1    -9.10504592e-03    # (T^_u)_{11}
  1  2    -1.77708652e-08    # (T^_u)_{12}
  1  3    -9.65860584e-08    # (T^_u)_{13}
  2  1    -8.87982750e-06    # (T^_u)_{21}
  2  2    -4.17081097e+00    # (T^_u)_{22}
  2  3    -4.19327252e-04    # (T^_u)_{23}
  3  1    -1.18996000e-02    # (T^_u)_{31}
  3  2    -1.26297991e-01    # (T^_u)_{32}
  3  3    -8.26465663e+02    # (T^_u)_{33}
Block td Q= 9.55780048e+02   # super CKM trilinear matrix - DRbar
  1  1    -2.13478038e-01    # (T^_d)_{11}
  1  2    -3.13923257e-06    # (T^_d)_{12}
  1  3     7.46299541e-05    # (T^_d)_{13}
  2  1    -6.87337686e-05    # (T^_d)_{21}
  2  2    -4.67365069e+00    # (T^_d)_{22}
  2  3    -1.20300675e-02    # (T^_d)_{23}
  3  1     7.10930974e-02    # (T^_d)_{31}
  3  2    -5.23402346e-01    # (T^_d)_{32}
  3  3    -1.90646256e+02    # (T^_d)_{33}
Block te Q= 9.55780048e+02   # super CKM trilinear matrix - DRbar
  1  1    -9.07898531e-03    # (T^_e)_{11}
  1  2     0.00000000e+00    # (T^_e)_{12}
  1  3     0.00000000e+00    # (T^_e)_{13}
  2  1     0.00000000e+00    # (T^_e)_{21}
  2  2    -1.87721547e+00    # (T^_e)_{22}
  2  3     0.00000000e+00    # (T^_e)_{23}
  3  1     0.00000000e+00    # (T^_e)_{31}
  3  2     0.00000000e+00    # (T^_e)_{32}
  3  3    -3.24769980e+01    # (T^_e)_{33}
Block VCKM Q= 9.55780048e+02 # DRbar CKM mixing matrix
  1  1     9.73840729e-01    # CKM_{11} matrix element
  1  2     2.27197384e-01    # CKM_{12} matrix element
  1  3     3.94746568e-03    # CKM_{13} matrix element
  2  1    -2.27161573e-01    # CKM_{21} matrix element
  2  2     9.72961909e-01    # CKM_{22} matrix element
  2  3     4.17461893e-02    # CKM_{23} matrix element
  3  1     5.64389127e-03    # CKM_{31} matrix element
  3  2    -4.15508520e-02    # CKM_{32} matrix element
  3  3     9.99120450e-01    # CKM_{33} matrix element
Block msoft Q= 9.55780048e+02 # MSSM DRbar SUSY breaking parameters
     1     2.32441172e+02     # M_1(Q)
     2     4.28956969e+02     # M_2(Q)
     3     1.21682755e+03     # M_3(Q)
    21     1.31346850e+05     # mH1^2(Q)
    22    -4.48802141e+05     # mH2^2(Q)
Block USQMIX  # super CKM squark mass^2 matrix
  1  1     2.10610576e-05   # (USQMIX)_{11}
  1  2     2.23014703e-04   # (USQMIX)_{12}
  1  3     4.08097280e-01   # (USQMIX)_{13}
  1  4     2.02569785e-10   # (USQMIX)_{14}
  1  5     5.84441441e-07   # (USQMIX)_{15}
  1  6     9.12938421e-01   # (USQMIX)_{16}
  2  1     1.46707181e-04   # (USQMIX)_{21}
  2  2     1.55272130e-03   # (USQMIX)_{22}
  2  3     9.12937190e-01   # (USQMIX)_{23}
  2  4     5.44892081e-09   # (USQMIX)_{24}
  2  5     2.80307447e-05   # (USQMIX)_{25}
  2  6    -4.08097112e-01   # (USQMIX)_{26}
  3  1     1.42329223e-07   # (USQMIX)_{31}
  3  2     7.93868398e-03   # (USQMIX)_{32}
  3  3    -3.78040115e-05   # (USQMIX)_{33}
  3  4    -1.26050943e-04   # (USQMIX)_{34}
  3  5     9.99968479e-01   # (USQMIX)_{35}
  3  6     1.43195255e-05   # (USQMIX)_{36}
  4  1     1.73305878e-05   # (USQMIX)_{41}
  4  2     1.00112138e-06   # (USQMIX)_{42}
  4  3    -1.22932246e-08   # (USQMIX)_{43}
  4  4     9.99999992e-01   # (USQMIX)_{44}
  4  5     1.26046964e-04   # (USQMIX)_{45}
  4  6     4.54831266e-09   # (USQMIX)_{46}
  5  1     1.62526441e-01   # (USQMIX)_{51}
  5  2     9.86671843e-01   # (USQMIX)_{52}
  5  3    -1.51140877e-03   # (USQMIX)_{53}
  5  4    -2.81712531e-06   # (USQMIX)_{54}
  5  5    -7.83320966e-03   # (USQMIX)_{55}
  5  6     4.30851709e-04   # (USQMIX)_{56}
  6  1     9.86704177e-01   # (USQMIX)_{61}
  6  2    -1.62521352e-01   # (USQMIX)_{62}
  6  3     1.04503959e-04   # (USQMIX)_{63}
  6  4    -1.71000728e-05   # (USQMIX)_{64}
  6  5     1.29010810e-03   # (USQMIX)_{65}
  6  6    -2.97773837e-05   # (USQMIX)_{66}
Block DSQMIX  # super CKM squark mass^2 matrix
  1  1     4.62262476e-03   # (DSQMIX)_{11}
  1  2    -3.40331461e-02   # (DSQMIX)_{12}
  1  3     9.77216983e-01   # (DSQMIX)_{13}
  1  4     9.11630740e-07   # (DSQMIX)_{14}
  1  5    -1.46963113e-04   # (DSQMIX)_{15}
  1  6     2.09445273e-01   # (DSQMIX)_{16}
  2  1    -1.65024033e-03   # (DSQMIX)_{21}
  2  2     1.21506387e-02   # (DSQMIX)_{22}
  2  3    -2.09141041e-01   # (DSQMIX)_{23}
  2  4    -2.03294832e-06   # (DSQMIX)_{24}
  2  5     3.27852201e-04   # (DSQMIX)_{25}
  2  6     9.77808548e-01   # (DSQMIX)_{26}
  3  1     1.71177808e-06   # (DSQMIX)_{31}
  3  2     4.07706623e-03   # (DSQMIX)_{32}
  3  3     3.58649267e-04   # (DSQMIX)_{33}
  3  4     4.70892350e-06   # (DSQMIX)_{34}
  3  5     9.99991577e-01   # (DSQMIX)_{35}
  3  6    -3.09239761e-04   # (DSQMIX)_{36}
  4  1     1.86787003e-04   # (DSQMIX)_{41}
  4  2     5.89311647e-08   # (DSQMIX)_{42}
  4  3    -2.22640692e-06   # (DSQMIX)_{43}
  4  4     9.99999983e-01   # (DSQMIX)_{44}
  4  5    -4.70813116e-06   # (DSQMIX)_{45}
  4  6     1.91897094e-06   # (DSQMIX)_{46}
  5  1    -1.36865243e-01   # (DSQMIX)_{51}
  5  2     9.89909904e-01   # (DSQMIX)_{52}
  5  3     3.61504716e-02   # (DSQMIX)_{53}
  5  4     2.55769377e-05   # (DSQMIX)_{54}
  5  5    -4.05017742e-03   # (DSQMIX)_{55}
  5  6    -4.79850879e-03   # (DSQMIX)_{56}
  6  1     9.90577497e-01   # (DSQMIX)_{61}
  6  2     1.36952058e-01   # (DSQMIX)_{62}
  6  3     8.61138920e-05   # (DSQMIX)_{63}
  6  4    -1.85037500e-04   # (DSQMIX)_{64}
  6  5    -5.60096523e-04   # (DSQMIX)_{65}
  6  6    -1.14243519e-05   # (DSQMIX)_{66}
Block RVLMIX  # charged higgs-slepton mixing matrix 
  1 1    0.00000000e+00   # C_{11}
  1 2    0.00000000e+00   # C_{12}
  1 3    0.00000000e+00   # C_{13}
  1 4    0.00000000e+00   # C_{14}
  1 5    1.32438249e-01   # C_{15}
  1 6    0.00000000e+00   # C_{16}
  1 7    0.00000000e+00   # C_{17}
  1 8    9.91191258e-01   # C_{18}
  2 1    0.00000000e+00   # C_{21}
  2 2    0.00000000e+00   # C_{22}
  2 3    0.00000000e+00   # C_{23}
  2 4    7.89736330e-03   # C_{24}
  2 5    0.00000000e+00   # C_{25}
  2 6    0.00000000e+00   # C_{26}
  2 7    9.99968815e-01   # C_{27}
  2 8    0.00000000e+00   # C_{28}
  3 1    0.00000000e+00   # C_{31}
  3 2    0.00000000e+00   # C_{32}
  3 3    3.81990318e-05   # C_{33}
  3 4    0.00000000e+00   # C_{34}
  3 5    0.00000000e+00   # C_{35}
  3 6    9.99999999e-01   # C_{36}
  3 7    0.00000000e+00   # C_{37}
  3 8    0.00000000e+00   # C_{38}
  4 1    0.00000000e+00   # C_{41}
  4 2    0.00000000e+00   # C_{42}
  4 3    9.99999999e-01   # C_{43}
  4 4    0.00000000e+00   # C_{44}
  4 5    0.00000000e+00   # C_{45}
  4 6   -3.81990318e-05   # C_{46}
  4 7    0.00000000e+00   # C_{47}
  4 8    0.00000000e+00   # C_{48}
  5 1    0.00000000e+00   # C_{51}
  5 2    0.00000000e+00   # C_{52}
  5 3    0.00000000e+00   # C_{53}
  5 4    9.99968815e-01   # C_{54}
  5 5    0.00000000e+00   # C_{55}
  5 6    0.00000000e+00   # C_{56}
  5 7   -7.89736330e-03   # C_{57}
  5 8    0.00000000e+00   # C_{58}
  6 1    0.00000000e+00   # C_{61}
  6 2    0.00000000e+00   # C_{62}
  6 3    0.00000000e+00   # C_{63}
  6 4    0.00000000e+00   # C_{64}
  6 5    9.91191258e-01   # C_{65}
  6 6    0.00000000e+00   # C_{66}
  6 7    0.00000000e+00   # C_{67}
  6 8   -1.32438249e-01   # C_{68}
  7 1    9.94690129e-01   # C_{71}
  7 2    1.02915244e-01   # C_{72}
  7 3    0.00000000e+00   # C_{73}
  7 4    0.00000000e+00   # C_{74}
  7 5    0.00000000e+00   # C_{75}
  7 6    0.00000000e+00   # C_{76}
  7 7    0.00000000e+00   # C_{77}
  7 8    0.00000000e+00   # C_{78}
Block RVHMIX  # CP-even neutral scalar mixing matrix 
  1 1    1.05503554e-01   # curlyN_{11}
  1 2    9.94418926e-01   # curlyN_{12}
  1 3    0.00000000e+00   # curlyN_{13}
  1 4    0.00000000e+00   # curlyN_{14}
  1 5    0.00000000e+00   # curlyN_{15}
  2 1    0.00000000e+00   # curlyN_{21}
  2 2    0.00000000e+00   # curlyN_{22}
  2 3    0.00000000e+00   # curlyN_{23}
  2 4    0.00000000e+00   # curlyN_{24}
  2 5    1.00000000e+00   # curlyN_{25}
  3 1    0.00000000e+00   # curlyN_{31}
  3 2    0.00000000e+00   # curlyN_{32}
  3 3    0.00000000e+00   # curlyN_{33}
  3 4    1.00000000e+00   # curlyN_{34}
  3 5    0.00000000e+00   # curlyN_{35}
  4 1    0.00000000e+00   # curlyN_{41}
  4 2    0.00000000e+00   # curlyN_{42}
  4 3    1.00000000e+00   # curlyN_{43}
  4 4    0.00000000e+00   # curlyN_{44}
  4 5    0.00000000e+00   # curlyN_{45}
  5 1    9.94418926e-01   # curlyN_{51}
  5 2   -1.05503554e-01   # curlyN_{52}
  5 3    0.00000000e+00   # curlyN_{53}
  5 4    0.00000000e+00   # curlyN_{54}
  5 5    0.00000000e+00   # curlyN_{55}
Block RVAMIX  # CP-odd neutral scalar mixing matrix 
  1 1    0.00000000e+00   # curlyN~_{11}
  1 2    0.00000000e+00   # curlyN~_{12}
  1 3    0.00000000e+00   # curlyN~_{13}
  1 4    0.00000000e+00   # curlyN~_{14}
  1 5    1.00000000e+00   # curlyN~_{15}
  2 1    0.00000000e+00   # curlyN~_{21}
  2 2    0.00000000e+00   # curlyN~_{22}
  2 3    0.00000000e+00   # curlyN~_{23}
  2 4    1.00000000e+00   # curlyN~_{24}
  2 5    0.00000000e+00   # curlyN~_{25}
  3 1    0.00000000e+00   # curlyN~_{31}
  3 2    0.00000000e+00   # curlyN~_{32}
  3 3    1.00000000e+00   # curlyN~_{33}
  3 4    0.00000000e+00   # curlyN~_{34}
  3 5    0.00000000e+00   # curlyN~_{35}
  4 1    9.94690132e-01   # curlyN~_{41}
  4 2    1.02915214e-01   # curlyN~_{42}
  4 3    0.00000000e+00   # curlyN~_{43}
  4 4    0.00000000e+00   # curlyN~_{44}
  4 5    0.00000000e+00   # curlyN~_{45}
