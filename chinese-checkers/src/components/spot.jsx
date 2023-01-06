import "../index.css"


function isSmallArrayInBigArray(smallArray, bigArray) {
    var currArray
    for (let i=0; i<bigArray.length; i++) {
        currArray = bigArray[i]
        if (currArray.length === smallArray.length) {
            var equalityCount = 0
            for (let j=0; j<currArray.length; j++) {
                if (smallArray[j] === currArray[j]) {
                    equalityCount++
                }
            }
            if (equalityCount == smallArray.length) return true
        }
    }
    return false
}


export default function Spot({i, j, gameState, setGameState, validMoves, myProps, updateMyProps}) {
    var isSelected = false
    if ((myProps.selectedSpot[0] === i) && (myProps.selectedSpot[1] === j)) {
        isSelected = true;
    }
    function handleClick() {
        console.log("click")
        if (myProps.selectedSpot[0] > -1) {
            const moveTuple = [myProps.selectedSpot[0], myProps.selectedSpot[1], i, j]
            console.log("------------")
            console.log(moveTuple)
            console.log("------------")
            if (isSmallArrayInBigArray(moveTuple, validMoves)) {
                let newGameState = gameState
                newGameState[i][j] = myProps.currPlayerID
                newGameState[myProps.selectedSpot[0]][myProps.selectedSpot[1]] = 0
                setGameState(newGameState)
                updateMyProps({currPlayerID: (myProps.currPlayerID % 2) + 1})
            } else {
                console.log("Error, cannot play move")
            }
            updateMyProps({selectedSpot: [-1, -1]})
        } else {
            if (isSelected) {
                updateMyProps({selectedSpot: [-1, -1]})
            } else {
                updateMyProps({selectedSpot: [i, j]})
            }
        }
    }
    if (gameState[i][j] === 1) {
        return (
            <div className="player1-occupied" onClick={handleClick} style={{"--color": myProps.player1Color, "--row": i, "--column": j}} pieceStyle={myProps.player1PieceStyle} isSelected={isSelected.toString()}></div>
        )
    } else if (gameState[i][j] === 2) {
        return (
            <div className="player2-occupied" onClick={handleClick} style={{"--color": myProps.player2Color, "--row": i, "--column": j}} pieceStyle={myProps.player2PieceStyle}  isSelected={isSelected.toString()}></div>
        )
    } else {
        return (
        <div className="inaccessible"  onClick={handleClick} style={{"--color": "black", "--row": i, "--column": j}} isSelected={isSelected.toString()}></div>
        )
    }
}