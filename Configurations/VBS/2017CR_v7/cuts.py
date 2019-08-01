# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

# supercut='\
# nLepton>1 && nCleanJet > 1 &&\
# Alt$(Lepton_pt[0],0.)>30 && Alt$(Lepton_pt[1],0.)>30 && Alt$(Lepton_pt[2],0.)<10 && mjj >500 && detajj > 2.5\
# && abs(Alt$(CleanJet_eta[1],-9999.))<5 && abs(Alt$(CleanJet_eta[0],-9999.))<5\
# && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5 && Alt$(CleanJet_pt[0],-9999.) >30 && Alt$(CleanJet_pt[1],-9999.) >30'

supercut='\
mjj > 500 && nLepton >= 2 && nCleanJet >= 2'
#((Alt$(abs(Lepton_pdgId[0]),-9999)==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[0]],-9999)==2) || Alt$(abs(Lepton_pdgId[0]),-9999)==13) && ((Alt$(abs(Lepton_pdgId[1]),-9999)==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[1]],-9999)==2) || Alt$(abs(Lepton_pdgId[1]),-9999)==13) && ((Alt$(abs(Lepton_pdgId[2]),-9999)==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[2]],-9999)==2) || Alt$(abs(Lepton_pdgId[2]),-9999)==13) && ((Alt$(abs(Lepton_pdgId[3]),-9999)==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[3]],-9999)==2) || Alt$(abs(Lepton_pdgId[3]),-9999)==13)
triple_charge = '((abs(Alt$(Lepton_pdgId[0],-9999))==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[0]],-9999)==2) || abs(Alt$(Lepton_pdgId[0],-9999))==13) && ((abs(Alt$(Lepton_pdgId[1],-9999))==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[1]],-9999)==2) || abs(Alt$(Lepton_pdgId[1],-9999))==13)'
triple_charge_wz = '((abs(Alt$(Lepton_pdgId[0],-9999))==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[0]],-9999)==2) || abs(Alt$(Lepton_pdgId[0],-9999))==13) && ((abs(Alt$(Lepton_pdgId[1],-9999))==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[1]],-9999)==2) || abs(Alt$(Lepton_pdgId[1],-9999))==13) && ((abs(Alt$(Lepton_pdgId[2],-9999))==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[2]],-9999)==2) || abs(Alt$(Lepton_pdgId[2],-9999))==13)'
triple_charge_zz = '((abs(Alt$(Lepton_pdgId[0],-9999))==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[0]],-9999)==2) || abs(Alt$(Lepton_pdgId[0],-9999))==13) && ((abs(Alt$(Lepton_pdgId[1],-9999))==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[1]],-9999)==2) || abs(Alt$(Lepton_pdgId[1],-9999))==13) && ((abs(Alt$(Lepton_pdgId[2],-9999))==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[2]],-9999)==2) || abs(Alt$(Lepton_pdgId[2],-9999))==13) && ((abs(Alt$(Lepton_pdgId[3],-9999))==11 && Alt$(Electron_tightCharge[Lepton_electronIdx[3]],-9999)==2) || abs(Alt$(Lepton_pdgId[3],-9999))==13)'
#supercut='1'#for test on raw samples

ww = ' Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) > 0 && Alt$(Lepton_pt[2],0.)<10 && mll > 20  && mjj > 500 && abs(detajj) > 2.5 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7 && abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7'  # bveto tauveto zveto zlep
top = ' Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) > 0 && Alt$(Lepton_pt[2],0.)<10 && mll > 20  && mjj > 500 && abs(detajj) > 2.5 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7 && abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7'  # bveto tauveto zveto zlep
lowmjj = 'Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) > 0 && Alt$(Lepton_pt[2],0.)<10 && mll > 20 && mjj < 500 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7 && abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7'  # bveto tauveto zveto zlep
wz = 'Alt$(Lepton_pt[2],0.) > 10 && (Lepton_isTightMuon_cut_Tight_HWWW[2] ==1 || Lepton_isTightElectron_mvaFall17Iso_WP90[2] ==1)&& Alt$(Lepton_pt[3],0.) < 10 && mjj > 500 && abs(detajj) > 2.5 && abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7 && abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7'  # bveto tauveto zveto zlep

