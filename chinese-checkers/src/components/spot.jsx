import "../index.css"

export default function Spot({i, j, gameState, myProps, updateMyProps}) {
    var isSelected = false
    if ((myProps.selectedSpot[0] === i) && (myProps.selectedSpot[1] === j)) {
        isSelected = true;
    }
    function handleClick() {
        if (isSelected) {
            updateMyProps({selectedSpot: [-1, -1]})
        } else {
            updateMyProps({selectedSpot: [i, j]})
        }
    }
    if (gameState[i][j] === 1) {
        return (
            <div className="player1-occupied" onClick={handleClick} style={{"--color": myProps.player1Color}} pieceStyle={myProps.player1PieceStyle} isSelected={isSelected.toString()}></div>
        )
    } else if (gameState[i][j] === 2) {
        return (
            <div className="player2-occupied" onClick={handleClick} style={{"--color": myProps.player2Color}} pieceStyle={myProps.player2PieceStyle}  isSelected={isSelected.toString()}></div>
        )
    } else {
        return (
        <div className="inaccessible"  onClick={handleClick} isSelected={isSelected.toString()}></div>
        )
    }
}