	SUBROUTINE RGESOFT(PAR,IFAIL)

*   Subroutine to integrate the RGEs for all 21 soft terms
*   from the SUSY scale Q2 up to MGUT, through a call of the
*   subroutine ODEINTS that is part of the file integ.f
*   Q2 is either computed in terms of the first generation squarks, 
*   or put in by the user.
*
*   Present accuracy: 
*   Gauginos: two loops
*   Trilinear couplings and scalar masses: two loops, 
*   except for terms ~lambda**2 and kappa**2
*
*   MGUT and the gauge/Yukawa couplings at Q2 are read in from
*   COMMON/SUSYCOUP.
* 
*   The soft terms at Q2 are read in from PAR(*), the soft Higgs
*   masses squared at the scale QSTSB from COMMON/QMHIGGS.
*   They still have to be integrated to the SUSY scale Q2.
*   All sparticle threshold effects are taken into account.
*
*   CAUTION: Near an infrared quasi fixed point, very small changes in 
*   A_top, M3 or M_HU^2 at low energy can cause a very large changes 
*   of M_HU^2 and the stop masses at MGUT!
*********************************************************************** 

	IMPLICIT NONE

	INTEGER IFAIL,NN
	PARAMETER (NN=30)

	DOUBLE PRECISION PAR(*),EPS,X1,X2,Y(NN),PI,COEF
	DOUBLE PRECISION MGUT,g1s,g2s,g3s,HTOPS,HBOTS,HTAUS
	DOUBLE PRECISION LS2,KS2,HTOPS2,HBOTS2,HTAUS2
	DOUBLE PRECISION MS,MC,MB,MBP,MT,MTAU,MMUON,MZ,MW
	DOUBLE PRECISION MHU,MHD,MSS,Q2,QSTSB,ANOMQSTSB
	DOUBLE PRECISION LQSTSB,LM1QSTSB,LM2QSTSB
	DOUBLE PRECISION LM3QSTSB,LMQ3QSTSB,LMU3QSTSB
	DOUBLE PRECISION LMD3QSTSB,LMQQSTSB,LMUQSTSB,LMDQSTSB
	DOUBLE PRECISION LML3QSTSB,LME3QSTSB,LMLQSTSB,LMEQSTSB
	DOUBLE PRECISION RTOP,RBOT,RTAU,RL,RK,RG
	DOUBLE PRECISION M1,M2,M3,ALS,AKS,AT,AB,ATAU,AMUON
	DOUBLE PRECISION MHUS,MHDS,MSSS,MQ3,MU3,MD3,MQ
	DOUBLE PRECISION MU,MD,ML3,ME3,ML,ME
	DOUBLE PRECISION G1GUT,G2GUT,G3GUT,LGUT,KGUT,HTOPGUT
	DOUBLE PRECISION HBOTGUT,HTAUGUT,M1GUT,M2GUT,M3GUT,ALGUT,AKGUT
	DOUBLE PRECISION ATGUT,ABGUT,ATAUGUT,AMUGUT
	DOUBLE PRECISION MHUGUT,MHDGUT,MSSGUT,MQ3GUT
	DOUBLE PRECISION MU3GUT,MD3GUT,MQGUT,MUGUT,MDGUT,ML3GUT,ME3GUT
	DOUBLE PRECISION MLGUT,MEGUT

	COMMON/SUSYCOUP/MGUT,g1s,g2s,g3s,HTOPS,HBOTS,HTAUS
	COMMON/SMSPEC/MS,MC,MB,MBP,MT,MTAU,MMUON,MZ,MW
	COMMON/RENSCALE/Q2
	COMMON/STSBSCALE/QSTSB
	COMMON/QMHIGGS/MHU,MHD,MSS
	COMMON/SUSYMH/MHUS,MHDS,MSSS
	COMMON/GUTCOUP/G1GUT,G2GUT,G3GUT,LGUT,KGUT,HTOPGUT,
     C        HBOTGUT,HTAUGUT
	COMMON/GUTPAR/M1GUT,M2GUT,M3GUT,ALGUT,AKGUT,ATGUT,ABGUT,
     C        ATAUGUT,AMUGUT,MHUGUT,MHDGUT,MSSGUT,MQ3GUT,MU3GUT,MD3GUT,
     C        MQGUT,MUGUT,MDGUT,ML3GUT,ME3GUT,MLGUT,MEGUT
	
	EXTERNAL DERIVSS,RKQSS

	IF(IFAIL.NE.0)RETURN

	!PRINT*,"CALL RGESOFT"
	!PRINT*,""

	EPS=1.D-8
	PI=4.D0*DATAN(1.D0)
	COEF=1.D0/(16.D0*PI**2)
	
	LS2=PAR(1)**2
	KS2=PAR(2)**2
	HTOPS2=HTOPS**2
	HBOTS2=HBOTS**2
	HTAUS2=HTAUS**2
	ALS=PAR(5)
	AKS=PAR(6)
	AT=PAR(12)
	AB=PAR(13)
	ATAU=PAR(14)
	AMUON=PAR(24)
	M1=PAR(20)
	M2=PAR(21)
	M3=PAR(22)
	MQ3=PAR(7)
	MU3=PAR(8)
	MD3=PAR(9)
	ML3=PAR(10)
	ME3=PAR(11)
	MQ=PAR(15)
	MU=PAR(16)
	MD=PAR(17)
	ML=PAR(18)
	ME=PAR(19)

