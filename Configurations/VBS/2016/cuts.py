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
mjj > 150'

## Signal regions
cuts['ww'] = {
    'expr': 'ssww_region',
    # Define the sub-categorization of sr
    'categories' : {
        'bveto_jetpt50_leppt0' : ' bVeto && jetpt50 && leppt0 && mjj > 500',
        'btag_jetpt50_leppt0' : ' bReq && jetpt50 && leppt0 && mjj > 500',
        'bveto_jetpt30_leppt0' : ' bVeto && jetpt30 && leppt0 && mjj > 500',
        'btag_jetpt30_leppt0' : ' bReq && jetpt30 && leppt0 && mjj > 500',
        'bveto_jetpt30_leppt1' : ' bVeto && jetpt30 && leppt30 && mjj > 500',
        'btag_jetpt30_leppt1' : ' bReq && jetpt30 && leppt30 && mjj > 500',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
'''
cuts['wz'] = {
    'expr': 'wz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'bveto_jetpt50_leppt0' : ' bVeto && jetpt50 && leppt0',
        'btag_jetpt50_leppt0' : ' bReq && jetpt50 && leppt0',
        'bveto_jetpt30_leppt0' : ' bVeto && jetpt30 && leppt0',
        'btag_jetpt30_leppt0' : ' bReq && jetpt30 && leppt0',
        'bveto_jetpt30_leppt1' : ' bVeto && jetpt30 && leppt30',
        'btag_jetpt30_leppt1' : ' bReq && jetpt30 && leppt30',
        #'bveto_jetpt30_leppt1_ee' : ' bVeto && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==11*11',
        #'btag_jetpt30_leppt1_mumu' : ' bReq && jetpt30 && leppt30 && mjj > 500 && abs(Lepton_pdgId[0]*Lepton_pdgId[1])==13*13',
        #'bveto_jetpt30_leppt1_lowmjj' : ' bVeto && jetpt30 && leppt30 && mjj < 500',
        #'btag_jetpt30_leppt1_lowmjj' : ' bReq && jetpt30 && leppt30 && mjj < 500',
    }
}
'''
'''
cuts['zz'] = {
    'expr': 'zz_region',
    # Define the sub-categorization of sr
    'categories' : {
        'jetpt50_leppt0' : 'jetpt50 && leppt0',
        'jetpt30_leppt0' : 'jetpt30 && leppt0',
        'jetpt30_leppt1' : 'jetpt30 && leppt30',
    }
}
'''
