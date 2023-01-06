import "../index.css"
import React, { useState } from "react"
import Spot from "./spot"

export default function Game({myProps, updateMyProps, updateGameState}) {

    return (
        <div className="game" style={{"--gameColor": myProps.backgroundColor}} >
            <div className="board" style={{"--boardColor": myProps.boardColor}}>
                {[...Array(9).keys()].map(i=> [...Array(9).keys()].map(j => <Spot i={i} j={j} updateGameState={updateGameState} myProps={myProps} updateMyProps={updateMyProps} />))}
            </div>
        </div>
    )
}