*  Useful logarithms:

	LQSTSB=DLOG(Q2/QSTSB)
	LM1QSTSB=DLOG(Q2/MAX(M1**2,QSTSB))
	LM2QSTSB=DLOG(Q2/MAX(M2**2,QSTSB))
	LM3QSTSB=DLOG(Q2/MAX(M3**2,QSTSB))
	LMQ3QSTSB=DLOG(Q2/MAX(MQ3,QSTSB))
	LMU3QSTSB=DLOG(Q2/MAX(MU3,QSTSB))
	LMD3QSTSB=DLOG(Q2/MAX(MD3,QSTSB))
	LMQQSTSB=DLOG(Q2/MAX(MQ,QSTSB))
	LMUQSTSB=DLOG(Q2/MAX(MU,QSTSB))
	LMDQSTSB=DLOG(Q2/MAX(MD,QSTSB))
	LML3QSTSB=DLOG(Q2/MAX(ML3,QSTSB))
	LME3QSTSB=DLOG(Q2/MAX(ME3,QSTSB))
	LMLQSTSB=DLOG(Q2/MAX(ML,QSTSB))
	LMEQSTSB=DLOG(Q2/MAX(ME,QSTSB))

* The Higgs masses squared:

	ANOMQSTSB=G1S*(-MHD*LQSTSB+MQ3*LMQ3QSTSB
     C          -2.D0*MU3*LMU3QSTSB
     C          +MD3*LMD3QSTSB+2.D0*(MQ*LMQQSTSB
     C          -2.D0*MU*LMUQSTSB+MD*LMDQSTSB)
     C          +ME3*LME3QSTSB-ML3*LML3QSTSB
     C          +2.D0*(ME*LMEQSTSB-ML*LMLQSTSB))

	RTOP=HTOPS2*(MQ3*LMQ3QSTSB+MU3*LMU3QSTSB
     C       +AT**2*LQSTSB)

  	RBOT=HBOTS2*(MHD*LQSTSB+MQ3*LMQ3QSTSB+MD3*LMD3QSTSB
     C       +AB**2*LQSTSB) 

	RTAU=HTAUS2*(MHD*LQSTSB+ML3*LML3QSTSB+ME3*LME3QSTSB
     C       +ATAU**2*LME3QSTSB)

	RL=LS2*(MHD+MSS+ALS**2)*LQSTSB

	RK=KS2*(3.D0*MSS+AKS**2)*LQSTSB

	RG=G1S*M1**2*LM1QSTSB+3.D0*G2S*M2**2*LM2QSTSB

        MHUS=(MHU+COEF*(RL+3.D0*RTOP-RG+ANOMQSTSB/2.D0))
     C      *(Q2/QSTSB)**(COEF*(LS2+3.D0*HTOPS2+G1S/2.D0))
     
        MHDS=MHD+COEF*(RL+3.D0*RBOT+RTAU-RG-ANOMQSTSB/2.D0
     C      +(LS2-G1S/2.D0)*MHU*LQSTSB)

        MSSS=MSS+COEF*(2.D0*RK+2.D0*RL+2.D0*LS2*MHU*LQSTSB)

* Definition of the couplings squared Y(I) at Q2=M_SUSY

	Y(1)=g1s
	Y(2)=g2s
	Y(3)=g3s
	Y(4)=LS2
	Y(5)=KS2
	Y(6)=HTOPS2
	Y(7)=HBOTS2
	Y(8)=HTAUS2

