import Image from "next/image";
import Card from "./card";
import './globals.css'

export default function Home() {
  const data = [
    {
      polyline: "}g|eFnpqjVl@En@Md@HbAd@d@^h@Xx@VbARjBDh@OPQf@w@d@k@XKXDFPH\\EbGT`AV`@v@|@NTNb@?XOb@cAxAWLuE@eAFMBoAv@eBt@q@b@}@tAeAt@i@dAC`AFZj@dB?~@[h@MbAVn@b@b@\\d@Eh@Qb@_@d@eB|@c@h@WfBK|AMpA?VF\\\\t@f@t@h@j@|@b@hCb@b@XTd@Bl@GtA?jAL`ALp@Tr@RXd@Rx@Pn@^Zh@Tx@Zf@`@FTCzDy@f@Yx@m@n@Op@VJr@",
      mileage: 5.5,
      time: "1:30:25"
    },
    {
      polyline: "afutG|bvkV}@PYCc@RcAPk@?g@Eg@LEGCL?n@CRHj@s@T[Du@Ao@IU@qAXe@GS@SO]E_@Fe@?q@JmAd@a@XYDUo@Q_AKYSiAOg@SqAIQO_Aa@kAmAaCkAiBWi@EWi@q@i@{@Ui@QQ{@aB}@sAy@gB_@g@i@eAW]cAsBIaAFq@@cBPUt@GRIJOH_@@}@Ck@Ba@Co@PW\\GtEEdAShABHEj@Az@BtAKFIR?|Ac@pAm@`Cw@nA]XSZKx@EVMv@?xJeB`A[vEw@f@Al@SR@d@QZApBe@|AQz@QFB^OvB]bBk@hCqA|@u@^g@v@o@r@s@~@kAhBeDVu@LSh@wA`@wATe@VaAd@oA~@uBV]JUp@s@^k@bA{@JC`@e@p@]PCTQpA]pC[tBB`AN|@RjAl@~@Xj@\\\\Zt@\\bAl@d@^lDrBRTh@Vp@f@h@Rl@b@ZZp@j@p@b@d@NxAp@f@`@XLpAx@\\ZjBhA\\ZhAl@bCbB~Ax@hChB|Ar@x@h@N@@FLPvChBTRLBv@d@LNVPtAz@t@^fBlAhA~@pCtANNjAl@bA`@\\VbBn@`FdAlANz@?b@FtBFbDKp@GtCg@lCs@`@_@@UKS@KESHWTBRMZGLF\\CFH?n@D^C^DjABhEEjD@bHEhD?|IExAKVSLo@FyA\\o@Z{Bx@_@TGIBKJAn@c@rAi@`@Y\\MBI?MMGo@l@{Ax@[DONk@Pc@XS@}@n@wAj@k@`@}@Z}Ax@y@R}ATc@IgAi@q@FaBYw@C]OiCOOFQr@UXSJo@JmBH[UYc@OAa@PYDOV_@Lm@MiAJkADMEc@Lo@DgBKyDLiB?iARSLINe@PIJ[RU@g@\\kAAYHGGCcADeACKKG]C_@HSPm@XSP}@b@yAZg@?WRGZILWNw@Og@U]GkA`@s@d@e@NQRc@TcC@g@N_@Ta@He@XcAZc@EqAyAYQwBMkBPMFO\\URi@zAMP_AHmBEc@FYCUM[EOSM}@WaA]g@Gc@Q_@SQ_AMk@[YG_@DMHCTKJo@\\g@L[Se@EIKA]Q_AGq@O]g@Wa@E]Uc@Ge@YQEUDENGBOj@Gj@WNcADSJ}@CYLEHa@G_AN]A",
      mileage: 7.3,
      time: "1:20:30"
    }
  ];

  return (
    <>
      {data.map((entry, index) => (
        <Card key={index} polyline={entry.polyline} mileage={entry.mileage} time={entry.time} />
      ))}
    </>
  );
}
