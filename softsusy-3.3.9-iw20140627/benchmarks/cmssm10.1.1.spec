# SOFTSUSY3.3.9 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.3.9       # version number
Block MODSEL  # Select model
     1    1   # sugra
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.00000000e+01   # tanb
     4    1.00000000e+00   # sign(mu)
     1    1.25000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.87397038e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=6.98752212e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03966438e+01   # MW
        25     1.14893670e+02   # h0
        35     7.18021423e+02   # H0
        36     7.17744245e+02   # A0
        37     7.22473881e+02   # H+
   1000021     1.14697670e+03   # ~g
   1000022     2.04229888e+02   # ~neutralino(1)
   1000023     3.85953130e+02   # ~neutralino(2)
   1000024     3.85964787e+02   # ~chargino(1)
   1000025    -6.35418512e+02   # ~neutralino(3)
   1000035     6.49082326e+02   # ~neutralino(4)
   1000037     6.49407682e+02   # ~chargino(2)
   1000001     1.05534278e+03   # ~d_L
   1000002     1.05250356e+03   # ~u_L
   1000003     1.05534020e+03   # ~s_L
   1000004     1.05250098e+03   # ~c_L
   1000005     9.66106638e+02   # ~b_1
   1000006     8.04556382e+02   # ~t_1
   1000011     3.61732332e+02   # ~e_L
   1000012     3.52829770e+02   # ~nue_L
   1000013     3.61729056e+02   # ~mu_L
   1000014     3.52826423e+02   # ~numu_L
   1000015     2.22716151e+02   # ~stau_1
   1000016     3.51659274e+02   # ~nu_tau_L
   2000001     1.01074956e+03   # ~d_R
   2000002     1.01406924e+03   # ~u_R
   2000003     1.01074687e+03   # ~s_R
   2000004     1.01406649e+03   # ~c_R
   2000005     1.00746209e+03   # ~b_2
   2000006     1.01149434e+03   # ~t_2
   2000011     2.29854758e+02   # ~e_R
   2000013     2.29844323e+02   # ~mu_R
   2000015     3.62872241e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06795863e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95805827e-01   # N_{1,1}
  1  2    -1.74963294e-02   # N_{1,2}
  1  3     8.29381070e-02   # N_{1,3}
  1  4    -3.44369426e-02   # N_{1,4}
  2  1     3.81464358e-02   # N_{2,1}
  2  2     9.70403552e-01   # N_{2,2}
  2  3    -1.98321550e-01   # N_{2,3}
  2  4     1.32402258e-01   # N_{2,4}
  3  1    -3.32414872e-02   # N_{3,1}
  3  2     4.84244368e-02   # N_{3,2}
  3  3     7.03438565e-01   # N_{3,3}
  3  4     7.08324970e-01   # N_{3,4}
  4  1    -7.62273384e-02   # N_{4,1}
  4  2     2.35936216e-01   # N_{4,2}
  4  3     6.77468833e-01   # N_{4,3}
  4  4    -6.92502329e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.58912952e-01   # U_{1,1}
  1  2    -2.83700460e-01   # U_{1,2}
  2  1     2.83700460e-01   # U_{2,1}
  2  2     9.58912952e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.81790872e-01   # V_{1,1}
  1  2    -1.89964953e-01   # V_{1,2}
  2  1     1.89964953e-01   # V_{2,1}
  2  2     9.81790872e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.26570184e-01   # F_{11}
  1  2     9.04454465e-01   # F_{12}
  2  1     9.04454465e-01   # F_{21}
  2  2    -4.26570184e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.75796552e-01   # F_{11}
  1  2     2.18680333e-01   # F_{12}
  2  1    -2.18680333e-01   # F_{21}
  2  2     9.75796552e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.42033706e-01   # F_{11}
  1  2     9.89861822e-01   # F_{12}
  2  1     9.89861822e-01   # F_{21}
  2  2    -1.42033706e-01   # F_{22}
Block gauge Q= 8.74650664e+02  # SM gauge couplings
     1     3.62418838e-01   # g'(Q)MSSM DRbar
     2     6.43002750e-01   # g(Q)MSSM DRbar
     3     1.06092720e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.74650664e+02  
  3  3     8.61186154e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.74650664e+02  
  3  3     1.35322630e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.74650664e+02  
  3  3     1.00513771e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.74650664e+02 # Higgs mixing parameters
     1     6.29931069e+02    # mu(Q)MSSM DRbar
     2     9.67352186e+00    # tan beta(Q)MSSM DRbar
     3     2.44115788e+02    # higgs vev(Q)MSSM DRbar
     4     5.34459938e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.74650664e+02  # MSSM DRbar SUSY breaking parameters
     1     2.09311197e+02      # M_1(Q)
     2     3.88509042e+02      # M_2(Q)
     3     1.11339802e+03      # M_3(Q)
    21     1.09119511e+05      # mH1^2(Q)
    22    -3.84358981e+05      # mH2^2(Q)
    31     3.54224756e+02      # meL(Q)
    32     3.54221423e+02      # mmuL(Q)
    33     3.53216493e+02      # mtauL(Q)
    34     2.22002006e+02      # meR(Q)
    35     2.21991190e+02      # mmuR(Q)
    36     2.18709521e+02      # mtauR(Q)
    41     1.01835260e+03      # mqL1(Q)
    42     1.01834998e+03      # mqL2(Q)
    43     9.38585094e+02      # mqL3(Q)
    44     9.80337408e+02      # muR(Q)
    45     9.80334618e+02      # mcR(Q)
    46     8.07037854e+02      # mtR(Q)
    47     9.75738733e+02      # mdR(Q)
    48     9.75735992e+02      # msR(Q)
    49     9.70731245e+02      # mbR(Q)
Block au Q= 8.74650664e+02  
  1  1    -1.14073241e+03      # Au(Q)MSSM DRbar
  2  2    -1.14072730e+03      # Ac(Q)MSSM DRbar
  3  3    -8.80143020e+02      # At(Q)MSSM DRbar
Block ad Q= 8.74650664e+02  
  1  1    -1.39566894e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39566419e+03      # As(Q)MSSM DRbar
  3  3    -1.30417573e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.74650664e+02  
  1  1    -2.99340251e+02      # Ae(Q)MSSM DRbar
  2  2    -2.99334874e+02      # Amu(Q)MSSM DRbar
  3  3    -2.97713643e+02      # Atau(Q)MSSM DRbar