* Definition of the soft terms Y(I) at Q2=M_SUSY

	Y(9)=M1
	Y(10)=M2
	Y(11)=M3
	Y(12)=ALS
	Y(13)=AKS
	Y(14)=AT
	Y(15)=AB
	Y(16)=ATAU
	Y(17)=MHUS
	Y(18)=MHDS
	Y(19)=MSSS
	Y(20)=MQ3
	Y(21)=MU3
	Y(22)=MD3
	Y(23)=MQ
	Y(24)=MU
	Y(25)=MD
	Y(26)=ML3
	Y(27)=ME3
	Y(28)=ML
	Y(29)=ME
	Y(30)=AMUON
	
	X1=0.D0
	X2=COEF*DLOG(MGUT**2/Q2)

	!PRINT*,"MSUSY =",DSQRT(Q2)
	!PRINT*,"G1 =",5.D0/3.D0*Y(1)
	!PRINT*,"G2 =",Y(2)
	!PRINT*,"G3 =",Y(3)
	!PRINT*,"L =",Y(4)
	!PRINT*,"K =",Y(5)
	!PRINT*,"HT =",Y(6)
	!PRINT*,"HB =",Y(7)
	!PRINT*,"HL =",Y(8)
	!PRINT*,"M1 =",Y(9)
	!PRINT*,"M2 =",Y(10)
	!PRINT*,"M3 =",Y(11)
	!PRINT*,"AL =",Y(12)
	!PRINT*,"AK =",Y(13)
	!PRINT*,"ATOP =",Y(14)
	!PRINT*,"ABOT =",Y(15)
	!PRINT*,"ATAU =",Y(16)
	!PRINT*,"AMUON =",Y(30)
	!PRINT*,"MHU =",Y(17)
	!PRINT*,"MHD =",Y(18)
	!PRINT*,"MS =",Y(19)
	!PRINT*,"MQ3 =",Y(20)
	!PRINT*,"MU3 =",Y(21)
	!PRINT*,"MD3 =",Y(22)
	!PRINT*,"MQ =",Y(23)
	!PRINT*,"MU =",Y(24)
	!PRINT*,"MD =",Y(25)
	!PRINT*,"ML3 =",Y(26)
	!PRINT*,"ME3 =",Y(27)
	!PRINT*,"ML =",Y(28)
	!PRINT*,"ME =",Y(29)
	!PRINT*,""

	CALL ODEINTS(Y,NN,X1,X2,EPS,DERIVSS,RKQSS,IFAIL)
	
	!PRINT*,"MGUT =",MGUT
	!PRINT*,"G1GUT =",5.D0/3.D0*Y(1)
	!PRINT*,"G2GUT =",Y(2)
	!PRINT*,"G3GUT =",Y(3)
	!PRINT*,"LGUT =",Y(4)
	!PRINT*,"KGUT =",Y(5)
	!PRINT*,"HTGUT =",Y(6)
	!PRINT*,"HBGUT =",Y(7)
	!PRINT*,"HLGUT =",Y(8)
	!PRINT*,"M1GUT =",Y(9)
	!PRINT*,"M2GUT =",Y(10)
	!PRINT*,"M3GUT =",Y(11)
	!PRINT*,"ALGUT =",Y(12)
	!PRINT*,"AKGUT =",Y(13)
	!PRINT*,"ATOPGUT =",Y(14)
	!PRINT*,"ABOTGUT =",Y(15)
	!PRINT*,"ATAUGUT =",Y(16)
	!PRINT*,"AMUGUT =",Y(30)
	!PRINT*,"MHUGUT =",Y(17)
	!PRINT*,"MHDGUT =",Y(18)
	!PRINT*,"MSGUT =",Y(19)
	!PRINT*,"MQ3GUT =",Y(20)
	!PRINT*,"MU3GUT =",Y(21)
	!PRINT*,"MD3GUT =",Y(22)
	!PRINT*,"MQGUT =",Y(23)
	!PRINT*,"MUGUT =",Y(24)
	!PRINT*,"MDGUT =",Y(25)
	!PRINT*,"ML3GUT =",Y(26)
	!PRINT*,"ME3GUT =",Y(27)
	!PRINT*,"MLGUT =",Y(28)
	!PRINT*,"MEGUT =",Y(29)
	!PRINT*,""

	IF(IFAIL.NE.0)THEN
	 !PRINT*,"IFAIL =",IFAIL
	 !PRINT*,""
	 !PRINT*,""
	 IFAIL=12
	 RETURN
	ENDIF
	!PRINT*,""
	
* Couplings at the GUT scale

	G1GUT=Y(1)
	G2GUT=Y(2)
	G3GUT=Y(3)
	LGUT=Y(4)
	KGUT=Y(5)
	HTOPGUT=Y(6)
	HBOTGUT=Y(7)
	HTAUGUT=Y(8)
	
* Soft terms at the GUT scale

	M1GUT=Y(9)
	M2GUT=Y(10)
	M3GUT=Y(11)
	ALGUT=Y(12)
	AKGUT=Y(13)
	ATGUT=Y(14)
	ABGUT=Y(15)
	ATAUGUT=Y(16)
	MHUGUT=Y(17)
	MHDGUT=Y(18)
	MSSGUT=Y(19)
	MQ3GUT=Y(20)
	MU3GUT=Y(21)
	MD3GUT=Y(22)
	MQGUT=Y(23)
	MUGUT=Y(24)
	MDGUT=Y(25)
	ML3GUT=Y(26)
	ME3GUT=Y(27)
	MLGUT=Y(28)
	MEGUT=Y(29)
	AMUGUT=Y(30)
	
	END


