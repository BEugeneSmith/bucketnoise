# TODO: add method to correctly output the key.

from collections import OrderedDict

PITCHES = ['C','C#/Db','D','Eb/D#','E','F','F#/Gb','G','G#/Ab','A','Bb','B']

MODES = ['MAJOR','MELODICMINOR','MELODICMINOR']

MAJOR = [0,2,4,5,7,9,11]
NATURALMINOR = [0,2,3,5,7,8,10]
MELODICMINOR = [0,2,3,5,7,8,11]

class scale:

    def __init__(self,key,mode='MAJOR'):
        self.scale = self.__generateScale(key,mode)
        self.chords = self.__generateDiatonicChords()
        self.chordTypes = self.__applyChordTypes()

        self.scale_name = self.scale[0] + ' ' + mode

    def __generateScale(self,key,mode='MAJOR'):
        ''' generates given a pitch and modern mode '''
        keyId = PITCHES.index(key)
        partScale = list(range(keyId,len(PITCHES)))
        for i in range(0,keyId):
            partScale.append(i)
        newScaleIds = list(map(lambda x: PITCHES[x], partScale))

        if mode == 'MAJOR':
            newScale = list(map(lambda x: newScaleIds[x], MAJOR ))
        elif mode == 'NATURALMINOR':
            newScale = list(map(lambda x: newScaleIds[x], NATURALMINOR ))
        elif mode == 'MELODICMINOR':
            newScale = list(map(lambda x: newScaleIds[x], MELODICMINOR))
        return newScale

    def __generateDiatonicChords(self):
        ''' generate chords for each degree of the scale '''
        scale = self.scale + self.scale
        scaleDict = OrderedDict()

        for i in range(7):
            scaleDict[scale[i]] = scale[i:(i+5):2]
        return scaleDict

    def __determineChordType(self,chord):
        chromaticScale = PITCHES+PITCHES

        d1 = chromaticScale.index(chord[0])
        d2 = chromaticScale.index(chord[1])
        d3 = chromaticScale.index(chord[2])

        if d2 < d1:
            d2 += 12

        if d3 < d1:
            d3 += 12

        dyad1 = d2-d1
        dyad2 = d3-d2

        if dyad1 == 3 and dyad2 == 4:
            return 'minor'
        elif dyad1 == 4 and dyad2 == 3:
            return 'major'
        elif dyad1 == 4 and dyad2 == 4:
            return 'augmented'
        elif dyad1 == 3 and dyad2 == 3:
            return 'diminished'

    def __applyChordTypes(self):
        chordType = OrderedDict()
        for degree in self.chords.keys():
            chordType[degree] = self.__determineChordType(self.chords[degree])
        return chordType
