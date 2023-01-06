import "../index.css"
import React, { useState } from "react"



export default function NavigationBar({myProps, updateMyProps}) {
    const [showThemeDropdown, setShowThemeDropdown] = useState(false)
    return (
        <ul className="navigationBar">
            <li><button onClick={() => console.log("New game")}><p>New Game</p></button></li>
            <li >
                <button onClick={() => setShowThemeDropdown(!showThemeDropdown)}><p>Theme</p></button>
                <ul className="themeDropdown" show={showThemeDropdown.toString()}>
                    <li>
                        <p>Colors</p>
                        <ul>
                            <li>
                                <label>Player 1</label>
                                <input type="color" name="player1-color-and-type" value={myProps.player1Color} onChange={(e) => updateMyProps({player1Color: e.target.value})} />
                            </li>
                            <li>
                                <label>Player 2</label>
                                <input type="color" name="player2-color-and-type" value={myProps.player2Color} onChange={(e) => updateMyProps({player2Color: e.target.value})} />
                            </li>
                            <li>
                                <label>Board</label>
                                <input type="color" name="board-color-and-type" value={myProps.boardColor} onChange={(e) => updateMyProps({boardColor: e.target.value})} />
                            </li>
                            <li>
                                <label>Background</label>
                                <input type="color" name="background-color-and-type" value={myProps.backgroundColor} onChange={(e) => updateMyProps({backgroundColor: e.target.value})} />
                            </li>
                        </ul>
                    </li>
                    <li>
                        <p>Styles</p>
                        <ul>
                            <li>
                                <label>Player 1</label>
                                <select value={myProps.player1PieceStyle} onChange={(e) => updateMyProps({player1PieceStyle: e.target.value})}>
                                    {myProps.pieceStyles.map(style => <option>{style}</option>)}
                                </select>
                            </li>
                            <li>
                                <label>Player 2</label>
                                <select value={myProps.player2PieceStyle} onChange={(e) => updateMyProps({player2PieceStyle: e.target.value})}>
                                    {myProps.pieceStyles.map(style => <option>{style}</option>)}
                                </select>
                            </li>
                            <li>
                                <label>Board</label>
                                <select value={myProps.boardStyle} onChange={(e) => updateMyProps({boardStyle: e.target.value})}>
                                    {myProps.boardStyles.map(style => <option>{style}</option>)}
                                </select>
                            </li>
                            <li>
                                <label>Background</label>
                                <select value={myProps.backgroundStyle} onChange={(e) => updateMyProps({backgroundStyle: e.target.value})}>
                                    {myProps.backgroundStyles.map(style => <option>{style}</option>)}
                                </select>
                            </li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    )
}