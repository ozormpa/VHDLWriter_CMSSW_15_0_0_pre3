import FWCore.ParameterSet.Config as cms

############################################################
# L1 Global Trigger Emulation
############################################################

# Conditions

from L1Trigger.Phase2L1GT.l1tGTProducer_cff import l1tGTProducer

from L1Trigger.Phase2L1GT.l1tGTSingleObjectCond_cfi import l1tGTSingleObjectCond
from L1Trigger.Phase2L1GT.l1tGTDoubleObjectCond_cfi import l1tGTDoubleObjectCond
from L1Trigger.Phase2L1GT.l1tGTTripleObjectCond_cfi import l1tGTTripleObjectCond
from L1Trigger.Phase2L1GT.l1tGTQuadObjectCond_cfi import l1tGTQuadObjectCond

from L1Trigger.Phase2L1GT.l1tGTAlgoBlockProducer_cff import algorithms

from L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.step1_2024.l1tGTObject_constants import *
from L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.step1_2024.l1tGTMenuObjects_cff import *

testCombinedPT = l1tGTDoubleObjectCond.clone(
    collection1=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    collection2=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    minCombPt = cms.double(10),
    maxCombPt = cms.double(25)
)

testAbsEta = l1tGTDoubleObjectCond.clone(
    collection1=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
        minAbsEta = cms.double(1.0),
        maxAbsEta = cms.double(2.4)
    ),
    collection2=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
        minAbsEta = cms.double(1.0),
        maxAbsEta = cms.double(2.4)
    ),
)

testPtMultiplicityCut = l1tGTDoubleObjectCond.clone(
    collection1=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
        minPtMultiplicityCut = cms.double(0),
        minPtMultiplicityN = cms.uint32(4)
    ),
    collection2=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
        minPtMultiplicityCut = cms.double(0),
        minPtMultiplicityN = cms.uint32(2)
    ),
)

testRelIsolationPt = l1tGTDoubleObjectCond.clone(
    collection1=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "CL2Electrons"),
        minRelIsolationPt=cms.double(0.1),
        maxRelIsolationPt=cms.double(20),

    ),
    collection2=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "CL2Electrons"),
        minRelIsolationPt=cms.double(0.1),
        maxRelIsolationPt=cms.double(20),

    ),
)

testQualityScoreSum = l1tGTQuadObjectCond.clone(
    collection1=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "CL2Taus"),
    ),
    collection2=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "CL2Taus"),
    ),
    collection3=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "CL2Taus"),
    ),
    collection4=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "CL2Taus"),
    ),
    minQualityScoreSum=cms.uint32(0),
    maxQualityScoreSum=cms.uint32(500),
)

testDRSquared = l1tGTDoubleObjectCond.clone(
    collection1=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    collection2=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
        minDR=cms.double(0.2),
        maxDR=cms.double(1.4),
)

testTransMass = l1tGTDoubleObjectCond.clone(
    collection1=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    collection2=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    minTransMass=cms.double(10),
    maxTransMass=cms.double(20),
)

testInvMassSqrOver2DRSqr = l1tGTDoubleObjectCond.clone(
    collection1=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    collection2=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    minInvMassOverDR=cms.double(10),
    maxInvMassOverDR=cms.double(20),
)

test3BodyInvMass = l1tGTTripleObjectCond.clone(
    collection1=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    collection2=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    collection3=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    minInvMass=cms.double(10),
    maxInvMass=cms.double(20),
)

test3BodyTransMass = l1tGTTripleObjectCond.clone(
    collection1=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    collection2=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    collection3=cms.PSet(
        tag=cms.InputTag("l1tGTProducer", "GMTTkMuons"),
    ),
    minTransMass=cms.double(10),
    maxTransMass=cms.double(20),
)

ptestCombinedPT           = cms.Path(testCombinedPT)
ptestAbsEta               = cms.Path(testAbsEta)
ptestPtMultiplicityCut    = cms.Path(testPtMultiplicityCut)
ptestRelIsolationPt       = cms.Path(testRelIsolationPt)
ptestQualityScoreSum      = cms.Path(testQualityScoreSum)
ptestDRSquared            = cms.Path(testDRSquared)
ptestTransMass            = cms.Path(testTransMass)
ptestInvMassSqrOver2DRSqr = cms.Path(testInvMassSqrOver2DRSqr)
ptest3BodyInvMass         = cms.Path(test3BodyInvMass)
ptest3BodyTransMass       = cms.Path(test3BodyTransMass)

algorithms.append(cms.PSet(expression=cms.string("ptestCombinedPT")))
algorithms.append(cms.PSet(expression=cms.string("ptestAbsEta")))
algorithms.append(cms.PSet(expression=cms.string("ptestPtMultiplicityCut")))
algorithms.append(cms.PSet(expression=cms.string("ptestRelIsolationPt")))
algorithms.append(cms.PSet(expression=cms.string("ptestQualityScoreSum")))
algorithms.append(cms.PSet(expression=cms.string("ptestDRSquared")))
algorithms.append(cms.PSet(expression=cms.string("ptestTransMass")))
algorithms.append(cms.PSet(expression=cms.string("ptestInvMassSqrOver2DRSqr")))
algorithms.append(cms.PSet(expression=cms.string("ptest3BodyInvMass")))
algorithms.append(cms.PSet(expression=cms.string("ptest3BodyTransMass")))
