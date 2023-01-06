import "../index.css"
import React, { useState } from "react"
import Spot from "./spot"

const defaultGameState = [
    [0,0,0,0,0,2,2,2,2],
    [0,0,0,0,0,0,2,2,2],
    [0,0,0,0,0,0,0,2,2],
    [0,0,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0,0]
]

export default function Game({myProps, updateMyProps}) {
    const [gameState, setGameState] = useState(defaultGameState)
    return (
        <div className="game" style={{background: myProps.backgroundColor}}>
            <div className="board" style={{background: myProps.boardColor}}>
                {[...Array(9).keys()].map(i=> [...Array(9).keys()].map(j => <Spot i={i} j={j} gameState={gameState} myProps={myProps} updateMyProps={updateMyProps} />))}
            </div>
        </div>
    )
}