import "../index.css"
import isSmallArrayInBigArray from "../utils/isSmallArrayInBigArray";


export default function Spot({i, j, makeStep, makeJump, myProps, updateMyProps}) {
    var isSelected = false
    if ((myProps.selectedSpot[0] === i) && (myProps.selectedSpot[1] === j)) {
        isSelected = true;
    }
    function handleClick(e) {
        e.stopPropagation();
        if (myProps.selectedSpot[0] > -1) {
            const moveTuple = [myProps.selectedSpot[0], myProps.selectedSpot[1], i, j]
            if (isSmallArrayInBigArray(moveTuple, myProps.validSteps)) {
                let newGameState = myProps.gameState.map(elem => [...elem])
                newGameState[i][j] = myProps.currPlayerID
                newGameState[myProps.selectedSpot[0]][myProps.selectedSpot[1]] = 0
                makeStep(newGameState)
            } else if (isSmallArrayInBigArray(moveTuple, myProps.validJumps) || ((i === myProps.doubleJumpPivotSpot[0]) && (j === myProps.doubleJumpPivotSpot[1]))) {
                let newGameState = myProps.gameState.map(elem => [...elem])
                newGameState[myProps.selectedSpot[0]][myProps.selectedSpot[1]] = 0
                newGameState[i][j] = myProps.currPlayerID
                makeJump(newGameState, [i,j])
            } else if ((myProps.selectedSpot[0] === i) && (myProps.selectedSpot[1] === j)) {
                updateMyProps({selectedSpot: [-1, -1], showThemeDropdown: false, showNewGameDropdown: false})
            } else if (myProps.doubleJumpPivotSpot[0] > -1) {
                updateMyProps({showThemeDropdown: false, showNewGameDropdown: false})
                console.log("Please confirm double jump move")
            } else {
                updateMyProps({selectedSpot: [i, j], showThemeDropdown: false, showNewGameDropdown: false})
            }
        } else {
            updateMyProps({selectedSpot: [i, j], showThemeDropdown: false, showNewGameDropdown: false})
        }
    }
    if (myProps.gameState[i][j] === 1) {
        return (
            <div className="player1-occupied" onClick={(e) => handleClick(e)} style={{"--color": myProps.player1Color, "--row": i, "--column": j}} pieceStyle={myProps.player1PieceStyle} isSelected={isSelected.toString()}></div>
        )
    } else if (myProps.gameState[i][j] === 2) {
        return (
            <div className="player2-occupied" onClick={(e) => handleClick(e)} style={{"--color": myProps.player2Color, "--row": i, "--column": j}} pieceStyle={myProps.player2PieceStyle}  isSelected={isSelected.toString()}></div>
        )
    } else {
        return (
        <div className="inaccessible"  onClick={(e) => handleClick(e)} style={{"--color": "black", "--row": i, "--column": j}} isSelected={isSelected.toString()}></div>
        )
    }
}