from enum import Enum

class Direction (Enum):
    n  =1 << 0 # 0b00000001
    ne =1 << 1 # 0b00000010
    e  =1 << 2 # 0b00000100
    se =1 << 3 # 0b00001000
    s  =1 << 4 # 0b00010000
    sw =1 << 5 # 0b00100000
    w  =1 << 6 # 0b01000000
    nw =1 << 7 # 0b10000000
 
class node():
    """
    Node class is a representing a node in a grid system
    The interconnections between nodes is given by the linkage to other nodes
       NW   N   NE
          \ | /        
       W  - ^ -  E
          / | \
       SW   S   SE
    Orientation is used in world coordinates as the map is layout
    or relative to the movement direction ie we move always relative to the nord direction.
    """
 
    myID = 0
    _s_Node = 0
    _seNode = 0
    _e_Node = 0
    _neNode = 0
    _n_Node = 0
    _nwNode = 0
    _w_Node = 0
    _swNode = 0
    _moveMask = 0
 
    def __init__(self) :
        pass
 
    def setw_Node( self, nodeID):
        _w_Node = nodeID
        self.updateMoveMask()
   
    def sete_Node( self, nodeID):
        _e_Node = nodeID
        self.updateMoveMask()
   
    def setn_Node( self, nodeID):
        _n_Node = nodeID
        self.updateMoveMask()
   
    def sets_Node( self,nodeID):
        _s_Node = nodeID
        self.updateMoveMask()
 
    def setMoveMask(self):
        moveMask = 0
       
        if (self._n_Node != 0):
            moveMask = Direction.n
        if (self._neNode != 0):
            moveMask = Direction.ne
        if self._e_Node != 0 :
            moveMask = moveMask | Direction.e
        if self._seNode != 0 :
            moveMask = moveMask | Direction.se
        if self._s_Node != 0 :
            moveMask = moveMask | Direction.s
        if self._swNode != 0 :
            moveMask = moveMask | Direction.sw
        if self._w_Node != 0 :
            moveMask = moveMask | Direction.w
        if self._nwNode != 0 :
            moveMask = moveMask | Direction.nw
 
        self._moveMask = moveMask | moveMask << 8
 
    def getMoveCapability(self,prevNode):
        """
        prevnode: is the node where we are comming from.
        return: returns a bitpattern that tells us that we can move backwards (bit 0), right (bit 1), forward (bit 2) or left (bit 3)
                given the direction we are comming from
        """
        match prevNode:
            case self._n_Node:
                return self._moveMask & 0b0000000011111111
            case self._neNode:
                return (self._moveMask >> 1) & 0b0000000011111111
            case self._e_Node:
                return (self._moveMask >> 2) & 0b0000000011111111
            case self._seNode:
                return (self._moveMask >> 3) & 0b0000000011111111
            case self._s_Node:
                return (self._moveMask >> 4) & 0b0000000011111111
            case self._swNode:
                return (self._moveMask >> 5) & 0b0000000011111111
            case self._w_Node:
                return (self._moveMask >> 6) & 0b0000000011111111
            case self._nwNode:
                return (self._moveMask >> 7) & 0b0000000011111111
 
    
    def canMoveNord (self,prevNode):
        return (self.getMoveCapability(prevNode) & Direction.n) != 0
   
    def canMoveNordEast (self,prevNode):
        return (self.getMoveCapability(prevNode) & Direction.ne) != 0
   
    def canMoveEast (self,prevNode):
        return (self.getMoveCapability(prevNode) & Direction.e) != 0
   
    def canMoveSouthEast (self,prevNode):
        return (self.getMoveCapability(prevNode) & Direction.se) != 0
   
    def canMoveSouth (self,prevNode):
        return (self.getMoveCapability(prevNode) & Direction.s) != 0
   
    def canMoveSouthWest (self,prevNode):
        return (self.getMoveCapability(prevNode) & Direction.sw) != 0
    
    def canMoveWest (self,prevNode):
        return (self.getMoveCapability(prevNode) & Direction.w) != 0
    
    def canMoveNordWest (self,prevNode):
        return (self.getMoveCapability(prevNode) & Direction.nw) != 0
   
    def canMoveForward (self,prevNode):
        return self.canMoveNord(self, prevNode)
    def canMoveRight (self,prevNode):
        return self.canMoveEast(self, prevNode)
    def canMoveBack (self,prevNode):
        return self.canMoveSouth(self, prevNode)
    def canMoveLeft (self,prevNode):
        return self.canMoveWest(self, prevNode)

    def getNextNode(self, moveDirection,prevNode):
        # are we allowed to move where we want to go ?
        match moveDirection:
            case Direction.n:
                if ~self.canMoveNord(prevNode): return                
            case Direction.ne:
                if ~self.canMoveNordEast(prevNode): return                
            case Direction.e:
                if ~self.canMoveEast(prevNode): return                
            case Direction.e:
                if ~self.canMoveSouthEast(prevNode): return                
            case Direction.s:
                if ~self.canMoveSouth(prevNode): return
            case Direction.sw:
                if ~self.canMoveSouthWest(prevNode): return
            case Direction.w:
                if ~self.canMoveWest(prevNode): return
            case Direction.nw:
                if ~self.canMoveNordWest(prevNode): return
            case _:
                return 0
        # determine the bitshift that is needed            
        match prevNode:
            case self._n_Node:
                worldDirection = moveDirection
            case self._neNode:
                worldDirection = moveDirection << 1
            case self._e_Node:
                worldDirection = moveDirection << 2
            case self._seNode:
                worldDirection = moveDirection << 3
            case self._s_Node:
                worldDirection = moveDirection << 4
            case self._sw_Node:
                worldDirection = moveDirection << 5
            case self._w_Node:
                worldDirection = moveDirection << 6
            case self._nw_Node:
                worldDirection = moveDirection << 7
        # if no direction bit in the last 4 bits throw away the last nibble
        if ~(worldDirection & 0b0000000011111111):
            worldDirection = worldDirection >> 8
        match worldDirection:
            case Direction.n :
                return self._n_Node
            case Direction.ne :
                return self._neNode
            case Direction.e :
                return self._e_Node
            case Direction.se :
                return self._seNode
            case Direction.s :
                return self._s_Node
            case Direction.sw :
                return self._swNode
            case Direction.w :
                return self._w_Node
            case Direction.nw :
                return self._nwNode