lep_eta = '(((abs(Alt$(Lepton_pdgId[0],-9999))==11 && abs(Alt$(Lepton_eta[0],-9999.)) <=2.4) || (abs(Alt$(Lepton_pdgId[0],-9999))==13 && abs(Alt$(Lepton_eta[0],-9999.)) <=2.5)) && ((abs(Alt$(Lepton_pdgId[1],-9999))==11 && abs(Alt$(Lepton_eta[1],-9999.)) <=2.4) || (abs(Alt$(Lepton_pdgId[1],-9999))==13 && abs(Alt$(Lepton_eta[1],-9999.)) <=2.5)))'

#signal cuts are used as preselections

zveto ='(abs(Alt$(Lepton_pdgId[0],-9999)) * abs(Alt$(Lepton_pdgId[1],-9999)) != 11*11 || abs(mll - 91.1876) > 15)'
zlep='\
(abs((Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/abs(detajj)) <= 0.5) \
&&(abs((Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/abs(detajj)) <= 0.5)'
ztag ='((abs(mll - 91.1876) < 15 && (Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[1],-9999) == 0)) \
|| (abs(mllOneThree - 91.1876) < 15 && (Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[2],-9999) == 0)) \
|| (abs(mllTwoThree - 91.1876) < 15 && (Alt$(Lepton_pdgId[1],-9999) + Alt$(Lepton_pdgId[2],-9999) == 0)))'
ztag1 ='Alt$(WH3l_mlll,-9999.) > 100 \
&& abs(Alt$(Lepton_pdgId[0],-9999) + Alt$(Lepton_pdgId[1],-9999) + Alt$(Lepton_pdgId[2],-9999)) < 20 \
&& ((abs(mll - 91) < 15 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) <0) \
|| (abs(mllOneThree - 91) < 15 && Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[2],-9999) < 0) \
|| (abs(mllTwoThree - 91) < 15 && Alt$(Lepton_pdgId[1],-9999) * Alt$(Lepton_pdgId[2],-9999) < 0))'


