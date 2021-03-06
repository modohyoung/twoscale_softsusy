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
     1    1.05000000e+03   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.05569695e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.56095998e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03955993e+01   # MW
        25     1.15546189e+02   # h0
        35     1.24696022e+03   # H0
        36     1.24690812e+03   # A0
        37     1.24960824e+03   # H+
   1000021     1.19892505e+03   # ~g
   1000022     2.07781248e+02   # ~neutralino(1)
   1000023     3.93581059e+02   # ~neutralino(2)
   1000024     3.93580636e+02   # ~chargino(1)
   1000025    -6.31593100e+02   # ~neutralino(3)
   1000035     6.46483810e+02   # ~neutralino(4)
   1000037     6.46625025e+02   # ~chargino(2)
   1000001     1.46189132e+03   # ~d_L
   1000002     1.45991321e+03   # ~u_L
   1000003     1.46188625e+03   # ~s_L
   1000004     1.45990814e+03   # ~c_L
   1000005     1.26992314e+03   # ~b_1
   1000006     1.01661700e+03   # ~t_1
   1000011     1.09845265e+03   # ~e_L
   1000012     1.09529460e+03   # ~nue_L
   1000013     1.09843767e+03   # ~mu_L
   1000014     1.09527972e+03   # ~numu_L
   1000015     1.05579453e+03   # ~stau_1
   1000016     1.09071828e+03   # ~nu_tau_L
   2000001     1.43350350e+03   # ~d_R
   2000002     1.43548544e+03   # ~u_R
   2000003     1.43349858e+03   # ~s_R
   2000004     1.43547997e+03   # ~c_R
   2000005     1.42384151e+03   # ~b_2
   2000006     1.29126645e+03   # ~t_2
   2000011     1.06599494e+03   # ~e_R
   2000013     1.06596423e+03   # ~mu_R
   2000015     1.09461158e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04674351e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95660361e-01   # N_{1,1}
  1  2    -1.74538133e-02   # N_{1,2}
  1  3     8.42361102e-02   # N_{1,3}
  1  4    -3.54977150e-02   # N_{1,4}
  2  1     3.93279330e-02   # N_{2,1}
  2  2     9.67844237e-01   # N_{2,2}
  2  3    -2.05409748e-01   # N_{2,3}
  2  4     1.39777255e-01   # N_{2,4}
  3  1    -3.34177498e-02   # N_{3,1}
  3  2     4.83726042e-02   # N_{3,2}
  3  3     7.03487405e-01   # N_{3,3}
  3  4     7.08271711e-01   # N_{3,4}
  4  1    -7.74403855e-02   # N_{4,1}
  4  2     2.46237665e-01   # N_{4,2}
  4  3     6.75141900e-01   # N_{4,3}
  4  4    -6.91052396e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.55549280e-01   # U_{1,1}
  1  2    -2.94831433e-01   # U_{1,2}
  2  1     2.94831433e-01   # U_{2,1}
  2  2     9.55549280e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.79492972e-01   # V_{1,1}
  1  2    -2.01478333e-01   # V_{1,2}
  2  1     2.01478333e-01   # V_{2,1}
  2  2     9.79492972e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.33464121e-01   # F_{11}
  1  2     9.72365417e-01   # F_{12}
  2  1     9.72365417e-01   # F_{21}
  2  2    -2.33464121e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.99134861e-01   # F_{11}
  1  2     4.15876084e-02   # F_{12}
  2  1    -4.15876084e-02   # F_{21}
  2  2     9.99134861e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.38257249e-01   # F_{11}
  1  2     9.90396351e-01   # F_{12}
  2  1     9.90396351e-01   # F_{21}
  2  2    -1.38257249e-01   # F_{22}
Block gauge Q= 1.11563796e+03  # SM gauge couplings
     1     3.62448053e-01   # g'(Q)MSSM DRbar
     2     6.41730679e-01   # g(Q)MSSM DRbar
     3     1.05156079e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.11563796e+03  
  3  3     8.57554636e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.11563796e+03  
  3  3     1.35253472e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.11563796e+03  
  3  3     9.95273359e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.11563796e+03 # Higgs mixing parameters
     1     6.23971936e+02    # mu(Q)MSSM DRbar
     2     9.64101550e+00    # tan beta(Q)MSSM DRbar
     3     2.43630413e+02    # higgs vev(Q)MSSM DRbar
     4     1.58716895e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.11563796e+03  # MSSM DRbar SUSY breaking parameters
     1     2.10819943e+02      # M_1(Q)
     2     3.89854799e+02      # M_2(Q)
     3     1.10018516e+03      # M_3(Q)
    21     1.14794713e+06      # mH1^2(Q)
    22    -3.53858220e+05      # mH2^2(Q)
    31     1.09541001e+03      # meL(Q)
    32     1.09539516e+03      # mmuL(Q)
    33     1.09097365e+03      # mtauL(Q)
    34     1.06371481e+03      # meR(Q)
    35     1.06368408e+03      # mmuR(Q)
    36     1.05451095e+03      # mtauR(Q)
    41     1.42918341e+03      # mqL1(Q)
    42     1.42917821e+03      # mqL2(Q)
    43     1.24144274e+03      # mqL3(Q)
    44     1.40567541e+03      # muR(Q)
    45     1.40566978e+03      # mcR(Q)
    46     9.92264642e+02      # mtR(Q)
    47     1.40292119e+03      # mdR(Q)
    48     1.40291612e+03      # msR(Q)
    49     1.39319940e+03      # mbR(Q)
Block au Q= 1.11563796e+03  
  1  1    -1.11892468e+03      # Au(Q)MSSM DRbar
  2  2    -1.11891970e+03      # Ac(Q)MSSM DRbar
  3  3    -8.63683699e+02      # At(Q)MSSM DRbar
Block ad Q= 1.11563796e+03  
  1  1    -1.36814110e+03      # Ad(Q)MSSM DRbar
  2  2    -1.36813651e+03      # As(Q)MSSM DRbar
  3  3    -1.27848764e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.11563796e+03  
  1  1    -2.97143866e+02      # Ae(Q)MSSM DRbar
  2  2    -2.97138578e+02      # Amu(Q)MSSM DRbar
  3  3    -2.95567127e+02      # Atau(Q)MSSM DRbar
