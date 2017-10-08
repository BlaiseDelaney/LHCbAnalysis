import ROOT as r

r.gROOT.ProcessLine(".x ~/Scratch/lhcb/lhcbStyle.C")

tf = r.TFile("root/AnalysisOutWSWeights.root")
tree = tf.Get("AnalysisTree")

tree.Draw("B_s0_M_pPimKmPip>>h1(150,5000,6500)", "itype>0 && pass_bdt && pass_pid","goff" )
tree.Draw("B_s0_M_pPimKmPip>>h2(150,5000,6500)", "itype>0 && pass_bdt && pass_pid && !pass_lambdab","goff" )
tree.Draw("B_s0_M_KpPimpbPip>>h3(150,5000,6500)", "itype>0 && pass_bdt && pass_pid","goff" )
tree.Draw("B_s0_M_KpPimpbPip>>h4(150,5000,6500)", "itype>0 && pass_bdt && pass_pid && !pass_lambdab","goff" )

#tree.Draw("B_s0_M_PipPimKmPip>>h1(150,4500,5500)", "itype>0 && pass_bdt","goff" )
#tree.Draw("B_s0_M_PipPimKmPip>>h2(150,4500,5500)", "itype>0 && pass_bdt && !pass_rhokst","goff" )
#tree.Draw("B_s0_M_KpPimPimPip>>h3(150,4500,5500)", "itype>0 && pass_bdt","goff" )
#tree.Draw("B_s0_M_KpPimPimPip>>h4(150,4500,5500)", "itype>0 && pass_bdt && !pass_rhokst","goff" )

h1 = r.gROOT.FindObject('h1')
h2 = r.gROOT.FindObject('h2')
h3 = r.gROOT.FindObject('h3')
h4 = r.gROOT.FindObject('h4')

h1.SetLineColor(r.kBlack)
h1.SetLineWidth(3)
h2.SetLineColor(r.kBlack)
h2.SetLineColor(r.kBlue-9)
h2.SetFillColor(r.kBlue-9)
h1.GetXaxis().SetTitle("m(p#pi^{-}K^{-}#pi^{+}) [MeV]")
h1.GetXaxis().SetTitleSize(0.08)
h1.GetXaxis().SetTitleOffset(0.9)

h3.SetLineColor(r.kBlack)
h3.SetLineWidth(3)
h4.SetLineColor(r.kBlack)
h4.SetLineColor(r.kBlue-9)
h4.SetFillColor(r.kBlue-9)
h3.GetXaxis().SetTitle("m(K^{+}#pi^{-}#bar{p}#pi^{+}) [MeV]")
h3.GetXaxis().SetTitleSize(0.08)
h3.GetXaxis().SetTitleOffset(0.9)

leg = r.TLegend(0.6,0.6,0.9,0.9)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry(h1,"Before #Lambda_{B}^{0} veto", "L")
leg.AddEntry(h2,"After #Lambda_{B}^{0} veto", "F")

c1 = r.TCanvas()
h1.Draw("HIST")
h2.Draw("HISTFsame")
h1.Draw("HISTsame")
leg.Draw()
c1.Update()
c1.Modified()
c1.Print("plots/MassVetoes/pdf/LbCutOnP.pdf")

c2 = r.TCanvas()
h3.Draw("HIST")
h4.Draw("HISTFsame")
h3.Draw("HISTsame")
leg.Draw()
c2.Update()
c2.Modified()
c2.Print("plots/MassVetoes/pdf/LbCutOnPb.pdf")

raw_input()