# cuts['WW_BVeto_tauVeto_zlep_zveto']=ww+'&&'+BVeto+'&&'+tauVeto+'&&'+zlep+'&&'+zveto+'&&'+charge_ww
tauVeto='!((Alt$(Tau_pt[0],-9999.) > 18 && Alt$(Tau_rawIso[0],-9999) >=1 && sqrt( pow(Alt$(Tau_eta[0],-9999.) - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[0],-9999.) - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Alt$(Tau_eta[0],-9999.) - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[0],-9999.) - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) >= 0.3) || \
(Alt$(Tau_pt[1],-9999.) > 18 && Alt$(Tau_rawIso[1],-9999) >=1 && sqrt( pow(Alt$(Tau_eta[1],-9999.) - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[1],-9999.) - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Alt$(Tau_eta[1],-9999.) - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[1],-9999.) - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) >= 0.3) || \
(Alt$(Tau_pt[2],-9999.) > 18 && Alt$(Tau_rawIso[2],-9999) >=1 && sqrt( pow(Alt$(Tau_eta[2],-9999.) - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[2],-9999.) - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Alt$(Tau_eta[2],-9999.) - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[2],-9999.) - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) >= 0.3) || \
(Alt$(Tau_pt[3],-9999.) > 18 && Alt$(Tau_rawIso[3],-9999) >=1 && sqrt( pow(Alt$(Tau_eta[3],-9999.) - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[3],-9999.) - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Alt$(Tau_eta[3],-9999.) - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[3],-9999.) - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) >= 0.3) || \
(Alt$(Tau_pt[4],-9999.) > 18 && Alt$(Tau_rawIso[4],-9999) >=1 && sqrt( pow(Alt$(Tau_eta[4],-9999.) - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[4],-9999.) - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Alt$(Tau_eta[4],-9999.) - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[4],-9999.) - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) >= 0.3) || \
(Alt$(Tau_pt[5],-9999.) > 18 && Alt$(Tau_rawIso[5],-9999) >=1 && sqrt( pow(Alt$(Tau_eta[5],-9999.) - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[5],-9999.) - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Alt$(Tau_eta[5],-9999.) - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[5],-9999.) - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) >= 0.3) || \
(Alt$(Tau_pt[6],-9999.) > 18 && Alt$(Tau_rawIso[6],-9999) >=1 && sqrt( pow(Alt$(Tau_eta[6],-9999.) - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[6],-9999.) - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Alt$(Tau_eta[6],-9999.) - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[6],-9999.) - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) >= 0.3) || \
(Alt$(Tau_pt[7],-9999.) > 18 && Alt$(Tau_rawIso[7],-9999) >=1 && sqrt( pow(Alt$(Tau_eta[7],-9999.) - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[7],-9999.) - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Alt$(Tau_eta[7],-9999.) - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[7],-9999.) - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) >= 0.3) || \
(Alt$(Tau_pt[8],-9999.) > 18 && Alt$(Tau_rawIso[8],-9999) >=1 && sqrt( pow(Alt$(Tau_eta[8],-9999.) - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[8],-9999.) - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Alt$(Tau_eta[8],-9999.) - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[8],-9999.) - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) >= 0.3) || \
(Alt$(Tau_pt[9],-9999.) > 18 && Alt$(Tau_rawIso[9],-9999) >=1 && sqrt( pow(Alt$(Tau_eta[9],-9999.) - Alt$(Lepton_eta[0],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[9],-9999.) - Alt$(Lepton_phi[0],-9999.))-pi)-pi, 2) ) >= 0.3 && sqrt( pow(Alt$(Tau_eta[9],-9999.) - Alt$(Lepton_eta[1],-9999.), 2) + pow(abs(abs(Alt$(Tau_phi[9],-9999.) - Alt$(Lepton_phi[1],-9999.))-pi)-pi, 2) ) >= 0.3))'
cuts['ww_tauVeto_ww']='Alt$(Lepton_pt[0],0.)>25 && Alt$(Lepton_pt[1],0.)>20 && Alt$(Lepton_pt[2],0.)<10 &&  Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) >0 && abs(Alt$(CleanJet_eta[0],-9999.)) < 5.0 && abs(Alt$(CleanJet_eta[1],-9999.)) < 5.0 && Alt$(CleanJet_pt[0],-9999.)>30 && Alt$(CleanJet_pt[1],-9999.)>30 && detajj > 2.5 && MET_pt> 30 && mll>10 && dmZll_veto >10&&'+ lep_eta+ '&& tauVeto_ww'
cuts['ww_tauVeto_ww2']='Alt$(Lepton_pt[0],0.)>25 && Alt$(Lepton_pt[1],0.)>20 && Alt$(Lepton_pt[2],0.)<10 &&  Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) >0 && abs(Alt$(CleanJet_eta[0],-9999.)) < 5.0 && abs(Alt$(CleanJet_eta[1],-9999.)) < 5.0 && Alt$(CleanJet_pt[0],-9999.)>30 && Alt$(CleanJet_pt[1],-9999.)>30 && detajj > 2.5 && MET_pt> 30 && mll>10 && dmZll_veto >10&&'+ lep_eta+ '&& tauVeto_ww2'
cuts['ww_tauVeto']='Alt$(Lepton_pt[0],0.)>25 && Alt$(Lepton_pt[1],0.)>20 && Alt$(Lepton_pt[2],0.)<10 &&  Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],-9999) >0 && abs(Alt$(CleanJet_eta[0],-9999.)) < 5.0 && abs(Alt$(CleanJet_eta[1],-9999.)) < 5.0 && Alt$(CleanJet_pt[0],-9999.)>30 && Alt$(CleanJet_pt[1],-9999.)>30 && detajj > 2.5 && MET_pt> 30 && mll>10 && dmZll_veto >10&&'+ lep_eta+ '&&'+ tauVeto

#cuts['ww1']=ww1+'&& bVeto &&'+zlep+'&&'+zveto+'&&'+ssww+'&& tauVeto_ww && '+lep_eta+'&&'+veto_l3
#cuts['ww1_bVeto1']=ww+'&& bVeto1 &&'+zlep+'&&'+zveto+'&&'+ssww+'&& tauVeto_ww && '+lep_eta+'&&'+veto_l3
#cuts['ww1_bVeto2']=ww+'&& bVeto2 &&'+zlep+'&&'+zveto+'&&'+ssww+'&& tauVeto_ww && '+lep_eta+'&&'+veto_l3
#cuts['ww1_bVeto3']=ww+'&& bVeto3 &&'+zlep+'&&'+zveto+'&&'+ssww+'&& tauVeto_ww && '+lep_eta+'&&'+veto_l3
#cuts['ww1_zveto1']=ww+'&& bVeto &&'+zlep+'&&'+zveto1+'&&'+ssww+'&& tauVeto_ww && '+lep_eta+'&&'+veto_l3
#cuts['ww1_lep_eta1']=ww+'&& bVeto &&'+zlep+'&&'+zveto+'&&'+ssww+'&& tauVeto_ww && '+lep_eta1+'&&'+veto_l3
#cuts['ww1_veto_l31']=ww+'&& bVeto &&'+zlep+'&&'+zveto+'&&'+ssww+'&& tauVeto_ww && '+lep_eta+'&&'+veto_l31
