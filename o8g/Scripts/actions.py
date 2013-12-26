debugLevel = 0

def debugNotify(msg, *a):
  if debugLevel > 0:
    try:
      msg = msg % a
    except Exception as e:
      msg = "Error formatting log message: %s" % repr(e)
    notify(msg)


def checkMovedCard(player,card,fromGroup,toGroup,oldIndex,index,oldX,oldY,x,y,isScriptMove):
  mute()
  debugNotify("isScriptMove = %s", isScriptMove)
  if isScriptMove: return # If the card move happened via a script, then all automations should have happened already.
  if card.type == "Problem" and toGroup == table:
      card.orientation = Rot90

def checkDeck(player,groups):
  pass

def resetAll():
  pass
