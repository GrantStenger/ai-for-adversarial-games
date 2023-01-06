import "../index.css"
import React, { useState } from "react"
import defaultGameState from "../utils/defaultGameState"
import getValidMoves from "../utils/getValidMoves"


export default function NavigationBar({myProps, updateMyProps}) {
    
    const [tempPlayer1Color, setTempPlayer1Color] = useState(myProps.player1Color)
    const [tempPlayer2Color, setTempPlayer2Color] = useState(myProps.player2Color)
    const [tempBoardColor, setTempBoardColor] = useState(myProps.boardColor)
    const [tempBackgroundColor, setTempBackgroundColor] = useState(myProps.backgroundColor)
    const [tempPlayer1PieceStyle, setTempPlayer1PieceStyle] = useState(myProps.player1PieceStyle)
    const [tempPlayer2PieceStyle, setTempPlayer2PieceStyle] = useState(myProps.player2PieceStyle)
    const [tempBoardStyle, setTempBoardStyle] = useState(myProps.boardStyle)
    const [tempBackgroundStyle, setTempBackgroundStyle] = useState(myProps.backgroundStyle)
    
    function newGame() {
        updateMyProps({
          gameState: defaultGameState(),
          currPlayerID: 1,
          validMoves: getValidMoves(defaultGameState(), 1),
          selectedSpot: [-1, -1]
        })
      }
      function applyTheme() {
        updateMyProps({
            player1Color: tempPlayer1Color,
            player2Color: tempPlayer2Color,
            boardColor: tempBoardColor,
            backgroundColor: tempBackgroundColor,
            player1PieceStyle: tempPlayer1PieceStyle,
            player2PieceStyle: tempPlayer2PieceStyle,
            boardStyle: tempBoardStyle,
            backgroundStyle: tempBackgroundStyle
        })
      }
      function revertThemeChanges() {
        setTempPlayer1Color(myProps.player1Color)
        setTempPlayer2Color(myProps.player2Color)
        setTempBoardColor(myProps.boardColor)
        setTempBackgroundColor(myProps.backgroundColor)
        setTempPlayer1PieceStyle(myProps.player1PieceStyle)
        setTempPlayer2PieceStyle(myProps.player2PieceStyle)
        setTempBoardStyle(myProps.boardStyle)
        setTempBackgroundStyle(myProps.backgroundStyle)
      }
      function applyDefaultTheme() {
          updateMyProps({
              player1Color: "#0000FF",
              player2Color: "#FF0000",
              boardColor: "#00FF00",
              backgroundColor: "#FFFFFF",
              player1PieceStyle: "style1",
              player2PieceStyle: "style1",
              boardStyle: "style1",
              backgroundStyle: "style1",
            })
            setTempPlayer1Color("#0000FF")
            setTempPlayer2Color("#FF0000")
            setTempBoardColor("#00FF00")
            setTempBackgroundColor("#FFFFFF")
            setTempPlayer1PieceStyle("style1")
            setTempPlayer2PieceStyle("style1")
            setTempBoardStyle("style1")
            setTempBackgroundStyle("style1")
      }
    return (
        <ul className="navigationBar">
            <li>
                <button onClick={(e) => {e.stopPropagation(); updateMyProps({showNewGameDropdown: !myProps.showNewGameDropdown, showThemeDropdown: false})}}><p>New Game</p></button>
                <div className="dropdown" show={myProps.showNewGameDropdown.toString()} onClick={(e) => e.stopPropagation()}>
                    <ul>
                        <li>
                            <p>Opponent</p>
                            <ul>
                                <li>
                                    <label>Computer</label>
                                    <select value={myProps.computerStrength} onChange={(e) => updateMyProps({computerStrength: e.target.value})}>
                                        {myProps.computerStrengthLevels.map(level => <option>{level}</option>)}
                                    </select>
                                </li>
                                <li>Human</li>
                            </ul>
                        </li>
                        <li>
                            <p>Time Controls</p>
                            <ul>
                                <li>
                                    <label>Time Limit</label>
                                    <select value={myProps.timeLimit} onChange={(e) => updateMyProps({timeLimit: e.target.value})}>
                                        {myProps.timeLimits.map(limit => <option>{limit}</option>)}
                                    </select>
                                </li>
                                <li>
                                    <label>Increment</label>
                                    <select value={myProps.increment} onChange={(e) => updateMyProps({increment: e.target.value})}>
                                        {myProps.increments.map(increment => <option>{increment}</option>)}
                                    </select>
                                </li>
                            </ul>
                        </li>
                    </ul>
                    <button onClick={newGame}><p>Begin New Game</p></button>
                </div>
            </li>
            <li >
                <button onClick={(e) => {e.stopPropagation(); updateMyProps({showThemeDropdown: !myProps.showThemeDropdown, showNewGameDropdown: false})}}><p>Theme</p></button>
                <div className="dropdown" show={myProps.showThemeDropdown.toString()} onClick={(e) => e.stopPropagation()}>
                    <ul>
                        <li>
                            <p>Colors</p>
                            <ul>
                                <li>
                                    <label>Player 1</label>
                                    <input type="color" name="player1-color-and-type" value={tempPlayer1Color} onChange={(e) => setTempPlayer1Color(e.target.value)} />
                                </li>
                                <li>
                                    <label>Player 2</label>
                                    <input type="color" name="player2-color-and-type" value={tempPlayer2Color} onChange={(e) => setTempPlayer2Color(e.target.value)} />
                                </li>
                                <li>
                                    <label>Board</label>
                                    <input type="color" name="board-color-and-type" value={tempBoardColor} onChange={(e) => setTempBoardColor(e.target.value)} />
                                </li>
                                <li>
                                    <label>Background</label>
                                    <input type="color" name="background-color-and-type" value={tempBackgroundColor} onChange={(e) => setTempBackgroundColor(e.target.value)} />
                                </li>
                            </ul>
                        </li>
                        <li>
                            <p>Styles</p>
                            <ul>
                                <li>
                                    <label>Player 1</label>
                                    <select value={tempPlayer1PieceStyle} onChange={(e) => setTempPlayer1PieceStyle(e.target.value)}>
                                        {myProps.pieceStyles.map(style => <option>{style}</option>)}
                                    </select>
                                </li>
                                <li>
                                    <label>Player 2</label>
                                    <select value={tempPlayer2PieceStyle} onChange={(e) => setTempPlayer2PieceStyle(e.target.value)}>
                                        {myProps.pieceStyles.map(style => <option>{style}</option>)}
                                    </select>
                                </li>
                                <li>
                                    <label>Board</label>
                                    <select value={tempBoardStyle} onChange={(e) => setTempBoardStyle(e.target.value)}>
                                        {myProps.boardStyles.map(style => <option>{style}</option>)}
                                    </select>
                                </li>
                                <li>
                                    <label>Background</label>
                                    <select value={tempBackgroundStyle} onChange={(e) => setTempBackgroundStyle(e.target.value)}>
                                        {myProps.backgroundStyles.map(style => <option>{style}</option>)}
                                    </select>
                                </li>
                            </ul>
                        </li>
                    </ul>
                    <button onClick={applyTheme}><p>Apply Selection</p></button>
                    <button onClick={revertThemeChanges}><p>Revert to Current</p></button>
                    <button onClick={applyDefaultTheme}><p>Revert to Default</p></button>
                </div>
            </li>
        </ul>
    )
}