debugLevel = 0

scoreCardID = "eff15a21-6e14-11e3-9bd2-e0cb4ee82d3a"
turnCardID = "f04ce79e-6e14-11e3-afbe-e0cb4ee82d3a"


def debugNotify(msg, *a):
  if debugLevel > 0:
    try:
      msg = msg % a
    except Exception as e:
      msg = "Error formatting log message: %s" % repr(e)
    notify(msg)

def flip(card, x = 0, y = 0):
    mute()
    if card.type == "Mane":
      if card.alternate == 'boosted':
        notify("{} flips {} to the Start side.".format(me, card))
        card.switchTo('')
      else:
        notify("{} flips {} to the Boosted side.".format(me, card))
        card.switchTo('boosted')
    else:
      if card.isFaceUp == True:
        notify("{} flips {} face down.".format(me, card))
        card.isFaceUp = False
      else:
        card.isFaceUp = True
        notify("{} flips {} face up.".format(me, card))

def shuffle(group, x = 0, y = 0):
  group.shuffle()


def checkMovedCard(player,card,fromGroup,toGroup,oldIndex,index,oldX,oldY,x,y,isScriptMove):
  mute()
  debugNotify("isScriptMove = %s", isScriptMove)
  if isScriptMove: return # If the card move happened via a script, then all automations should have happened already.
  if card.type == "Problem" and toGroup == table and not (card.orientation & Rot90):
      card.orientation |= Rot90

def createReferenceCards(group, x=0, y=0):
  table.create(scoreCardID, 0, 0, 1)
  table.create(turnCardID, 99, 0, 1)

def tap(card, x=0, y=0):
  card.orientation ^= Rot90

def resetAll():
  pass
